import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError, APIError


def carregar_base_conhecimento():
    caminho_base = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(caminho_base, "..", "data", "conhecimento.txt")

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Diretrizes padrão de ensino de inglês."


def main():
    client = genai.Client()
    base_conhecimento = carregar_base_conhecimento()

    system_instruction = f"""
    Você é o 'LingoBot', um tutor inteligente e amigável para aprendizado de inglês.

    DIRETRIZES E BASE DE CONHECIMENTO:
    ---
    {base_conhecimento}
    ---

    REGRAS DE FUNCIONAMENTO:
    1. Se o usuário digitar uma palavra solta: forneça a tradução, nível (A1-C2), 2 sinônimos, 2 frases de exemplo e uma 🖼️ Descrição Visual / Emoji para fixação.
    2. Se o usuário conversar em inglês: responda em inglês mantendo o diálogo. Se houver erro de gramática/escrita, inclua no final a seção "💡 Correção Didática".
    3. Se o usuário pedir "exercício" ou "prática": envie uma frase em português para ele traduzir ou uma frase em inglês com lacuna para preencher.
    4. Mantenha as explicações gramaticais curtas, diretas e simples.
    """

    print("==================================================")
    print("  Welcome to LingoBot! 🇬🇧🇺🇸")
    print("  Seu assistente virtual para aprender inglês.")
    print("==================================================")
    print("Você pode:")
    print(" -> Digitar uma palavra para ver tradução, usos e dica visual.")
    print(" -> Conversar em inglês para praticar (eu corrijo seus erros!).")
    print(" -> Digitar 'exercicio' para testar seus conhecimentos.")
    print(" -> Digitar 'sair' para encerrar.\n")


    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.4,
        )
    )

    while True:
        entrada_usuario = input("Você: ")

        if entrada_usuario.lower() in ["sair", "exit", "quit"]:
            print("\nLingoBot: See you later! Keep practicing! 👋")
            break

        if not entrada_usuario.strip():
            continue

        tentativas = 3
        for i in range(tentativas):
            try:
                response = chat.send_message(entrada_usuario)
                print(f"\nLingoBot: {response.text}\n" + "-" * 50)
                break
            except (ServerError, APIError) as e:
                if i < tentativas - 1:
                    print("\n[Aviso] O servidor da Google está sobrecarregado. Tentando novamente em 2 segundos...")
                    time.sleep(2)
                else:
                    print(
                        "\n[Erro] Os servidores da IA estão instáveis no momento. Por favor, tente novamente em instantes.")


if __name__ == "__main__":
    main()