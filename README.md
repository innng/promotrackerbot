* # Promotracketbot

  A telegram bot to keep track of game prices and sales on the steam platform.

  ## Usage

  The bot can be found at the [promotracker_bot link](http://t.me/promotracker_bot) or by the @promotracker_bot username by searching it on Telegram.

  More information about the bot's commands can be retrieved with the /help command.

  ## Code style

  For Python code:

  * PEP8 (using Flake8 and Pydocstyle);
  * Black for auto formatting;
  * Snake case.

  For git management:

  * Commit messages using imperative mode ("fix", "modify", "change", "remove");
  * English only.

  ## Technologies

  Python

  Redis

  Telegram

  Heroku

  Docker

  ## Architecture

  Package Diagram UML

  ![UML Package](https://i.imgur.com/CZUP7MT.png)

  ## Sprint Planning

  ### 1ª Sprint 

  #### Estória 1
  **Nome:** Configurar ambiente de desenvolvimento\
  **Como um** desenvolvedor do bot\
  **Eu quero** ter um ambiente de desenvolvimento bem definido\
  **Para que** eu consiga desenvolver novas features e aplicar correções

  **Tasks:**

  * Definir ambientes de desenvolvimento (Ingrid)
  * Implementar maneira local de executar (Ingrid)
  * Configurar as dependências (Ingrid)
  * Configurar pipeline para entrega contínua (Ingrid)

  #### Estória 2
  **Nome:** Encontrar o bot na busca do Telegram\
  **Como um** usuário do Telegram\
  **Eu quero** buscar pelo nome do bot\
  **Para que** eu possa interagir com ele

  **Tasks:**

  * Gerar o token do bot usando a API do Telegram (Gabriel)
  * Configurar as informações principais do bot (nome, avatar, etc) (Raydan)
  * Testar a url/username do bot gerado (Raydan)


  #### Estória 3
  **Nome:** Ajuda ao usuário
  **Como um** usuário do bot
  **Eu quero** poder visualizar as funcionalidades e comandos do bot
  **Para que** eu possa me orientar na busca e gerência dos produtos que desejo monitorar o preço 

  **Tasks:**

  * Tratar comando `/help` recebido pelo bot (Gabriel)
  * Criar função que envia resposta com a mensagem de ajuda (Gabriel)

  #### Estória 4
  **Nome:** Mensagem de boas vindas\
  **Como um** usuário do bot\
  **Eu quero** receber instruções sobre o funcionamento do bot ao interagir com ele pela primeira vez\
  **Para que** eu saiba como utiliza-lo

  **Tasks:**

  * Tratar comando `/start` recebido pelo bot (Raydan)
  * Criar função que envia resposta com a mensagem de boas vindas (Raydan)


  #### Estória 5
  **Nome:** Adicionar item à lista de rastreamento\
  **Como um** usuário do bot\
  **Eu quero** poder adicionar itens à lista de rastreamento\
  **Para que** eu seja avisado caso exista uma promoção

  **Tasks:**

  * Tratar comando `/add` recebido pelo bot (Gabriel)
  * Criar função que envia resposta com item adicionado (Gabriel)

  #### Estória 6
  **Nome:** Listar produtos rastreados\
  **Como um** usuário do bot\
  **Eu quero** poder listar os produtos que pedi para o bot rastrear\
  **Para que** eu possa ver todos os produtos que ainda estão sendo rastreados

  **Tasks:**

  * Implementar client de comunicação com o banco de dados (Ingrid)
  * Tratar comando `/tracklist` recebido pelo bot (Gabriel)
  * Criar função que envia resposta com a lista de produtos rastreados (Raydan)