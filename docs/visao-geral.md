# Visão Geral — Zavvy

> Site: https://zavvy.com.br
> App: https://app.zavvy.com.br
> Data da captura: 2026-03-11

**Zavvy** é uma plataforma de agenda inteligente com confirmação automática pelo WhatsApp, voltada para profissionais autônomos que trabalham com agendamentos.

**Tagline:** _"Seus clientes nunca mais vão faltar."_

**Proposta de valor central:** O cliente recebe mensagem de confirmação no momento do agendamento e 24h antes do horário. Ele confirma ou remarca direto no WhatsApp — e a agenda do profissional atualiza sozinha.

---

## Identidade Visual

| Elemento | Detalhe |
|----------|---------|
| Logo | "zavvy" (minúsculas, tipografia verde) |
| Cor primária | Verde (#1DB954 aproximado) |
| Fundo | Off-white claro |
| Tipografia | Sans-serif moderna, bold nos headlines |
| Estilo | Minimalista, clean, voltado para conversão |

---

## Notas Técnicas

- Site construído como **landing page de uma única página** (`/`) com seções acessadas via âncoras
- App separado em subdomínio: `app.zavvy.com.br`
- Mensagens WhatsApp via API (cobradas por mensagem enviada)
- Integração com Google Calendar e Google Meet
- Conformidade com LGPD mencionada explicitamente
- PWA (Progressive Web App) para acesso mobile

---

## Estrutura de Páginas

| Página | URL | Screenshot |
|--------|-----|------------|
| Home | `https://zavvy.com.br/` | `screenshots/home/` |
| Termos de Uso | `https://zavvy.com.br/termos-de-uso` | `screenshots/termos-de-uso/full-page.png` |
| Política de Privacidade | `https://zavvy.com.br/politica-de-privacidade` | `screenshots/politica-de-privacidade/full-page.png` |
| Login (app externo) | `https://app.zavvy.com.br/login` | — |
| Cadastro (app externo) | `https://app.zavvy.com.br/signup` | — |
