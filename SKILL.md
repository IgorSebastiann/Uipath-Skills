---
name: uipath-skills
description: Pesquisa, compara e recomenda pacotes e atividades oficiais do UiPath, suas versões suportadas/LTS, compatibilidade com Studio e tipos de projeto, funcionalidades, dependências, mudanças de versão e uso em workflows. Use esta skill sempre que o usuário mencionar UiPath, Studio, StudioX, atividades, pacotes NuGet UiPath.*, Windows/Windows-Legacy/Cross-platform, versões LTS, migração, project.json, XAML ou pedir ajuda para escolher, instalar, atualizar ou usar uma atividade oficial do UiPath.
compatibility: Requer acesso à documentação oficial do UiPath; o script opcional de consulta ao feed usa Python 3 e acesso à internet.
---

# UiPath Skills

Ajude a desenvolver automações UiPath com informações verificáveis sobre pacotes e atividades oficiais. Responda no idioma do usuário.

## Princípios

- Trate versões, suporte, compatibilidade e catálogo como dados mutáveis. Verifique-os em fonte oficial no momento da resposta.
- Considere apenas pacotes publicados oficialmente pela UiPath. Exclua Marketplace, parceiros e comunidade, salvo para explicar que estão fora do escopo.
- Priorize versões atualmente suportadas, versões ligadas às linhas LTS e a versão estável mais recente compatível.
- Não presuma que “mais recente” significa “compatível”. Considere versão do Studio/Robot, tipo de projeto e dependências.
- Não invente nomes de atividades, propriedades, argumentos, namespaces, versões ou recursos. Quando a fonte não confirmar um detalhe, declare a incerteza.
- Diferencie pacote, atividade, conector do Integration Service, produto e recurso de plataforma.

## Fluxo de trabalho

### 1. Entender o ambiente

Extraia da solicitação ou dos arquivos disponíveis:

- versão do UiPath Studio e Robot;
- perfil Studio ou StudioX;
- tipo de projeto: Windows, Windows - Legacy ou Cross-platform;
- linha do produto: Automation Cloud, 2025.10 LTS, 2024.10 LTS, 2023.10 LTS ou outra;
- linguagem do projeto, quando relevante;
- pacotes e versões já instalados;
- objetivo funcional e restrições.

Se o usuário fornecer `project.json`, leia primeiro `projectVersion`, `targetFramework`, `runtimeOptions` e `dependencies`. Se fornecer XAML, examine namespaces, assemblies, atividades e argumentos antes de recomendar alterações.

Quando faltar informação que muda materialmente a recomendação, apresente a suposição adotada e peça somente o dado indispensável. Para uma consulta genérica, responda sem bloquear.

### 2. Selecionar a fonte oficial

Leia [references/official-sources.md](references/official-sources.md) antes de pesquisar versões ou compatibilidade.

Use, nesta ordem:

1. página oficial da atividade, para propriedades, argumentos, limitações e exemplos;
2. página de compatibilidade do pacote, para tipos de projeto;
3. release notes do pacote, para versões e mudanças;
4. Activities Lifecycle, para suporte e associação com linhas LTS;
5. Activities Overview, para catálogo e categorias;
6. feed oficial NuGet, para existência do pacote e versões publicadas.

Uma versão presente no feed não é automaticamente uma versão suportada. Confirme suporte no lifecycle ou release notes.

### 3. Consultar o catálogo

Para descobrir ou validar pacotes e versões no feed oficial, use:

```powershell
python scripts/query_uipath_feed.py search "Excel"
python scripts/query_uipath_feed.py versions UiPath.Excel.Activities
python scripts/query_uipath_feed.py package UiPath.Excel.Activities
```

O script consulta metadados; depois confirme suporte, compatibilidade e funcionalidade na documentação.

Para navegação por domínio e nomes comuns de pacotes, leia [references/package-map.md](references/package-map.md). Esse mapa é um índice, não uma fotografia completa de versões.

### 4. Avaliar compatibilidade

Verifique separadamente:

- compatibilidade do pacote com Windows, Windows - Legacy e Cross-platform;
- versão mínima ou recomendada do Studio;
- disponibilidade específica da atividade dentro do pacote;
- dependências transitivas e conflitos conhecidos;
- status estável, preview, suportado ou fora de suporte;
- diferenças entre atividades Modern e Classic;
- exigências de Integration Service, conexão, autenticação ou serviço externo.

Desde Studio 2023.10, muitas atividades do Integration Service são entregues pela dependência unificada `UiPath.IntegrationService.Activities`. Não recomende um pacote individual antigo sem conferir a versão do Studio e a documentação atual.

Evite downgrade como primeira solução. Caso seja necessário, explique risco de inconsistência entre dependências e indique validação em ambiente separado.

### 5. Recomendar uma solução

Compare opções pelo resultado desejado, compatibilidade, suporte, manutenção e complexidade. Dê preferência a atividades modernas e suportadas, mas reconheça projetos legados existentes.

Ao propor um workflow:

1. liste pacote e faixa de versão indicada;
2. descreva as atividades na ordem de execução;
3. mostre entradas, saídas e tipos importantes;
4. inclua tratamento de erros, timeout, retry e logging quando aplicável;
5. destaque credenciais, permissões e dados sensíveis;
6. indique como validar no Studio.

Só gere ou edite XAML quando houver contexto suficiente do projeto. Preserve namespaces, versões de dependência, argumentos e estrutura existente. Se não puder validar o XAML no Studio, entregue-o como rascunho explicitamente identificado.

## Formatos de resposta

### Consulta de pacote ou atividade

Use uma tabela compacta:

| Campo | Informação |
|---|---|
| Pacote | ID oficial |
| Atividade | Nome exibido |
| Finalidade | O que faz |
| Versão indicada | Versão/faixa e motivo |
| Compatibilidade | Studio e tipo de projeto |
| Dependências | Requisitos relevantes |
| Observações | Modern/Classic, limitações e mudanças |

Inclua links oficiais junto das afirmações e informe a data da consulta.

### Comparação

Compare pacote/atividade, cenário ideal, compatibilidade, vantagens, limitações e recomendação final. Não compare apenas pelo número da versão.

### Diagnóstico de projeto

Organize em:

1. diagnóstico;
2. evidências encontradas em `project.json`/XAML/log;
3. correção recomendada;
4. riscos de versão ou migração;
5. passos de validação.

## Limites

- Não trate listagens de blogs, fóruns, Stack Overflow ou respostas de IA como prova de versão ou suporte.
- Use fontes secundárias apenas para pistas, nunca para substituir a documentação oficial.
- Não alegue cobertura integral do catálogo se a consulta foi parcial.
- Não exponha tokens, credenciais, connection strings ou valores de assets.
- Não publique nem execute automações no Orchestrator sem autorização explícita.

