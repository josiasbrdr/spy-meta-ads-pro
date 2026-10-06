# Escola de Servas — Landing (v5 jornadas)

Site estático pronto para o Cloudflare Pages. Esta pasta é a raiz de publicação: não há build, basta publicar o conteúdo dela.

## Como publicar no Cloudflare Pages

**Opção A: upload direto (mais rápido)**

1. No painel do Cloudflare, vá em **Workers & Pages → Create → Pages → Upload assets**.
2. Dê um nome ao projeto (ex.: `escola-de-servas`).
3. Arraste o conteúdo desta pasta (ou o arquivo `escola-de-servas-landing.zip`) e clique em **Deploy site**.

**Opção B: conectado ao GitHub (atualiza sozinho a cada commit)**

1. **Workers & Pages → Create → Pages → Connect to Git** e escolha este repositório.
2. Em *Build settings*: Framework preset `None`, Build command vazio, **Root directory** `escola-de-servas-landing`, Build output directory `/`.
3. Clique em **Save and Deploy**.

## Antes de divulgar o link

- Em `index.html`, troque `SEU-DOMINIO` (4 ocorrências: canonical, `og:url`, `og:image`, `twitter:image`) pelo domínio final, por exemplo `escoladeservas.com.br` ou `escola-de-servas.pages.dev`. Sem isso o WhatsApp e o Instagram não mostram a prévia com imagem.
- Confira a prévia em https://developers.facebook.com/tools/debug/ depois de publicar.
- Se for usar Meta Pixel ou Google Analytics, adicione o script e libere os domínios deles em `_headers` (`script-src`, `img-src` e `connect-src`), senão a CSP bloqueia.

## O que há aqui

| Caminho | Conteúdo |
|---|---|
| `index.html` | A landing. O markup fica dentro de `<x-dc>` e é montado pelo runtime. |
| `assets/js/` | `dc-runtime.js` (motor da página), React 18.3.1 e ReactDOM, `resources.js` (mapa de recursos locais). |
| `assets/img/` | Logos, lírio decorativo, símbolo oval e fotos das docentes. |
| `assets/fonts/` | Cormorant Garamond e Lato em woff2, servidas localmente. |
| `_headers` | Cabeçalhos de segurança (CSP, HSTS etc.) e cache. O Cloudflare Pages aplica automaticamente. |
| `og-image.jpg` | Imagem 1200×630 para compartilhamento. |
| `favicon.svg`, `favicon.png`, `apple-touch-icon.png` | Ícones. |
| `robots.txt` | Libera indexação. |

## Como editar textos, preços ou links

Edite direto em `index.html`. O link de checkout aparece no atributo `data-props` do `<script type="text/x-dc">` (valor `default` de `checkoutUrl`) e como fallback no método `renderVals()` no fim do mesmo script. Troque nos dois lugares.

## Verificações feitas

- Renderizada em Chromium (desktop 1366px e celular 390px) com os cabeçalhos de `_headers` aplicados: sem erro de JavaScript, sem violação de CSP, fontes carregadas, botões de compra apontando para o checkout, barra fixa no celular, FAQ e vídeos funcionando.
- Nenhuma dependência externa no carregamento além das miniaturas dos vídeos do YouTube.
- Nenhum segredo, chave ou dado de localização nas imagens.
