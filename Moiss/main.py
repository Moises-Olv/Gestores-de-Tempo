# Programação Orientada a Objetos - P.O.O
# 2°B - Vespertino
# Aluno: Moisés Claudino Oliveira
from sistema_de_gerenciamento import SistemaDeGerenciamento

print("               |-----------------------|")
print("               |   GESTORES DE TEMPO   |")
print("               |                       |")
print("               |-----------------------|")
print("       ")
# Iniciar o programa
if __name__ == "__main__":
    sistema = SistemaDeGerenciamento('usuarios.txt')
    sistema.main()
