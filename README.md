# [GeminiDev Helper] 🤖

Este repositório contém um agente de IA experimental desenvolvido em **Python**, utilizando a **API do Gemini**. 

O projeto não tem como objetivo ser uma ferramenta de produção, mas sim um **laboratório de estudo** para explorar a integração de LLMs (Large Language Models) com sistemas de arquivos locais e automação de tarefas simples de codificação.

## 🎯 Objetivos de Estudo
* Compreender o consumo da API do Google Gemini via SDK.
* Praticar a manipulação de contexto (Prompt Engineering) para análise de código.
* Implementar um ciclo de "Percepção-Ação" onde a IA analisa um erro e sugere uma correção funcional.
* Explorar o uso de variáveis de ambiente e segurança de chaves de API.

## 🧩 O Desafio: A Calculadora
O agente atua sobre um mini projeto de calculadora (localizado na pasta `/calculator`).
- **Cenário:** A calculadora possui bugs propositais ou funcionalidades incompletas.
- **Ação:** O agente deve ler o código, identificar a falha e propor a solução.

## 🏗️ Arquitetura Simples
O fluxo de funcionamento segue a lógica:
1. **Entrada:** O usuário aponta um problema ou arquivo.
2. **Contexto:** O agente lê os arquivos Python da calculadora.
3. **Processamento:** A API do Gemini analisa o código conforme as instruções do sistema.
4. **ação:**: O agente inicia um loop para acessar e agir de forma autônoma para concluir a solicitação do usuário
5. **Resposta:** O agente devolve a respostas com as ações e soluções realizadas, ao usuário 

## 🛠️ Tecnologias
* **Linguagem:** Python >=3.10
* **LLM:** Google Gemini **gemini-2.5-flash**
* **Bibliotecas:** `google.genai`, `python-dotenv`

## 🚀 Como Executar o Experimento
1. Clone o repositório:
   ```bash
   git clone https://github.com/andretrindade13/geminidev.git
2. Inicie o servidor
   ```bash
   -- antes de solicitar uma correçao no código, tente criar um bug propositalmente no projeto de exemplo /calculator para que o agente corrija
   uv run main.py "<Seu prompt>"
3. ⚠️ Esta implemetação de agente de IA é para fins educacionais, não use este código para outros projetos, por motivo de segurança.


## 📁 Estrutura do Projeto
```text
├── calculator/         # O mini projeto de calculadora alvo
├── functions/          # funções utilitárias para leitura, escrita e limitações de acesso a arquivos
├── .env                # Variáveis sensíveis (API Keys)
└── main.py             # Ponto de entrada do projeto