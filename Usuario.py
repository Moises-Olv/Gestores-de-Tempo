# Programação Orientada a Objetos - P.O.O
# 2°B - Vespertino
# Alunos: Ana Clara Rodrigues; Lívia Esteves de Oliveira; Moisés Claudino Oliveira; Sarha Sthefanny Araripe Silva

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