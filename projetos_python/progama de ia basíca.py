import random

# Banco de dados inicial de perguntas e respostas
base_conhecimento = {
    "oi": ["Oi!", "Olá!", "E aí, tudo bem?"],
    "tudo bem": ["Estou bem! E você?", "Tudo ótimo por aqui."],
    "qual é o seu nome": ["Sou uma IA básica feita em Python.", "Ainda não tenho nome, mas podemos inventar um."],
}

print("🤖 Olá! Sou uma IA simples. Digite 'sair' para encerrar.")

while True:
    pergunta = input("Você: ").lower().strip()

    if pergunta == "sair":
        print("🤖 Até logo!")
        break

    # Se já conheço a resposta
    if pergunta in base_conhecimento:
        print("🤖", random.choice(base_conhecimento[pergunta]))
    else:
        print("🤖 Não sei responder isso ainda.")
        nova_resposta = input("O que eu deveria responder? ").strip()

        # Salva a nova resposta
        base_conhecimento[pergunta] = [nova_resposta]
        print("🤖 Entendi! Vou lembrar disso.")
