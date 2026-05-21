# 🤖 pAIrBot: Pair Programming com IA

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Um agente de IA projetado para auxiliar estudantes de programação de forma **didática e interativa**, sem fornecer soluções prontas. Ele funciona como um verdadeiro par de programação: faz perguntas, sugere melhorias, aponta erros e incentiva o raciocínio crítico.

## 📋 Pré-requisitos

- Python 3.12 ou superior
- `pip` (gerenciador de pacotes)
- Chave de API da Google AI Studio. ([Saiba mais](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br))

## 🚀 Como executar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/pairbot.git
   cd pairbot
   ```
2. Crie um ambiente virtual (recomendado)
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate      # Windows
    ```
3. Instale as dependências
    ```bash
    pip install -r requirements.txt
    ```
4. Configure a chave de API nas variáveis de ambiente
    ```bash
    # .env
    GOOGLE_API_KEY=<SUA_CHAVE_AQUI>
    ```
5. Execute o agente
    ```bash
    python3 agent.py
    ```
