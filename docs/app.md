# App — app.zavvy.com.br

> Explorado em sessão autenticada em 2026-03-11
> Screenshots: `screenshots/app/`

Aplicação web (PWA) acessível via `app.zavvy.com.br`. Interface com sidebar fixa de navegação à esquerda.

**Usuário de teste:** Fabio da Silva Lino (`fabiosl@gmail.com`) — Plano **Starter** (em período de teste)
**Link de agendamento público:** `booking.zavvy.com.br/ofabio`

---

## Estrutura de Navegação (Sidebar)

| Item | Rota | Descrição |
|------|------|-----------|
| Home | `/dashboard` | Dashboard com resumo da semana |
| Agenda | `/agenda` | Calendário de agendamentos |
| Clientes | `/clients` | Lista e perfil de clientes |
| Configurações | `/settings` | Configurações gerais da conta |
| + Novo Agendamento | — | Botão de ação principal (verde) |
| Compartilhar Link | — | Atalho para link/QR Code |

---

## Dashboard (`/dashboard`)
**Screenshot:** `screenshots/app/dashboard/01-home.png`

- **Alerta de pendentes:** Banner amarelo indicando agendamentos sem confirmação do dia
- **Seção "Próximos":** Lista de próximos agendamentos (ou CTA para compartilhar link se vazia)
- **Link de agendamento:** `booking.zavvy.com.br/ofabio` com botões "Copiar link" e "QR Code"
- **Resumo semanal** (cards): Agendados (confirmados / pendentes) · Concluídos · Cancelados · Não compareceram
- **Resumo semanal em gráfico:** Período exibido no rodapé

---

## Agenda (`/agenda`)
**Screenshot:** `screenshots/app/agenda/`

### Views disponíveis
| View | Descrição |
|------|-----------|
| Dia | Visão horária de um único dia |
| Semana | Visão semanal (padrão) — colunas SEG a DOM |
| Lista | Listagem cronológica de agendamentos |

### Card de agendamento (na grade)
- Horário + nome do cliente + nome do serviço
- Cor: verde para confirmados, amarelo para pendentes

### Modal "Detalhes do agendamento"

| Campo | Detalhe |
|-------|---------|
| Status badge | Pendente / Confirmado / Concluído / Cancelado |
| Data e hora | Ex: Quarta-feira, 11 Março 2026, 10:00 – 11:00 (1h) |
| Cliente | Nome + telefone + botão WhatsApp |
| Serviço | Nome + duração + valor ("A combinar" se sem preço fixo) |
| Ações | Concluir · Remarcar horário · Não compareceu · Cancelar |

---

## Clientes (`/clients`)
**Screenshot:** `screenshots/app/clientes/`

### Lista de clientes
- **Busca** por nome
- **Filtros:** Todos · Agendados · Inativos · Ordenar (Mais recente)
- **Cards de resumo:** Total · Agendados · Atendimentos (total histórico)
- **Colunas:** Cliente · Telefone · Último Atendimento · Próximo · Atendimentos · (ícone WhatsApp)

### Perfil do cliente (`/clients/:id`)

- Avatar com iniciais + Nome + Telefone
- Contador: `N visitas` · `N agendados`
- Ações rápidas: **WhatsApp** · **Ligar** · **Agendar**

**Abas do perfil:**

| Aba | Conteúdo |
|-----|----------|
| Histórico | Agendamentos futuros (PRÓXIMOS) e passados (ANTERIORES) com status e ações |
| Mensagens | Conversa de WhatsApp trocada com o cliente via Zavvy |
| Anotações | Anotações privadas do profissional — cliente não tem acesso |

> **Gap identificado:** O perfil atual armazena apenas nome, telefone e anotações livres.
> Não há campos estruturados para dados clínicos (anamnese, diagnóstico, convênio, data de nascimento).

---

## Configurações (`/settings`)
**Screenshot:** `screenshots/app/configuracoes/`

### Perfil do usuário
- Avatar + Nome + Profissão + Status (badge "Teste") — clicável para editar

### MEU NEGÓCIO
| Item | Descrição |
|------|-----------|
| Serviços e preços | Gerencie seu catálogo de serviços |
| Horários de funcionamento | Defina sua disponibilidade por dia/hora |

### NOTIFICAÇÕES E LEMBRETES
| Notificação | Toggle | Observação |
|-------------|--------|------------|
| Notificações push | ✅ Ativo | Alertas no app |
| WhatsApp para clientes | ✅ Ativo | Confirmação + lembrete 24h antes — ~2 mensagens/agendamento a R$0,25/msg |
| Notificações por email | ✅ Ativo | Novos agendamentos e cancelamentos |

### INTEGRAÇÕES
| Integração | Status | Ação |
|------------|--------|------|
| WhatsApp | ✅ Conectado (+55 11 97777-7030) | Alterar |
| Google Calendar | — | Sincronize sua agenda |
| Link de agendamento | `booking.zavvy.com.br/ofabio` | Copiar |
| QR Code | — | Compartilhe visualmente |

### CONTA
| Item | Descrição |
|------|-----------|
| Assinatura | Plano Starter — clica para gerenciar |
| Perfil | Nome, foto e link de agendamento |
| Excluir conta | Apagar permanentemente |
| Sair da conta | Logout |

---

## Booking Público (`booking.zavvy.com.br/:slug`)
**Screenshots:** `screenshots/app/booking/`

Página pública de agendamento, acessível por clientes sem login. Exibe os serviços disponíveis e permite selecionar horário.

| Screenshot | Conteúdo |
|------------|---------|
| `01-pagina-publica.png` | Topo — nome do profissional, serviços disponíveis |
| `02-pagina-publica-bottom.png` | Seleção de data/horário e formulário do cliente |
