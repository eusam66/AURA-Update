# AURA Update — Distribuição oficial de APKs

Este repositório **público e separado** contém a infraestrutura de atualizações do **AURA Glass TV** para Android TV / Google TV. Ele **não contém o código-fonte privado do aplicativo**, credenciais, listas IPTV ou chaves de assinatura.

## Situação

**Ambiente preparado, distribuição ainda desativada.** Até haver um APK aprovado e uma autorização de publicação, os dois canais usam `status: "unreleased"` e `latest: null`; **nenhum APK Premium ou Lite foi publicado aqui**.

| Canal | Feed HTTPS público | Estado |
|---|---|---|
| Glass TV (visual Premium / canal estável) | [stable.json](https://raw.githubusercontent.com/eusam66/AURA-Update/main/updates/android/stable.json) | Inativo |
| Glass Lite TV | [lite.json](https://raw.githubusercontent.com/eusam66/AURA-Update/main/updates/android/lite.json) | Inativo |

> **Premium aqui identifica a edição visual**, não significa que o licenciamento comercial Free/Premium já foi implementado. As edições compartilham o mesmo pacote Android, portanto não são aplicativos instaláveis lado a lado.

## Preparado para a próxima versão

- `updates/android/`: manifesto da última versão aprovada de cada canal.
- `scripts/validate_manifest.py`: verificador do formato e da política de URLs.
- `scripts/publish_manifest.py`: atualiza o feed depois de uma Release aprovada.
- `tests/`: testes automatizados de integridade dos manifestos.
- `.github/workflows/validate-updates.yml`: verifica os feeds a cada push e PR.
- `.github/workflows/publish-android.yml`: publicação **manual** de um APK preexistente do CI privado, condicionado a assinatura/código/pacote/hash corretos. O workflow não compila nem assina APKs.

A publicação requer uma autorização específica e um segredo de leitura mínima `AURA_SOURCE_READ_TOKEN` no **repositório público de distribuição**, com acesso somente às Actions do repositório privado de origem. **Nunca compartilhe o token nem o coloque no APK**. Consulte [Processo de publicação](docs/RELEASING.md).

### Links para integração no aplicativo
- Estável: `https://raw.githubusercontent.com/eusam66/AURA-Update/main/updates/android/stable.json`
- Lite: `https://raw.githubusercontent.com/eusam66/AURA-Update/main/updates/android/lite.json`

Documentação do [protocolo do atualizador](docs/UPDATE_PROTOCOL.md) e [instalação manual](docs/INSTALL_ANDROID.md).

O aplicativo atual ainda não implementou o AURA Update. A instalação do APK continuará usando o instalador nativo do Android, sempre com permissão/consentimento do usuário.

**Sem serviços pagos ou migração do código-fonte para um repositório público.**
