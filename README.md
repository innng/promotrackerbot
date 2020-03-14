# Promobot

A telegram bot to keep track of products' prices on a certain website. 

## Usage

The bot can be found at the [promotracker_bot link](http://t.me/promotracker_bot) or by the @promotracker_bot username.

More information about the bot's commands can be retrivied with the /help command.

## Code style

For Python code:
* PEP8 (using Flake8 and Pydocstyle);
* Black for auto formatting;
* Snake case.

For git management:
* Commit messages using imperative mode ("fix", "modify", "change", "remove");
* English only.

## Technologies

## Contributing

Contributions are on hold for now, since this is a course assignment.

## Architecture
Package Diagram UML

![UML Package](https://i.imgur.com/TLlKFwL.png)

## Sprint Planning

### 1ª Sprint 

**Nome:** Provisionar bot\
**Como um** Desenvolvedor do bot\
**Eu quero** ter um local para subir as modificações\
**para que** as implementações do bot possam ser feitas e testadas em um ambiente similar ou igual ao de produção

**Acceptance Criteria**
1. Bot está rodando na AWS
2. Comunicação básica com o bot pode ser feita via API

**Tasks**
1. Criar conta AWS
2. Configurar AWS Lambda para receber código do bot
3. Abrir uma rota de comunição com o bot via API Gateway
4. Configurar CI com testes e deploy automático

**Responsável:** Ingrid

---

**Nome:** Encontrar o bot na busca do Telegram\
**Como um** Usuário do Telegram\
**Eu quero** buscar pelo nome do bot\
**para que** eu possa interagir com ele

**Acceptance Criteria**
1. Usuário consegue colocar o nome do bot na busca
2. Resultado da busca retorna nosso bot
3. Usuário consegue abrir uma janela de conversa com o bot

**Tasks**
1. Gerar o token do bot usando a API do Telegram
2. Configurar as informações principais do bot (nome, avatar, etc)
3. Testar a url/username do bot gerado

**Responsável:** Ingrid

----
**Nome:** Ajuda ao usuário\ 
**Como um** usuário do bot\
**Eu quero** poder visualizar as funcionalidades e comandos do bot\
**para que** eu possa me orientar na busca e gerência dos produtos que desejo monitorar o preço 

**Acceptance Criteria**
1. Usuário consegue com um comando /help visualizar a lista de comandos disponíveis
2. Usuário consegue visualizar um tutorial de utilização

**Tasks**
1. Tratar comando /help recebido pelo bot
2. Criar função que envia resposta com a mensagem de ajuda

**Responsável:** Raydan

----
**Nome:** Listar sites suportados\
**Como um** usuário do bot\
**Eu quero** saber quais sites posso rastrear\
**para que** eu possa saber quais produtos o bot suporta

**Acceptance Criteria**
1. Usuário consegue ver o comando de listar no help
2. Usuário consegue executar comando de listar
3. Bot retorna uma lista com os sites que suporta

**Tasks**
1. Tratar comando /listsites recebido pelo bot
2. Criar função que envia resposta com a lista de sites suportados

**Responsável:** Gabriel

----
**Nome:** Mensagem de boas vindas\
**Como um** usuário do bot\
**Eu quero** receber instruções sobre o funcionamento do bot ao interagir com ele pela primeira vez\
**para que** eu saiba como utiliza-lo

**Acceptance Criteria**
1. Comando /start ativa o bot
2. Bot envia uma mensagem para o usuário dando informações sobre o funcionamento do sistema e onde procurar ajuda

**Tasks**
1. Tratar comando /start recebido pelo bot
2. Criar função que envia resposta com a mensagem de boas vindas

**Responsável:** Raydan

----
**Nome:** Listar produtos rastreados\
**Como um** usuário do bot\
**Eu quero** poder listar os produtos que pedi para o bot rastrear\
**para que** eu possa ver todos os produtos que ainda estão sendo rastreados

**Acceptance Criteria**
1. O bot procura no banco os produtos rastreados pelo usuário
2. Usuário recebe a lista de nomes e links rastreados

**Tasks**
1. Implementar client de comunicação com o database Redis
2. Tratar comando /listproducts recebido pelo bot
3. Criar função que envia resposta com a lista de produtos rastreados

**Responsável:** Gabriel

---
