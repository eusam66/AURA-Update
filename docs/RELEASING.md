# Publicação controlada de uma atualização

**Estado inicial:** sem Releases Premium/Lite e sem feed ativo. Preparar infraestrutura NÃO equivale a autorizar distribuição de um APK.

## Pré-requisitos antes da primeira publicação
1. Esperar o Codex concluir o APK assinado e a homologação da versão candidata.
2. Obter autorização do proprietário para tornar **aquele APK específico** público.
3. Habilitar GitHub Actions neste repositório de distribuição.
4. Criar o secret Actions `AURA_SOURCE_READ_TOKEN`: token mínimo de leitura do projeto **privado** `eusam66/AURA-TV-Player` com Actions:read (e acesso ao repo), sem permissões de escrita. Não expor no Git, logs ou apps.
5. Garantir Actions configurado para permitir `GITHUB_TOKEN` com permissão de `contents: write` para o workflow manual (o YAML declara essa permissão).
6. Conferir que a versão é *mais nova* do que o manifesto ativo no canal escolhido; mesmo pacote e certificado.

## Workflow manual

Acessar **Actions → Publish verified AURA Android APK (manual) → Run workflow** e informar:
- `channel`: `stable` (Premium visual) ou `lite`;
- `source_run_id`: ID da execução CI concluída com sucesso no repositório privado;
- `source_artifact_name`: nome exato do artefato contendo o APK;
- `expected_sha256`: SHA-256 do APK conferido independentemente;
- `version_code` e `version_name`: valores do APK;
- `release_notes`: novidades em linguagem pública, sem dados privados.

O workflow baixa do CI privado (sem recompilar), confere **SHA-256, pacote, versionCode, versionName e certificado** via `apksigner`/`aapt`, cria **uma nova Release pública** sem sobrescrever existente e **só depois ativa o canal correspondente**. Hash incorreto ou ausência de chave de leitura bloqueia a publicação.

**Importante:** a Release e a alteração do manifesto são duas ações separadas; falha parcial pode deixar Release pública sem atualizar o feed. Não reutilizar/forçar a mesma tag sem revisão: diagnosticar e resolver de forma controlada. A Release não contém código-fonte privado (GitHub anexará automaticamente os arquivos-fonte **deste repositório público de distribuição**, que tem apenas documentação/workflows).

Não habilitar mais de um canal sem identificar a edição correta. O canal Lite não é um método automático de downgrade.

## Para a equipe de desenvolvimento
A implementação do app Android deverá consumir `updates/android/<canal>.json` e usar instalação assistida pelo sistema, nunca silenciosa. O projeto privado permanece inalterado por este repositório, e Cloudflare não é necessário para servir os APKs.
