# Whatsapp Sender

Este projeto é um chatbot que utiliza a EvolutionAPI para enviar mensagens de texto, imagens, vídeos, áudios, PDFs e documentos via WhatsApp. A interface do usuário é construída com Streamlit e Flask é usado para gerenciar webhooks.


## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/AIChatbot.git
    cd AIChatbot
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente no  `.arquivoenv`:
    ```env
    EVO_API_TOKEN='seu_token_aqui'
    EVO_INSTANCE_TOKEN='seu_instance_token_aqui'
    EVO_INSTANCE_NAME='seu_instance_name_aqui'
    EVO_BASE_URL='http://localhost:8081'
    ```

# Uso

## Interface do Streamlit

A interface permitirá que você envie diferentes tipos de mensagens para um número de telefone especificado.

Webhook com Flask
Para iniciar o webhook do Flask, execute:

O webhook receberá mensagens e processará os dados recebidos.

## Estrutura dos Arquivos

app.py
Este arquivo contém a lógica para a interface do Streamlit, permitindo que os usuários enviem mensagens de diferentes tipos.

message_parser.py
Este arquivo contém a classe MessageReceived que é responsável por analisar e extrair dados de mensagens recebidas.

message_sender.py
Este arquivo contém a classe Send que é responsável por enviar mensagens de texto, imagens, vídeos, áudios, PDFs e documentos.

send_whatsapp_message.py
Este arquivo contém um exemplo de como usar a classe Send para enviar mensagens via Streamlit.

webhook_whatsapp.py
Este arquivo contém a configuração do Flask para receber webhooks e processar mensagens recebidas.

## Contribuição

Faça um fork do projeto.
Crie uma nova branch: git checkout -b minha-nova-funcionalidade
Faça suas alterações e commit: git commit -m 'Adiciona nova funcionalidade'
Envie para o branch original: git push origin minha-nova-funcionalidade
Crie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.


Para iniciar a interface do Streamlit, execute:
```sh
streamlit run app.py



