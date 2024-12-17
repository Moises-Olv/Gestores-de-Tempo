# Programação Orientada a Objetos - P.O.O
# 2°B - Vespertino
# Aluna: Ana Clara Rodrigues
import os
import re
# Título do sistema
print("               |-----------------------|")
print("               |   GESTORES DE TEMPO   |")
print("               |                       |")
print("               |-----------------------|")
print("       ")
# Classe Usuario
class Usuario:
    def __init__(self, nome, matricula, dia_contraturno, senha, horario_escolhido):
        self.nome = nome
        self.matricula = matricula
        self.dia_contraturno = dia_contraturno
        self.senha = senha
        self.horario_escolhido = horario_escolhido