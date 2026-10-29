# AURA Update — Protocolo público de atualização (Android)

**Versão de contrato: 1.** O aplicativo Android receberá a implementação do cliente em uma próxima versão. O repositório de distribuição já está pronto para publicação manual, mas ambos os feeds começam desativados.

## Manifestos

- Estável (visual Premium aprovado): `https://raw.githubusercontent.com/eusam66/AURA-Update/main/updates/android/stable.json`.
- Lite: `https://raw.githubusercontent.com/eusam66/AURA-Update/main/updates/android/lite.json`.

Exemplo futuro após uma Release autorizada (não é a situação atual):

```json
{
  "schema_version": 1,
  "platform": "android-tv",
  "channel": "stable",
  "status": "released",
  "latest": {
    "version_code": 27,
    "version_name": "0.9.5-aura-premium",
    "package_name": "com.auratv.player.engine3",
    "min_sdk": 28,
    "apk_url": "https://github.com/eusam66/AURA-Update/releases/download/android-stable-vc27/AURA-Glass-TV-stable-vc27.apk",
    "apk_sha256": "<SHA-256 real do arquivo verificado>",
    "apk_size_bytes": 42000000,
    "signing_cert_sha256": "f5e7ba845b611c41d3b8354a04c461609b47b9eacfa59f25b16bafcfb144e3b9",
    "notes": "Exemplo de novidades.",
    "published_at": "2026-10-29T18:00:00Z"
  }
}
```

O exemplo é documental, não é um manifesto ativo. `min_sdk`, nome do pacote, certificados e versão devem ser conferidos no APK real.

## Comportamento obrigatório do cliente Android

1. Configurações → Atualizações: opções verificação automática no máximo a cada 24h (somente Home/ocioso), baixar automaticamente **somente quando autorizado**, ou somente manual. Botão **Verificar agora**.
2. Se `status != "released"`, `latest == null` ou `latest.version_code <= BuildConfig.VERSION_CODE`, não oferecer instalação.
3. O cliente deve usar o canal correspondente à edição instalada. Lite vc25 e Premium vc26/vc27 compartilham applicationId, portanto **não** oferecer downgrade da Lite sobre Premium.
4. Exibir banner discreto sem roubar o foco nem interromper reprodução. Não repetir o aviso dispensado a toda navegação.
5. Download do APK via HTTPS em armazenamento privado com limite razoável de bytes e comparação de `apk_size_bytes` e SHA-256. Nunca executar arquivos por URL arbitrária nem confiar somente no manifesto.
6. Verificar package `com.auratv.player.engine3`, `versionCode`, SDK e **certificado real** `f5e7ba845b611c41d3b8354a04c461609b47b9eacfa59f25b16bafcfb144e3b9` do APK com PackageManager / APIs do Android; o instalador Android aplica sua própria verificação criptográfica. Não aceitar cert novo/rotacionado sem migração explícita aprovada.
7. Instalação apenas com ação do usuário, instalador oficial, permissões de fonte externa quando aplicável; usar `FileProvider` e URI `content://` ou API de instalação adequada. **Não** desinstalar nem limpar dados.
8. Falha de Internet, armazenamento, permissão ou SHA/certificado mantém a instalação anterior; limpar temporários e permitir tentar novamente.
9. Nunca verificar ou baixar durante playback. Testar APIs 28/30, resolução 720p/1080p e Mi TV Stick 1 GB.
10. Não armazenar GitHub PAT/token no APK: o repositório de distribuição é público, os feeds e assets podem ser acessados sem autenticação.

Observação: o esquema é um contrato inicial para integração. O Codex deve preservar compatibilidade retroativa se evoluir o formato.

## Segurança e políticas

O SHA-256 no manifesto permite verificar a integridade de download; o app deve **fixar o certificado de assinatura aprovado**, e o PackageManager/instalador devem confirmar que o APK pertence à instalação. A instalação é assistida, jamais silenciosa. Não há licenciamento comercial neste repositório.
