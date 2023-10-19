import os
import sys
import time

def menu():
    print("1. Inserir dados")
    print("2. Consultar dados")
    print("3. Excluir dados")
    print("4. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        inserir_dados()
    elif opcao == "2":
        consultar_dados()
    elif opcao == "3":
        excluir_dados()
    elif opcao == "4":
        sair()
    else:
        print("Opção inválida.")
        menu()

def salvar_dados(lista):
    with open("dados.txt", "w") as arquivo:
        for elemento in lista:
            arquivo.write(elemento + "\n")

def carregar_dados():
    lista = []
    try:
        with open("dados.txt", "r") as arquivo:
            for linha in arquivo:
                lista.append(linha.strip())  # Remove espaços em branco e quebras de linha
    except FileNotFoundError:
        pass  # Se o arquivo não existe, retorna uma lista vazia
    return lista

def inserir_dados():
    lista = carregar_dados()

    elemento = input("Digite o elemento a ser inserido: ")

    lista.append(elemento)

    salvar_dados(lista)

    print("Elemento inserido com sucesso.")

def consultar_dados():
    lista = carregar_dados()
    os.system("cls")
    elemento = input("Digite o elemento a ser consultado: ")

    if elemento in lista:
        print(f" {elemento} está na lista.\n")
        
    else:
        print(f" {elemento} não está na lista.\n")
        
def excluir_dados():
    lista = carregar_dados()

    elemento = input("Digite o elemento a ser excluído: ")

    if elemento in lista:
        lista.remove(elemento)
        salvar_dados(lista)
        print("Elemento excluído com sucesso.")
    else:
        print("O elemento não está na lista.")

def sair():
    print("Saindo do programa.")

menu()
