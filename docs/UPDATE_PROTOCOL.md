# AURA Update — Protocolo público de atualização Android TV

**Versão de contrato do manifesto: 1.** Cliente de atualização do AURA Glass TV implementado e homologado na Philips Android TV.

## Canais

- **Premium/Stable (ativo):** https://raw.githubusercontent.com/eusam66/AURA-Update/main/updates/android/stable.json
- **Lite (inativo):** https://raw.githubusercontent.com/eusam66/AURA-Update/main/updates/android/lite.json

Os feeds retornam `schema_version`, `platform`, `channel`, `status` e `latest`. O objeto `latest` possui: versão numérica e amigável, pacote, SDK mínimo, URL HTTPS do APK, SHA-256, tamanho, fingerprint do certificado, notas de versão e data.

**Não reproduzir valores antigos de exemplo como se fossem Releases atuais.** Consulte o manifesto público ativo.

## Fluxo no Android TV

1. Em **Configurações → Atualizações**, permitir consulta manual, configuração de verificação automática e download automático somente quando autorizado e permitido pelo ambiente.
2. Se `status != released`, `latest == null` ou `latest.version_code <= BuildConfig.VERSION_CODE`, não oferecer instalação.
3. Usar o canal da edição instalada; não misturar `stable` e `lite` nem permitir downgrade.
4. Avisar de forma discreta, sem roubar foco de outros menus ou interromper reprodução.
5. Baixar APK HTTPS de fonte aprovada em armazenamento privado, limitando bytes e comparando tamanho e SHA-256.
6. Verificar pacote original, `versionCode`, compatibilidade Android e certificado real do APK usando APIs Android; rejeitar troca não autorizada de certificado.
7. Instalar somente com confirmação do usuário no instalador Android, `FileProvider` e permissões específicas quando necessárias. **Não instalar silenciosamente**.
8. Se houver falha de Internet, espaço, certificado, checksum ou permissão, manter instalação anterior.
9. Não verificar/baixar no meio da reprodução.
10. Não embutir PAT/GitHub token no APK; manifestos e Releases são públicos.

## Identidade da edição Stable

- Pacote: `com.auratv.player.engine3`.
- Certificado SHA-256: `f5e7ba845b611c41d3b8354a04c461609b47b9eacfa59f25b16bafcfb144e3b9`.
- SDK mínimo: 28.

A política de assinatura é de continuidade. Não criar nova chave ou aceitar alteração sem migração aprovada. Não publicar credenciais ou dados pessoais na infraestrutura pública.

## Processo de Release

O código continua privado. CI privada produz o APK, o workflow público verifica o mesmo binário e só ativa o manifesto após Release imutável válida. Após validação integral, a publicação é autorizada permanentemente pelo proprietário. Ver `RELEASING.md`.

**Histórico de homologação:** vc28→vc29, vc29→vc30 e vc30→vc31 instaladas via AURA Update na Philips, com preservação de dados relatada nos testes físicos.
