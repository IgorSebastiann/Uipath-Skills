#!/usr/bin/env python3
"""Consulta metadados do feed NuGet oficial do UiPath usando apenas a stdlib."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request


DEFAULT_FEED = (
    "https://pkgs.dev.azure.com/uipath/Public.Feeds/"
    "_packaging/UiPath-Official/nuget/v3/index.json"
)
USER_AGENT = "uipath-skills/1.0"


def get_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def resources(feed: str) -> tuple[str, str]:
    index = get_json(feed)
    search = None
    registrations = None
    for item in index.get("resources", []):
        kind = item.get("@type", "")
        if search is None and "SearchQueryService" in kind:
            search = item.get("@id")
        if registrations is None and "RegistrationsBaseUrl" in kind:
            registrations = item.get("@id")
    if not search or not registrations:
        raise RuntimeError("O feed não expôs os serviços NuGet esperados.")
    return search, registrations


def search_packages(service: str, query: str, take: int) -> dict:
    params = urllib.parse.urlencode(
        {"q": query, "skip": 0, "take": take, "prerelease": "false"}
    )
    return get_json(f"{service}?{params}")


def registration(registrations: str, package_id: str) -> dict:
    base = registrations.rstrip("/") + "/"
    encoded = urllib.parse.quote(package_id.lower(), safe="")
    return get_json(f"{base}{encoded}/index.json")


def registration_leaves(document: dict) -> list[dict]:
    leaves: list[dict] = []
    for page in document.get("items", []):
        page_items = page.get("items")
        if page_items is None and page.get("@id"):
            page_items = get_json(page["@id"]).get("items", [])
        leaves.extend(page_items or [])
    return leaves


def version_key(value: str) -> tuple:
    main, _, suffix = value.partition("-")
    numbers = tuple(int(part) if part.isdigit() else part for part in main.split("."))
    return numbers, suffix == "", suffix


def official_items(items: list[dict]) -> list[dict]:
    # O feed é a fonte oficial configurada no Studio. O prefixo reduz resultados
    # acidentais que não usam o namespace público padrão da UiPath.
    return [item for item in items if item.get("id", "").lower().startswith("uipath.")]


def command_search(args: argparse.Namespace, search_service: str, _: str) -> None:
    result = search_packages(search_service, args.query, args.take)
    items = official_items(result.get("data", []))
    output = [
        {
            "id": item.get("id"),
            "version": item.get("version"),
            "description": item.get("description"),
            "authors": item.get("authors"),
            "projectUrl": item.get("projectUrl"),
        }
        for item in items
    ]
    print(json.dumps(output, ensure_ascii=False, indent=2))


def command_versions(args: argparse.Namespace, _: str, registrations: str) -> None:
    leaves = registration_leaves(registration(registrations, args.package_id))
    versions = sorted(
        {
            leaf.get("catalogEntry", {}).get("version")
            for leaf in leaves
            if leaf.get("catalogEntry", {}).get("version")
        },
        key=version_key,
        reverse=True,
    )
    if not args.prerelease:
        versions = [version for version in versions if "-" not in version]
    print(json.dumps(versions, ensure_ascii=False, indent=2))


def command_package(args: argparse.Namespace, _: str, registrations: str) -> None:
    leaves = registration_leaves(registration(registrations, args.package_id))
    entries = [leaf.get("catalogEntry", {}) for leaf in leaves]
    if not args.prerelease:
        entries = [entry for entry in entries if "-" not in entry.get("version", "")]
    entries.sort(key=lambda entry: version_key(entry.get("version", "0")), reverse=True)
    if not entries:
        raise RuntimeError(f"Pacote não encontrado: {args.package_id}")
    entry = entries[0]
    dependency_groups = entry.get("dependencyGroups") or []
    dependencies = sorted(
        {
            dependency.get("id")
            for group in dependency_groups
            for dependency in (group.get("dependencies") or [])
            if dependency.get("id")
        }
    )
    output = {
        "id": entry.get("id"),
        "latestStableVersion": entry.get("version"),
        "description": entry.get("description"),
        "authors": entry.get("authors"),
        "published": entry.get("published"),
        "projectUrl": entry.get("projectUrl"),
        "targetFrameworks": [
            group.get("targetFramework")
            for group in dependency_groups
            if group.get("targetFramework")
        ],
        "dependencies": dependencies,
        "note": "Confirme suporte e compatibilidade nas release notes e no Activities Lifecycle.",
    }
    if args.full:
        output["dependencyGroups"] = dependency_groups
    print(json.dumps(output, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--feed", default=DEFAULT_FEED, help="Índice NuGet v3.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    search_parser = subparsers.add_parser("search", help="Pesquisa pacotes.")
    search_parser.add_argument("query")
    search_parser.add_argument("--take", type=int, default=30)
    search_parser.set_defaults(handler=command_search)

    versions_parser = subparsers.add_parser("versions", help="Lista versões.")
    versions_parser.add_argument("package_id")
    versions_parser.add_argument("--prerelease", action="store_true")
    versions_parser.set_defaults(handler=command_versions)

    package_parser = subparsers.add_parser("package", help="Mostra a versão estável mais recente.")
    package_parser.add_argument("package_id")
    package_parser.add_argument("--prerelease", action="store_true")
    package_parser.add_argument("--full", action="store_true", help="Inclui metadados completos das dependências.")
    package_parser.set_defaults(handler=command_package)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        search_service, registrations = resources(args.feed)
        args.handler(args, search_service, registrations)
        return 0
    except Exception as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
