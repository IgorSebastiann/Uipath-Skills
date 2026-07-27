# UiPath Skills

[English](README.md) | **Português (Brasil)**

[![skills.sh](https://skills.sh/b/IgorSebastiann/Uipath-Skills)](https://skills.sh/IgorSebastiann/Uipath-Skills)

Uma skill para agentes que pesquisa, compara e recomenda pacotes e atividades oficiais do UiPath.

Ela ajuda desenvolvedores de automações a escolher atividades, avaliar versões suportadas e LTS, verificar compatibilidade do projeto, analisar dependências, planejar migrações e desenhar workflows sem depender de um catálogo estático que rapidamente ficaria desatualizado.

## Instalação rápida

Execute o CLI interativo `skills`:

```bash
npx skills add IgorSebastiann/Uipath-Skills
```

O instalador exibe uma interface no terminal, detecta os agentes de IA compatíveis disponíveis na máquina e permite escolher o escopo e o método de instalação.

Para instalar `uipath-skills` globalmente em agentes específicos, sem perguntas:

```bash
npx skills add IgorSebastiann/Uipath-Skills --skill uipath-skills --global --agent codex --agent claude-code --yes
```

O CLI é compatível com Codex, Claude Code, Cursor, GitHub Copilot, Windsurf, Gemini CLI, Cline, OpenCode e muitos outros agentes.

## O que esta skill faz

- Pesquisa somente pacotes publicados e suportados oficialmente pela UiPath.
- Consulta versões estáveis no feed NuGet oficial da UiPath.
- Prioriza versões atualmente suportadas e alinhadas às linhas LTS.
- Verifica compatibilidade com:
  - UiPath Studio e StudioX;
  - Windows;
  - Windows - Legacy;
  - Cross-platform.
- Compara atividades Modern e Classic.
- Avalia dependências, requisitos e riscos de atualização.
- Recomenda pacotes e atividades para cenários específicos de automação.
- Propõe estruturas de workflows UiPath.
- Analisa arquivos `project.json` e XAML fornecidos.
- Ajuda a planejar migrações de projetos e pacotes.
- Confirma informações mutáveis sobre versões na documentação oficial, nas release notes e nas páginas de lifecycle.

## Escopo

Esta skill cobre somente pacotes oficiais da UiPath.

Pacotes de parceiros, Marketplace e comunidade estão fora do escopo de recomendação. Uma versão não é considerada suportada apenas porque existe em um feed NuGet: o suporte também precisa ser confirmado no UiPath Activities Lifecycle ou nas release notes oficiais.

## Estrutura do repositório

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

- `SKILL.md`: workflow principal carregado pelo agente.
- `references/official-sources.md`: mapa de fontes oficiais e regras de evidência.
- `references/package-map.md`: índice funcional para descoberta de pacotes.
- `scripts/query_uipath_feed.py`: consulta o feed NuGet oficial da UiPath.
- `evals/evals.json`: cenários realistas de avaliação.
- `skills.sh.json`: configuração da página do repositório no skills.sh.

## Requisitos

- Um agente de programação com IA compatível com Agent Skills.
- Acesso à internet para consultar documentação e metadados atuais.
- Node.js com `npx` para a instalação interativa.
- Python 3 para o script opcional de consulta ao feed NuGet.
- Git somente para instalação manual.

O script Python utiliza apenas a biblioteca padrão e não exige pacotes adicionais.

## Instalação com o skills CLI

### Instalação interativa

```bash
npx skills add IgorSebastiann/Uipath-Skills
```

O CLI:

1. descobre `uipath-skills` no repositório;
2. detecta os agentes compatíveis instalados na máquina;
3. permite selecionar o escopo de projeto ou global;
4. permite selecionar instalação por link simbólico ou cópia;
5. instala a skill nos diretórios corretos dos agentes.

### Listar sem instalar

```bash
npx skills add IgorSebastiann/Uipath-Skills --list
```

### Instalar globalmente

```bash
npx skills add IgorSebastiann/Uipath-Skills --skill uipath-skills --global
```

### Instalar no Codex

```bash
npx skills add IgorSebastiann/Uipath-Skills --skill uipath-skills --agent codex
```

### Instalar no Claude Code

```bash
npx skills add IgorSebastiann/Uipath-Skills --skill uipath-skills --agent claude-code
```

### Instalar em vários agentes

```bash
npx skills add IgorSebastiann/Uipath-Skills \
  --skill uipath-skills \
  --agent codex \
  --agent claude-code \
  --agent cursor
```

### Instalar sem interação

Útil para scripts de configuração e ambientes de CI:

```bash
npx skills add IgorSebastiann/Uipath-Skills \
  --skill uipath-skills \
  --global \
  --agent codex \
  --yes
```

### Usar sem instalar

Gere temporariamente o prompt da skill:

```bash
npx skills use IgorSebastiann/Uipath-Skills --skill uipath-skills
```

### Gerenciar a instalação

```bash
# Listar skills instaladas
npx skills list

# Atualizar esta skill
npx skills update uipath-skills

# Remover esta skill
npx skills remove uipath-skills
```

## Instalação manual

### Codex — global

#### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
git clone https://github.com/IgorSebastiann/Uipath-Skills.git "$HOME\.codex\skills\uipath-skills"
```

#### Linux ou macOS

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/IgorSebastiann/Uipath-Skills.git ~/.codex/skills/uipath-skills
```

### Codex — escopo do projeto

Na raiz do projeto:

```bash
mkdir -p .agents/skills
git clone https://github.com/IgorSebastiann/Uipath-Skills.git .agents/skills/uipath-skills
```

### Claude Code — global

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/IgorSebastiann/Uipath-Skills.git ~/.claude/skills/uipath-skills
```

Reinicie o agente caso a skill recém-instalada não seja detectada imediatamente.

## Como usar

Skills podem ser ativadas explicitamente ou automaticamente.

### Acionamento explícito

No Codex CLI ou na extensão de IDE, mencione a skill com `$`:

```text
$uipath-skills

Uso o UiPath Studio 2024.10 LTS em um projeto Windows.
Preciso ler uma planilha Excel, filtrar registros pendentes e salvar o
resultado em outra aba. Recomende os pacotes e atividades oficiais.
```

Também é possível executar `/skills` e selecionar `uipath-skills`.

No ChatGPT ou em outra interface compatível com menções de skills, selecione a skill usando o seletor da interface.

### Acionamento automático

O agente pode selecionar automaticamente a skill quando uma solicitação mencionar:

- UiPath Studio ou StudioX;
- atividades UiPath;
- pacotes `UiPath.*`;
- versões LTS;
- Windows, Windows-Legacy ou Cross-platform;
- migrações de pacotes;
- `project.json`;
- workflows XAML;
- compatibilidade ou dependências UiPath.

Exemplo:

```text
Tenho um projeto Windows-Legacy no Studio 2023.10.
Posso atualizar UiPath.IntelligentOCR.Activities para a versão mais nova?
Analise a compatibilidade e proponha uma migração segura.
```

## Exemplos de prompts

### Escolher atividades

```text
$uipath-skills

Quais atividades oficiais devo usar para ler emails com anexos, salvar somente
arquivos PDF e registrar os resultados em uma fila do Orchestrator?
Meu projeto é Windows e usa o Studio 2025.10 LTS.
```

### Comparar versões

```text
$uipath-skills

Compare as versões suportadas de UiPath.Excel.Activities para o Studio
2024.10 LTS. Mostre compatibilidade, mudanças importantes e riscos de atualização.
```

### Analisar um projeto

```text
$uipath-skills

Analise o project.json e os arquivos XAML deste projeto. Identifique pacotes
fora de suporte, problemas de compatibilidade e atividades que devem ser modernizadas.
```

Forneça os arquivos do projeto para que a skill possa analisar as dependências reais.

### Desenhar um workflow

```text
$uipath-skills

Desenhe um workflow Cross-platform que monitore novos arquivos no Google Drive,
evite duplicidades e crie Queue Items no Orchestrator. Inclua pacotes,
atividades, argumentos, autenticação e tratamento de falhas.
```

## Informações que melhoram as recomendações

Sempre que possível, forneça:

1. versões do UiPath Studio e Robot;
2. linha LTS utilizada;
3. tipo de compatibilidade do projeto;
4. perfil Studio ou StudioX;
5. pacotes atualmente instalados;
6. objetivo da automação;
7. restrições de ambiente, autenticação ou governança;
8. arquivos `project.json`, XAML ou logs relevantes.

Se alguns detalhes não estiverem disponíveis, a skill poderá trabalhar com suposições, indicando claramente quais delas afetam a recomendação.

## Consultar manualmente o feed oficial

O script incluído consulta pacotes e versões publicados no feed NuGet oficial da UiPath.

### Pesquisar pacotes

```bash
python scripts/query_uipath_feed.py search "Excel"
```

### Listar versões

```bash
python scripts/query_uipath_feed.py versions UiPath.Excel.Activities
```

Incluir versões prerelease:

```bash
python scripts/query_uipath_feed.py versions UiPath.Excel.Activities --prerelease
```

### Consultar um pacote

```bash
python scripts/query_uipath_feed.py package UiPath.Excel.Activities
```

Incluir os metadados completos dos grupos de dependências:

```bash
python scripts/query_uipath_feed.py package UiPath.Excel.Activities --full
```

O feed comprova que uma versão do pacote foi publicada. Ele não comprova sozinho que a versão é atualmente suportada ou alinhada a uma versão LTS.

## Prioridade das fontes

A skill prioriza:

1. documentação oficial da atividade;
2. páginas oficiais de compatibilidade do pacote;
3. release notes do pacote;
4. UiPath Activities Lifecycle;
5. UiPath Activities Overview;
6. feed NuGet oficial da UiPath.

Consulte [references/official-sources.md](references/official-sources.md) para ver o mapa completo de fontes e as regras de evidência.

## Limitações

- O catálogo UiPath muda continuamente; por isso, as versões não ficam congeladas no `SKILL.md`.
- Atividades do Integration Service podem seguir um modelo de atualização e distribuição diferente dos pacotes clássicos.
- Atividades individuais podem ter compatibilidade mais restrita que o pacote no qual estão incluídas.
- XAML gerado sem os arquivos e dependências do projeto deve ser tratado como rascunho.
- A skill não publica processos nem modifica o Orchestrator sem autorização explícita.

## Desenvolvimento e validação

Valide o script Python:

```bash
python -m py_compile scripts/query_uipath_feed.py
```

Execute uma consulta real ao feed:

```bash
python scripts/query_uipath_feed.py package UiPath.Excel.Activities
```

Os cenários de avaliação estão disponíveis em [evals/evals.json](evals/evals.json).

## Contribuindo

Contribuições são bem-vindas, especialmente para:

- ampliar o mapa funcional de pacotes;
- adicionar cenários de avaliação;
- melhorar as orientações de compatibilidade;
- corrigir links oficiais alterados;
- aprimorar o script de consulta ao feed.

Ao contribuir:

1. limite as recomendações a pacotes oficiais da UiPath;
2. use documentação oficial como evidência;
3. não identifique uma versão como atual sem data e evidência;
4. valide o script;
5. adicione ou atualize avaliações quando o comportamento mudar.

## Licença

Este projeto é distribuído sob os termos descritos em [LICENSE](LICENSE).
