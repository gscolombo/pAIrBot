from google import genai
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = open("system_prompt.md", "r").read()

client = genai.Client() # Instancia cliente com a chave de API (GOOGLE_API_KEY) nas variáveis de ambiente

# Configura uma conversa com acompanhamento de histórico (multi-turn)
chat = client.chats.create(model="gemini-3.1-flash-lite",
                           config=genai.types.GenerateContentConfig(
                               system_instruction=SYSTEM_PROMPT # Inclui system prompt para configurar o agente
                           ))

print("Conversa iniciada. Digite \"sair\" para encerrar o programa.")

while True:
    message = input(">> ").strip()

    if message.lower() == "sair":
        break

    print()
    response = chat.send_message_stream(message)

    print("<< Aguardando resposta...", end="", flush=True)

    for i, chunk in enumerate(response):
        if i == 0:
            print(f"\rpAIrBot: {chunk.text}", end="", flush=True)
        else:
            print(chunk.text, end="", flush=True)

    print("\n")
