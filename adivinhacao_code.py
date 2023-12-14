import streamlit as st
import random

def jogo_adivinhacao():
    # Título da aplicação
    st.title("Jogo de Adivinhação")

    # Gera um número aleatório entre 1 e 10
    numero_secreto = random.randint(1, 10)

    tentativas = 0

    # Caixa de entrada para o jogador fazer um palpite com chave única
    palpite = st.number_input("Faça seu palpite de um número entre 1 e 10:", min_value=1, max_value=100, key="palpite")

    if st.button("Verificar Palpite"):
        tentativas += 1
        if palpite == numero_secreto:
            st.success(f"Parabéns! Você acertou em {tentativas} tentativas. O número secreto era {numero_secreto}.")
        elif palpite < numero_secreto:
            st.info("Tente um número maior.")
        else:
            st.info("Tente um número menor.")

# Chama a função do jogo
jogo_adivinhacao()
