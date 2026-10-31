# Publicação verificada do AURA Glass TV (Android TV)

## Estado atual

**Premium vc31 publicada** e ativa no canal `stable` (31/10/2026). A edição Lite continua com feed inativo até lançamento aprovado. O repositório público `eusam66/AURA-Update` fornece somente material de distribuição, sem código-fonte privado do aplicativo.

## Autorização permanente

O proprietário autorizou **publicar futuras correções/versões Android após a conclusão do desenvolvimento e aprovação integral dos gates técnicos e de segurança**, sem pedir aprovação individual para cada versão. Esta autorização não permite publicação de build incompleto nem instalação silenciosa nas TVs; mudanças de assinatura/pacote, custos ou migrações destrutivas exigem decisão separada. Política registrada também na Issue #35 do repositório privado.

## Workflow oficial e obrigatório

Repositório público: `eusam66/AURA-Update`.

Acesse **Actions → Publish verified AURA Android APK (manual) → Run workflow** e informe:

- `channel`: `stable` (Premium) ou `lite`, conforme a edição exata;
- `source_run_id`: execução CI privada com resultado `success`;
- `source_artifact_name`: nome exato do artefato APK da execução;
- `expected_sha256`: SHA-256 conferido independentemente no arquivo APK;
- `version_code` e `version_name`: metadados do APK;
- `release_notes`: resumo público sem senhas, tokens, URLs de listas ou dados pessoais.

O workflow exige o segredo mínimo `AURA_SOURCE_READ_TOKEN` com acesso de leitura à Actions privada, via GitHub Secrets. Não expor o valor em commits, issues, documentação, páginas ou logs.

## Gates técnicos obrigatórios

1. Testes Android/back-end/regressões relevantes concluídos.
2. `versionCode` superior ao canal ativo e `versionName` coerente.
3. Package original `com.auratv.player.engine3`, minSdk compatível e **certificado original**.
4. APK real íntegro, SHA-256 idêntico ao esperado, `debuggable=false` e `testOnly=false`.
5. Nenhum segredo, lista privada, chave de assinatura, credencial ou dados de usuário publicados.
6. Uma **nova** Release versionada é criada primeiro; só depois `updates/android/stable.json` ou `lite.json` é atualizado.
7. Em erro parcial, bloquear ativação do feed e investigar; não substituir Release antiga nem forçar downgrade.

O workflow **não recompila nem reassina** o APK; usa o artefato privado já validado.

## Atualização na televisão

O usuário final consulta o AURA Update no próprio aplicativo e autoriza o download e a instalação nativa do Android. Atualizações preservam a instalação e dados. Não exigir PC ou ADB para o fluxo normal.

## Página pública de divulgação

- Repositório e README: https://github.com/eusam66/AURA-Update
- Página estática: `docs/index.html`. Ativar GitHub Pages a partir de `main /docs` (veja `docs/PUBLISH_SITE.md`).
- A página estática consulta o feed público `updates/android/stable.json` no navegador para exibir versão, hash, notas e link do APK sempre atualizados; falhas de rede mantêm o link da vc31 como fallback.
- O README menciona a vc31 e deverá ser atualizado durante próximas releases (ou utilizar o link permanente para Releases).
- Galeria: imagens demonstrativas da interface provenientes dos testes sintéticos, **não dados/capturas de usuários**.

**Não adicionar à página pública um pacote, preço, recursos de licenciamento ou canais que ainda não estejam implementados e aprovados.**
