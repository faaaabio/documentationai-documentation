# QA

Casos de teste organizados por funcionalidade.

## Booking Público

| # | Cenário | Resultado esperado |
|---|---------|-------------------|
| 1 | Acessar link de agendamento válido | Exibe perfil do profissional e serviços disponíveis |
| 2 | Acessar link de agendamento inválido | Exibe página de erro adequada |
| 3 | Selecionar serviço e data | Exibe apenas horários disponíveis |
| 4 | Tentar agendar horário já ocupado | Horário não aparece na lista |
| 5 | Preencher nome e telefone e confirmar | Agendamento criado, cliente recebe WhatsApp |
| 6 | Submeter sem preencher campos obrigatórios | Exibe validação nos campos |
| 7 | Agendar fora do horário de funcionamento | Horário não aparece na lista |

## Acessibilidade e Interface

| # | Critério | Como verificar | Resultado esperado |
|---|----------|----------------|--------------------|
| 1 | Tamanho mínimo de fonte | Inspecionar todos os elementos de texto | Nenhum texto abaixo de 14px |
| 2 | Uso de bold | Revisar textos em negrito na interface | Bold apenas em títulos e informações de alta relevância |
| 3 | Tamanho de títulos | Comparar títulos com o corpo do texto | Títulos proporcionais, sem destaque excessivo |
| 4 | Contraste branco sobre verde | Inspecionar elementos com texto branco em fundo verde | Contraste mínimo 4.5:1 (WCAG AA) — evitar a combinação quando possível |

## Notificações WhatsApp

| # | Cenário | Resultado esperado |
|---|---------|-------------------|
| 1 | Agendamento confirmado | Cliente recebe mensagem imediatamente |
| 2 | 24h antes do horário | Cliente recebe lembrete automático |
| 3 | Agendamento cancelado | Cliente recebe notificação de cancelamento |
