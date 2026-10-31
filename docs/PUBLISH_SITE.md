# Como colocar a página oficial do AURA Glass TV no ar (GitHub Pages)

A vitrine pública já está preparada em `docs/index.html`, no branch `main` do repositório público `eusam66/AURA-Update`.

## Ativação única pelo proprietário

1. Abra https://github.com/eusam66/AURA-Update/settings/pages
2. Na seção **Build and deployment → Source**, selecione **Deploy from a branch**.
3. Em **Branch**, escolha **main**.
4. Em **Folder**, escolha **/docs**.
5. Clique em **Save**.
6. Aguarde o workflow do GitHub Pages executar e confira o endereço apresentado em **Settings → Pages → Visit site**.

**Endereço padrão esperado (só funcionará após ativação e publicação):**

`https://eusam66.github.io/AURA-Update/`

A página `docs/index.html` usa estilos CSS e JavaScript próprios, **sem plataforma externa, API paga nem serviços de hospedagem adicionais**. GitHub Pages é oferecido no GitHub Free para repositórios públicos.

**Documentação oficial:** https://docs.github.com/pt/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## O que está pronto

- Cabeçalho AURA Glass TV, identidade grafite/dourado-champanhe.
- Descrição de divulgação voltada ao usuário.
- Botão principal para APK público verificado.
- Recursos: filmes, séries, TV ao vivo, favoritos, perfis, EPG e atualização integrada.
- Prévia de player e cartão Próximo episódio com **capturas ilustrativas de teste** (não prometem conteúdo incorporado).
- Requisitos mínimos Android TV/Google TV Android 9+.
- Instalação com confirmação do Android.
- Aviso explícito de que o aplicativo não inclui conteúdo ou listas.
- Links para GitHub Releases e suporte público.

## Atualização automática do link no site

A página lê o manifesto público estável:

`https://raw.githubusercontent.com/eusam66/AURA-Update/main/updates/android/stable.json`

Ao detectar `latest.version_code` válido, URLs oficiais do repositório e pacote esperado, atualiza:

- botão de download,
- versão informada,
- notas da versão,
- SHA-256.

**Este mecanismo atualiza só o conteúdo da página**. Não altera APK, manifesto, assinatura ou o processo de publicação: o workflow de Release autorizado continua sendo o único responsável por disponibilizar novas versões.

O fallback estático da página é a vc31; se o feed estiver temporariamente indisponível, o botão permanece direcionado ao APK público validado da vc31.

## Divulgação

**Link do GitHub — funciona imediatamente:** https://github.com/eusam66/AURA-Update

**Link do site — só divulgar após o GitHub Pages mostrar site publicado:** https://eusam66.github.io/AURA-Update/

**Link para APK vc31:** https://github.com/eusam66/AURA-Update/releases/download/android-stable-vc31/AURA-Glass-TV-stable-vc31.apk

## Atenções

- Não publicar o código do repositório privado `eusam66/AURA-TV-Player`.
- Não subir credenciais Xtream, listas de usuários, chaves de assinatura, logs com dados privados ou vídeos protegidos.
- Não afirmar que o aplicativo inclui canais, filmes, assinaturas ou catálogos.
- Usar apenas capturas próprias com direitos adequados ou demos sintéticas rotuladas.
- Quando licenciamento/pagamento de futuros produtos estiverem aprovados, atualizar a apresentação antes de anunciar condições comerciais.
- `lite.json` permanece inativo até release própria, sem cruzar edições.
