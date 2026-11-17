# Segurança — AURA Update

- Não publique credenciais Xtream/M3U, contas, backups, dados de clientes, arquivos de vídeo, PINs, keystores ou código do projeto privado.
- APKs públicos devem aparecer somente como assets de **Releases**, após verificação de pacote, versionCode, SHA-256, SDK, flags de debug e certificado do APK original.
- O workflow de publicação privado→público exige o segredo Actions `AURA_SOURCE_READ_TOKEN` com acesso mínimo de leitura. Nunca publicar o valor.
- Não instalar silenciosamente, permitir downgrade, desabilitar TLS ou alterar a assinatura sem uma política de migração verificada.
- Distribuir somente o player, sem canais, listas ou conteúdo de terceiros.

## Certificados distintos — não misturar canais

| Linha de distribuição | Certificado SHA-256 | Atualização |
|---|---|---|
| Stable legado vc36 e Lite vc37 | `f5e7ba845b611c41d3b8354a04c461609b47b9eacfa59f25b16bafcfb144e3b9` | Manter pin original e feeds antigos |
| Beta pública Premium vc47 | `45bbf20773d4da2e5a2bc83d12ca6e3283b04119a1b16e0226a8e71d573b22eb` | Somente novas instalações, Release independente |

Esses certificados foram confirmados em APKs assinados, não são intercambiáveis. A beta vc47 não pode atualizar por cima da Stable vc36 ou Lite vc37 pelo Android Package Manager. **Não alterar o certificado esperado nos manifestos Stable/Lite para tentar forçar a atualização.**

A beta vc47 foi publicada com o APK CI original de SHA-256 `0efdb60981c4f9ceb083b4eb351647eb00fa6cfbec0654217ca77ad4cfd914dd`, sem recompilação ou reassinatura, após verificação byte a byte do arquivo público.

O Smart Skip é experimental e desativado por padrão nas novas instalações; recomendar mantê-lo desligado. Publicar qualquer atualização futura exige verificação do certificado correspondente ao canal e nova decisão do responsável.

- [Release beta vc47](https://github.com/eusam66/AURA-Update/releases/tag/android-beta-vc47)
- [Workflow auditável de publicação vc47](https://github.com/eusam66/AURA-Update/actions/workflows/publish-vc47-beta-once.yml)
