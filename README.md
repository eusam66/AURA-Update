# AURA Update — Distribuição oficial de APKs

Este repositório **público e separado** contém a infraestrutura de atualizações do **AURA Glass TV** para Android TV / Google TV. Ele **não contém o código-fonte privado do aplicativo**, credenciais, listas IPTV ou chaves de assinatura.

## Situação

**Premium vc29 publicada para homologação autorizada pelo proprietário.** O canal estável oferece `0.9.7-aura-premium`, versionCode 29, com o certificado engine3 original. [Release e APK](https://github.com/eusam66/AURA-Update/releases/tag/android-stable-vc29). O canal Lite permanece desativado (`unreleased`, `latest: null`).

| Canal | Feed HTTPS público | Estado |
|---|---|---|
| Glass TV (visual Premium / canal estável) | [stable.json](https://raw.githubusercontent.com/eusam66/AURA-Update/main/updates/android/stable.json) | Ativo — vc29 |
| Glass Lite TV | [lite.json](https://raw.githubusercontent.com/eusam66/AURA-Update/main/updates/android/lite.json) | Inativo |

> **Premium aqui identifica a edição visual**, não significa que o licenciamento comercial Free/Premium já foi implementado. As edições compartilham o mesmo pacote Android, portanto não são aplicativos instaláveis lado a lado.

## Estrutura de distribuição

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

Na Premium vc28, acesse **Configurações → Atualizações → Verificar atualizações** para encontrar a vc29. O cliente verifica tamanho, SHA-256, pacote, versão e assinatura antes de abrir o instalador nativo do Android, sempre com permissão/consentimento do usuário. Atualize sobre a instalação existente, sem desinstalar nem limpar dados. O fluxo físico na TV ainda depende da homologação do proprietário.

**Sem serviços pagos ou migração do código-fonte para um repositório público.**
