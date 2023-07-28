# Projeto de ChatBot com GPT-4:

# import
import openai

# Chave
openai.api_key = "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"

# função para gerar texto a partir do modelo de linguagem
def gera_texto(texto):

    # obtém a resposta do modelo
    response = openai.Completion.create(

        # modelo usado
        # disposição de outros modelos: http://platform.openai.com/account/rete-limits
        engine = "text-davinci-003",

        # texto incial da conversa com o agente
        prompt = texto,

        # Comprimento da resposta gerada pelo modelo
        max_tokens = 150,

        # Número de conclusões geradas para cada prompt
        n = 2,

        # O texto retornado não deve conter a sequência de parada.
        stop = None,

        # Uma medida da aleatoriedade de um texto gerado pelo modelo. Seu valor está entre 0 e 1.
        # Valores próximos a 1 significam que a saída é mais aleatória, enquanto valores próximos a...
        # ... 0 indicam que a saída é muito identificável.
        temperature = 0.8,

    )

    return response.choices[0].text.strip()

# função principal do programa em Python
def main():

    print("\nBem-vindo ao GPT3.5 Chatbot do André!")
    print("(Digite 'sair' a qualquer momento para sair do chat)")

    # loop
    while True:

        # coleta a pergunta digitada pelo usuário
        user_message = input("\nVocê: ")

        # se a mensagem for 'sair' finaliza o programa
        if user_message.lower() == "sair":
            break

        # coloca a mensagem digita pelo usuário na variável Python chamada gpt3_5_promt
        gpt3_5_promt = f"\nUsuário: {user_message}\nChatbot:"

        # obtém a resposta do modelo executando a função gera_texto()
        chatbot_response = gera_texto(gpt3_5_promt)

        # imprime a resposta do chatbot
        print(f"\nChatbot: {chatbot_response}")

# Execução do programa (bloco main) em Python
if __name__ == "__main__":
    main()