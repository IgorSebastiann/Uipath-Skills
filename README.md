# UiPath Skills

Skill reutilizável para ChatGPT e Codex que pesquisa, compara e recomenda pacotes e atividades oficiais do UiPath.

Ela ajuda desenvolvedores de automações a escolher atividades, avaliar versões suportadas e LTS, verificar compatibilidade e desenhar workflows sem depender de um catálogo estático que rapidamente ficaria desatualizado.

## O que a skill faz

- Pesquisa somente pacotes oficiais publicados pela UiPath.
- Consulta versões estáveis disponíveis no feed NuGet oficial.
- Prioriza versões atualmente suportadas e relacionadas às linhas LTS.
- Verifica compatibilidade com:
  - UiPath Studio e StudioX;
  - Windows;
  - Windows - Legacy;
  - Cross-platform.
- Compara atividades Modern e Classic.
- Analisa dependências, requisitos e riscos de atualização.
- Ajuda a selecionar atividades para um caso de uso.
- Propõe a estrutura de workflows UiPath.
- Analisa arquivos `project.json` e XAML fornecidos pelo usuário.
- Orienta migrações de projetos e pacotes legados.
- Consulta documentação, release notes e lifecycle oficiais antes de fazer afirmações sobre versões.

## Escopo

A skill cobre exclusivamente pacotes oficiais da UiPath.

Pacotes de parceiros, Marketplace e comunidade não fazem parte do catálogo recomendado. A skill também não considera uma versão suportada apenas porque ela existe no feed: o status de suporte precisa ser confirmado no Activities Lifecycle ou nas release notes oficiais.

## Estrutura

```text
Uipath-Skills/
├── SKILL.md
├── README.md
├── LICENSE
├── references/
│   ├── official-sources.md
│   └── package-map.md
├── scripts/
│   └── query_uipath_feed.py
└── evals/
    └── evals.json
```

- `SKILL.md`: instruções principais carregadas pelo agente.
- `references/official-sources.md`: mapa de fontes oficiais e regras de evidência.
- `references/package-map.md`: índice funcional para descoberta de pacotes.
- `scripts/query_uipath_feed.py`: consulta o feed NuGet oficial usando Python.
- `evals/evals.json`: cenários usados para validar o comportamento da skill.

## Requisitos

- ChatGPT com suporte a Skills ou uma instalação atual do Codex.
- Acesso à internet para consultar documentação e versões atuais.
- Python 3 para usar o script opcional de consulta ao feed.
- Git, caso a instalação seja feita por clonagem.

O script utiliza apenas a biblioteca padrão do Python e não exige instalação de pacotes adicionais.

## Instalação no Codex

O padrão atual do Codex utiliza:

- `~/.agents/skills` para skills disponíveis ao usuário em qualquer projeto;
- `.agents/skills` dentro de um repositório para skills compartilhadas somente naquele projeto.

### Opção 1 — Skill Installer

No Codex, solicite:

```text
$skill-installer Instale a skill do repositório https://github.com/IgorSebastiann/Uipath-Skills.git
```

Se a skill não aparecer imediatamente após a instalação, reinicie o Codex.

### Opção 2 — Instalação global com Git

Esta opção deixa a skill disponível em todos os projetos do usuário.

#### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
git clone https://github.com/IgorSebastiann/Uipath-Skills.git "$HOME\.agents\skills\uipath-skills"
```

#### Linux ou macOS

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/IgorSebastiann/Uipath-Skills.git ~/.agents/skills/uipath-skills
```

### Opção 3 — Instalação em um único projeto

Execute dentro da raiz do projeto no qual a skill deve ficar disponível:

```bash
mkdir -p .agents/skills
git clone https://github.com/IgorSebastiann/Uipath-Skills.git .agents/skills/uipath-skills
```

No Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force ".agents\skills" | Out-Null
git clone https://github.com/IgorSebastiann/Uipath-Skills.git ".agents\skills\uipath-skills"
```

Essa opção permite versionar a skill junto às convenções do projeto.

## Atualização

Se a instalação foi feita por Git:

```bash
cd ~/.agents/skills/uipath-skills
git pull
```

No Windows PowerShell:

```powershell
Set-Location "$HOME\.agents\skills\uipath-skills"
git pull
```

## Como usar

Skills podem ser acionadas explícita ou automaticamente.

### Acionamento explícito

No Codex CLI ou na extensão de IDE, mencione a skill com `$`:

```text
$uipath-skills

