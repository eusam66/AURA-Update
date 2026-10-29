# Segurança — AURA Update

- Não publique credenciais Xtream/M3U, contas, backups, dados de clientes, arquivos de vídeo, PINs, keystores ou código do projeto privado.
- Arquivos APK só devem aparecer em **Releases**, depois da checagem de pacote `com.auratv.player.engine3`, `versionCode`, SHA-256 e certificado de assinatura original.
- Certificado SHA-256 público autorizado: `f5e7ba845b611c41d3b8354a04c461609b47b9eacfa59f25b16bafcfb144e3b9`.
- O workflow de publicação precisa de um token de leitura de artefatos do repositório privado, configurado como **segredo Actions** `AURA_SOURCE_READ_TOKEN`. Não incluir token nas instruções, no repositório ou no APK.
- O manifest `stable.json` ou `lite.json` é um aviso de versão, **não** uma fonte confiável de código executável. O app deve validar o APK baixado, inclusive o certificado de assinatura fixado e a verificação do próprio Android.
- Nada de atualização silenciosa, desinstalação, downgrade automático, bypass da verificação TLS ou autorização de fontes desconhecidas.
- A publicação de APKs e a ativação de manifestos dependem de decisão explícita do responsável.
- Distribuição de builds deve incluir somente software reprodutor, sem oferecer conteúdos ou listas IPTV de terceiros.
