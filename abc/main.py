# Programação Orientada a Objetos - P.O.O
# 2°B - Vespertino
# Aluna: Livia Esteves de  Oliveira
from sistema import SistemaDeGerenciamento

print("               |-----------------------|")
print("               |   GESTORES DE TEMPO   |")
print("               |                       |")
print("               |-----------------------|")
print("                                        ")
# Iniciar o programa
if __name__ == "__main__":
    sistema = SistemaDeGerenciamento('usuarios.txt')
    try:
        sistema.main()  # Chama a função principal
    except KeyboardInterrupt:
        print("\nProcesso interrompido pelo usuário. O programa será encerrado.")  # Mensagem amigável