Uso o UiPath Studio 2024.10 LTS em um projeto Windows.
Preciso ler uma planilha Excel, filtrar registros pendentes e salvar o
resultado em outra aba. Recomende os pacotes e atividades oficiais.
```

Também é possível abrir o seletor com `/skills` e escolher `uipath-skills`.

No ChatGPT com suporte a Skills, use `@` para selecionar a skill.

### Acionamento automático

O agente pode selecionar a skill automaticamente quando a solicitação mencionar temas como:

- UiPath Studio ou StudioX;
- atividades UiPath;
- pacotes `UiPath.*`;
- versões LTS;
- Windows, Windows-Legacy ou Cross-platform;
- migração de pacotes;
- `project.json`;
- workflows XAML;
- compatibilidade ou dependências UiPath.

Exemplo:

```text
Tenho um projeto Windows-Legacy no Studio 2023.10.
Posso atualizar UiPath.IntelligentOCR.Activities para a versão mais nova?
Analise a compatibilidade e proponha uma migração segura.
```

## Exemplos de solicitações

### Escolher atividades

```text
$uipath-skills

Qual atividade oficial devo usar para ler emails com anexos, salvar apenas
arquivos PDF e registrar os resultados em uma fila do Orchestrator?
Meu projeto é Windows e uso Studio 2025.10 LTS.
```

### Comparar versões

```text
$uipath-skills

Compare as versões suportadas de UiPath.Excel.Activities para Studio
2024.10 LTS. Mostre compatibilidade, mudanças importantes e riscos de upgrade.
```

### Analisar um projeto

```text
$uipath-skills

Analise o project.json e os XAML deste projeto. Identifique pacotes fora de
suporte, incompatibilidades e atividades que precisam ser modernizadas.
```

Anexe ou disponibilize os arquivos do projeto para que a skill possa analisar as dependências reais.

### Desenhar um workflow

```text
$uipath-skills

Monte o desenho de um workflow Cross-platform que monitore novos arquivos no
Google Drive, valide duplicidade e crie Queue Items no Orchestrator.
Informe pacotes, atividades, argumentos, autenticação e tratamento de falhas.
```

## Informações que melhoram a resposta

Sempre que possível, informe:

1. versão do UiPath Studio e Robot;
2. linha LTS utilizada;
3. tipo de projeto;
4. perfil Studio ou StudioX;
5. pacotes já instalados;
6. objetivo da automação;
7. restrições de ambiente, autenticação ou governança;
8. arquivos `project.json`, XAML ou logs relevantes.

Se esses dados não forem fornecidos, a skill pode trabalhar com suposições, mas indicará quais delas afetam a recomendação.

## Consulta manual ao feed oficial

O script incluído permite verificar pacotes e versões publicadas no feed NuGet oficial.

### Pesquisar pacotes

```bash
python scripts/query_uipath_feed.py search "Excel"
```

### Listar versões

```bash
python scripts/query_uipath_feed.py versions UiPath.Excel.Activities
```

Incluindo versões preview:

```bash
python scripts/query_uipath_feed.py versions UiPath.Excel.Activities --prerelease
```

### Consultar um pacote

```bash
python scripts/query_uipath_feed.py package UiPath.Excel.Activities
```

Para incluir os metadados completos dos grupos de dependências:

```bash
python scripts/query_uipath_feed.py package UiPath.Excel.Activities --full
```

O feed confirma que uma versão foi publicada. Para afirmar que ela está suportada ou ligada a uma LTS, consulte também o Activities Lifecycle e as release notes oficiais.

## Fontes utilizadas

A skill prioriza:

1. documentação oficial da atividade;
2. página oficial de compatibilidade do pacote;
3. release notes;
4. Activities Lifecycle;
5. Activities Overview;
6. feed NuGet oficial da UiPath.

Consulte [references/official-sources.md](references/official-sources.md) para os links e critérios completos.

## Limitações

- O catálogo UiPath muda continuamente; por isso, versões não ficam congeladas no `SKILL.md`.
- Algumas atividades do Integration Service são atualizadas e distribuídas de maneira diferente dos pacotes clássicos.
- Uma atividade pode ter compatibilidade mais restrita que o pacote no qual está incluída.
- A geração de XAML sem os arquivos e dependências do projeto deve ser tratada como rascunho.
- A skill não publica processos nem executa alterações no Orchestrator sem autorização explícita.

## Desenvolvimento e validação

Para verificar a sintaxe do script:

```bash
python -m py_compile scripts/query_uipath_feed.py
```

Para testar uma consulta real:

```bash
python scripts/query_uipath_feed.py package UiPath.Excel.Activities
```

Os cenários de validação ficam em [evals/evals.json](evals/evals.json).

## Contribuindo

Contribuições são bem-vindas, especialmente para:

- ampliar o mapa funcional de pacotes;
- adicionar casos de teste;
- melhorar instruções de compatibilidade;
- corrigir links oficiais alterados;
- aprimorar o script de consulta ao feed.

Ao contribuir:

1. mantenha o escopo limitado a pacotes oficiais;
2. use documentação oficial como fonte;
3. não fixe uma versão como “atual” sem data e evidência;
4. valide o script;
5. adicione ou atualize casos de teste quando alterar comportamento.

## Licença

Este projeto é distribuído sob os termos da licença presente em [LICENSE](LICENSE).

