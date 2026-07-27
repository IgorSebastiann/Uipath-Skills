# UiPath Skills

**English** | [Português (Brasil)](README.pt-BR.md)

[![skills.sh](https://skills.sh/b/IgorSebastiann/Uipath-Skills)](https://skills.sh/IgorSebastiann/Uipath-Skills)

An agent skill for researching, comparing, and recommending official UiPath packages and activities.

It helps automation developers choose activities, evaluate supported and LTS versions, verify project compatibility, inspect dependencies, plan migrations, and design workflows without relying on a static catalog that quickly becomes outdated.

## Quick install

Run the interactive `skills` CLI:

```bash
npx skills add IgorSebastiann/Uipath-Skills
```

The installer displays the terminal interface, detects supported AI agents on your machine, and lets you choose the installation scope and method.

To install `uipath-skills` globally for specific agents without prompts:

```bash
npx skills add IgorSebastiann/Uipath-Skills --skill uipath-skills --global --agent codex --agent claude-code --yes
```

The CLI supports Codex, Claude Code, Cursor, GitHub Copilot, Windsurf, Gemini CLI, Cline, OpenCode, and many other agents.

## What this skill does

- Searches only packages officially published and supported by UiPath.
- Queries stable package versions from the official UiPath NuGet feed.
- Prioritizes currently supported and LTS-aligned versions.
- Checks compatibility with:
  - UiPath Studio and StudioX;
  - Windows;
  - Windows - Legacy;
  - Cross-platform.
- Compares Modern and Classic activities.
- Evaluates dependencies, requirements, and upgrade risks.
- Recommends packages and activities for specific automation scenarios.
- Proposes UiPath workflow structures.
- Inspects supplied `project.json` and XAML files.
- Helps plan project and package migrations.
- Verifies mutable version claims against official documentation, release notes, and lifecycle pages.

## Scope

This skill covers official UiPath packages only.

Partner, Marketplace, and community packages are outside its recommendation scope. A version is not considered supported merely because it exists in a NuGet feed: support status must also be verified through UiPath Activities Lifecycle or official release notes.

## Repository structure

```text
Uipath-Skills/
├── SKILL.md
├── README.md
├── README.pt-BR.md
├── LICENSE
├── skills.sh.json
├── references/
│   ├── official-sources.md
│   └── package-map.md
├── scripts/
│   └── query_uipath_feed.py
└── evals/
    └── evals.json
```

- `SKILL.md`: core workflow loaded by the agent.
- `references/official-sources.md`: official source map and evidence rules.
- `references/package-map.md`: functional index for package discovery.
- `scripts/query_uipath_feed.py`: queries the official UiPath NuGet feed.
- `evals/evals.json`: realistic evaluation scenarios.
- `skills.sh.json`: skills.sh repository-page configuration.

## Requirements

- An AI coding agent that supports Agent Skills.
- Internet access for current documentation and package metadata.
- Node.js with `npx` for interactive installation.
- Python 3 for the optional NuGet feed query script.
- Git only when installing manually.

The Python script uses the standard library and requires no additional Python packages.

## Install with the skills CLI

### Interactive installation

```bash
npx skills add IgorSebastiann/Uipath-Skills
```

The CLI will:

1. discover `uipath-skills` from the repository;
2. detect compatible agents installed on the machine;
3. let you select project or global scope;
4. let you select symlink or copy installation;
5. install the skill into the correct agent directories.

### List without installing

```bash
npx skills add IgorSebastiann/Uipath-Skills --list
```

### Install globally

```bash
npx skills add IgorSebastiann/Uipath-Skills --skill uipath-skills --global
```

### Install for Codex

```bash
npx skills add IgorSebastiann/Uipath-Skills --skill uipath-skills --agent codex
```

### Install for Claude Code

```bash
npx skills add IgorSebastiann/Uipath-Skills --skill uipath-skills --agent claude-code
```

### Install for multiple agents

```bash
npx skills add IgorSebastiann/Uipath-Skills \
  --skill uipath-skills \
  --agent codex \
  --agent claude-code \
  --agent cursor
```

### Install non-interactively

Useful for setup scripts and CI environments:

```bash
npx skills add IgorSebastiann/Uipath-Skills \
  --skill uipath-skills \
  --global \
  --agent codex \
  --yes
```

### Use without installing

Generate a temporary skill prompt:

```bash
npx skills use IgorSebastiann/Uipath-Skills --skill uipath-skills
```

### Manage the installation

```bash
# List installed skills
npx skills list

# Update this skill
npx skills update uipath-skills

# Remove this skill
npx skills remove uipath-skills
```

## Manual installation

### Codex — global

#### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
git clone https://github.com/IgorSebastiann/Uipath-Skills.git "$HOME\.codex\skills\uipath-skills"
```

#### Linux or macOS

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/IgorSebastiann/Uipath-Skills.git ~/.codex/skills/uipath-skills
```

### Codex — project scope

From the project root:

```bash
mkdir -p .agents/skills
git clone https://github.com/IgorSebastiann/Uipath-Skills.git .agents/skills/uipath-skills
```

### Claude Code — global

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/IgorSebastiann/Uipath-Skills.git ~/.claude/skills/uipath-skills
```

Restart the agent if the newly installed skill is not detected immediately.

## How to use

Skills can be activated explicitly or automatically.

### Explicit invocation

In Codex CLI or the IDE extension, mention the skill with `$`:

```text
$uipath-skills

I use UiPath Studio 2024.10 LTS with a Windows project.
I need to read an Excel file, filter pending records, and save the result
to another sheet. Recommend official packages and activities.
```

You can also run `/skills` and select `uipath-skills`.

In ChatGPT or another interface that supports skill mentions, select the skill using the interface's skill picker.

### Automatic activation

An agent may automatically select the skill when a request mentions:

- UiPath Studio or StudioX;
- UiPath activities;
- `UiPath.*` packages;
- LTS versions;
- Windows, Windows-Legacy, or Cross-platform;
- package migrations;
- `project.json`;
- XAML workflows;
- UiPath compatibility or dependencies.

Example:

```text
I have a Windows-Legacy project in Studio 2023.10.
Can I update UiPath.IntelligentOCR.Activities to the newest version?
Analyze compatibility and propose a safe migration.
```

## Example prompts

### Choose activities

```text
$uipath-skills

Which official activities should I use to read emails with attachments,
save only PDF files, and register the results in an Orchestrator queue?
My project is Windows and uses Studio 2025.10 LTS.
```

### Compare versions

```text
$uipath-skills

Compare supported UiPath.Excel.Activities versions for Studio 2024.10 LTS.
Show compatibility, important changes, and upgrade risks.
```

### Inspect a project

```text
$uipath-skills

Inspect this project's project.json and XAML files. Identify unsupported
packages, compatibility problems, and activities that should be modernized.
```

Provide the project files so the skill can inspect the actual dependencies.

### Design a workflow

```text
$uipath-skills

Design a Cross-platform workflow that monitors new Google Drive files,
prevents duplicates, and creates Orchestrator Queue Items. Include packages,
activities, arguments, authentication, and failure handling.
```

## Information that improves recommendations

Whenever possible, provide:

1. UiPath Studio and Robot versions;
2. the LTS product line;
3. project compatibility type;
4. Studio or StudioX profile;
5. currently installed packages;
6. automation goal;
7. environment, authentication, or governance restrictions;
8. relevant `project.json`, XAML, or log files.

If some details are unavailable, the skill may work with assumptions while clearly identifying which assumptions affect the recommendation.

## Query the official feed manually

The bundled script queries packages and versions published to the official UiPath NuGet feed.

### Search packages

```bash
python scripts/query_uipath_feed.py search "Excel"
```

### List versions

```bash
python scripts/query_uipath_feed.py versions UiPath.Excel.Activities
```

Include prerelease versions:

```bash
python scripts/query_uipath_feed.py versions UiPath.Excel.Activities --prerelease
```

### Inspect a package

```bash
python scripts/query_uipath_feed.py package UiPath.Excel.Activities
```

Include complete dependency-group metadata:

```bash
python scripts/query_uipath_feed.py package UiPath.Excel.Activities --full
```

The feed proves that a package version was published. It does not prove by itself that the version is currently supported or aligned with an LTS release.

## Source priority

The skill prioritizes:

1. official activity documentation;
2. official package compatibility pages;
3. package release notes;
4. UiPath Activities Lifecycle;
5. UiPath Activities Overview;
6. the official UiPath NuGet feed.

See [references/official-sources.md](references/official-sources.md) for the complete source map and evidence rules.

## Limitations

- The UiPath catalog changes continuously, so versions are intentionally not frozen in `SKILL.md`.
- Integration Service activities can follow a different update and distribution model from classic activity packages.
- Individual activities can have narrower compatibility than their containing package.
- XAML generated without the project's files and dependencies must be treated as a draft.
- The skill does not publish processes or modify Orchestrator without explicit authorization.

## Development and validation

Validate the Python script:

```bash
python -m py_compile scripts/query_uipath_feed.py
```

Run a real feed query:

```bash
python scripts/query_uipath_feed.py package UiPath.Excel.Activities
```

Evaluation scenarios are available in [evals/evals.json](evals/evals.json).

## Contributing

Contributions are welcome, especially for:

- expanding the functional package map;
- adding evaluation scenarios;
- improving compatibility guidance;
- fixing changed official links;
- improving the feed query script.

When contributing:

1. keep recommendations limited to official UiPath packages;
2. use official documentation as evidence;
3. do not label a version as current without a date and evidence;
4. validate the script;
5. add or update evaluations when behavior changes.

## License

This project is distributed under the terms in [LICENSE](LICENSE).

