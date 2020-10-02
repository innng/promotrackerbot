  # Promotracketbot

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
  **Nome:** Ajuda ao usuário\
  **Como um** usuário do bot\
  **Eu quero** poder visualizar as funcionalidades e comandos do bot\
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
  
	### 2ª Sprint 
    
  #### Estória 1
  **Nome:** Modelar banco de dados\
  **Como um** Como um desenvolvedor do bot\
  **Eu quero** ter uma interface clara com o banco de dados\
  **Para que** eu possa adicionar, atualizar, remover e ler os dados necessários
  
  **Tasks:**

  * Definir campos necessários à aplicação (Gabriel)
  * Modelar salvamento dos dados (Gabriel)
  * Definir relação entre os diversos componentes (Gabriel)
  * Modelar funções auxiliares para salvar dados corretamente no banco (Gabriel)
  
  #### Estória 2
  **Nome:** Provisionar bot na nuvem \
  **Como um** usuário do bot \
  **Eu quero** que o bot esteja disponível continuamente \
  **Para que** eu possa utilizar o bot em qualquer momento

  **Tasks:**

  * Fazer as configurações necessárias para subir o bot em ambiente de nuvem (Ingrid)
  * Testar o deploy do bot na Google App Engine / Google Cloud Functions (Ingrid)
  * Adicionar passo de build automático ao CI (Ingrid)
  * Adicionar passo de deploy automático ao CI (Ingrid)
	
  #### Estória 3
  **Nome:** Implementar client da Steam \
  **Como um** deselvolvedor do bot\
  **Eu quero** uma api que converse com a Steam esteja disponível\
  **Para que** o bot consiga buscar as informações necessárias sobre os jogos

  **Tasks:**

  * Escolher a API a ser usada (Gabriel)
  * Implementar função que busca os dados da API (Gabriel)
  
  #### Estória 4
  **Nome:** Implementar client de Redis \
  **Como um** desenvolvedor do bot \
  **Eu quero** ter métodos auxiliares\
  **Para que** a comunicação com banco de dados seja facilitada

  **Tasks:**

  * Definir métodos essenciais para comunicação com banco (Ingrid)
  * Fornecer métodos para adicionar, ler e remover dados do banco (Ingrid)
  * Garantir tratamento de erros e exceções (Ingrid)
  * Criar testes de regressão para o client (Ingrid)
  
  #### Estória 5
  **Nome:** Trackear DLC de um jogo \
  **Como um** usuário do bot \
  **Eu quero** poder seguir também as DLC's dos jogos que desejo comprar \
  **Para que** eu possa adicionar conteúdo ao jogo desejado a um preço baixo.

  **Tasks:**

  * Acessar as DLC's de um jogo e seus respectivos preços no banco de dados (Raydan)
  * Criar um botão "DLC" (Raydan)
  * Quando acionado o botão, alterar o comportamento da tracklist para também trackear as DLC's do jogo (Raydan)
  
   #### Estória 6
  **Nome:** Melhorar comando de adição \
  **Como um** usuário \
  **Eu quero** poder adicionar um jogo e que ela persista na minha tracklist \
  **Para que** eu possa acompanhar as promoções do jogo desejado.

  **Tasks:**

  * Comunicar o banco de dados com a aplicação bot (Raydan)
  * Persistir o jogo adicionado no banco de dados (Raydan)
  
  
  #### Estória 7
  **Nome:** Melhorar comando de rastreamento \
  **Como um** usuário \
  **Eu quero** poder acessar minha lista de jogos salvos \
  **Para que** eu possa ver os preços atuais dos jogos selecionados.

  **Tasks:**

  * Comunicar o banco de dados com a aplicação bot (Ingrid)
  * Persistir a lista de jogos adicionados no banco de dados (Ingrid)
  
  #### Estória 8
  **Nome:** Implementar comando remove \
  **Como um** usuário \
  **Eu quero** poder deletar um jogo da minha lista de jogos \
  **Para que** eu possa controlar melhor quais jogos eu quero acompanhar o preço.

  **Tasks:**

  * Criar comando de deletar o jogo da lista do usuário (Gabriel)
  * Deletar o jogo selecionado da lista do usuário no banco de dados (Gabriel)
  
  #### Estória 9
  **Nome:** Implementar comando remove all \
  **Como um** usuário \
  **Eu quero** poder deletar a minha lista de jogos \
  **Para que** eu possa parar de acompanhar o preço dos jogos antes selecionados

  **Tasks:**

  * Criar comando de deletar toda a lista (Raydan)
  * Deletar a lista de jogos selecionadas no banco de dados (Raydan)
  * Deleta o usuário do banco de dados (Raydan)
