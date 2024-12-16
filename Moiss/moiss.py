# Programação Orientada a Objetos - P.O.O
# 2°B - Vespertino
# Alunos: Moisés Claudino Oliveira



#------------------------------------------------------------------------------------------------------------------------------------------
#    Tratamento feito no dia 16 |
#                               |
#                               V
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


# Classe que representa o Refeitório
class Refeitorio:
    def __init__(self, capacidade_maxima):
        self.capacidade_maxima = capacidade_maxima
        self.refeitorio_atual = []
        self.fila_espera = []
        self.contagem_janelas = {str(i): 0 for i in range(1, 9)}
        self.maximo_por_janela = 5

    def verificar_capacidade(self):
        capacidade_atual = len(self.refeitorio_atual)
        print(f"Capacidade do refeitório: {capacidade_atual}/{self.capacidade_maxima}")
        if capacidade_atual == 0:
            print("O refeitório não tem ninguém (°_°).")
        elif capacidade_atual == self.capacidade_maxima:
            print("O refeitório está cheio <3.")

    def tentar_entrar(self, usuario, dia_atual, hora_atual):
        # Associação: O usuário é associado ao refeitório
        if usuario.dia_contraturno != dia_atual:
            print("Erro: Opa, hoje não é o seu dia de contraturno.")
            return

        if hora_atual != usuario.horario_escolhido:
            print("Erro: Não é o seu Horário  <3.")
            return

        # Composição: o usuário só pode estar no refeitório se houver capacidade
        if len(self.refeitorio_atual) < self.capacidade_maxima:
            print("lugares sobrando... Você entrou no refeitório!")
            self.refeitorio_atual.append(usuario.nome)
        else:
            print("O refeitorio esta cheio, voce foi colocado na fila de espera!.")
            # Agregação: o usuário é agregado à fila de espera, mas existe fora dela
            self.fila_espera.append(usuario.nome)

    def sair(self, usuario):
        if usuario.nome in self.refeitorio_atual:
            self.refeitorio_atual.remove(usuario.nome)
            print("Você se auto-Retirou do refeitório <3.")
            if self.fila_espera:
                proximo = self.fila_espera.pop(0)
                self.refeitorio_atual.append(proximo)
                print(f"{proximo} entrou no refeitório.")
        else:
            print("Erro:Oxe,voce nem entrou no refeitório.")


# Classe que gerencia o sistema
def validar_hora(hora):
    return re.match(r'^\d{2}:\d{2}$', hora) is not None


class SistemaDeGerenciamento:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.usuarios = {}
        self.dias_da_semana = {
            "1": "Segunda",
            "2": "Terça",
            "3": "Quarta",
            "4": "Quinta",
            "5": "Sexta"
        }
        self.janelas_de_tempo = {
            "1": "11:00",
            "2": "11:30",
            "3": "12:00",
            "4": "12:30",
            "5": "13:00",
            "6": "13:30",
            "7": "14:00",
            "8": "14:30"
        }
        # Composição: o refeitório faz parte do sistema e é criado com ele
        self.refeitorio = Refeitorio(5)
        self.carregar_usuarios()

    def cadastrar_usuario(self):
        nome = input("Digite o seu Nickname da vida Real: ")
        matricula = input("Matricula ou CPF: ")

        if not matricula:
            print("Erro: Matrícula ou CPF não pode ser vazia!!!")
            return

        print("Escolha seu dia de contraturno:")
        for chave, dia in self.dias_da_semana.items():
            print(f"{chave}: {dia}")
        dia_contraturno = input("Dia de contraturno: ")

        if dia_contraturno not in self.dias_da_semana:
            print("Erro: Dia de contra-turno inválido.")
            return

        senha = input("Digite a palavra ultra-hipe-mega-secreta: ")

        print("Escolha uma janela de horário para você almoçar:")
        for chave, horario in self.janelas_de_tempo.items():
            print(f"{chave}: {horario}")
        horario_escolhido = input("Escolha um horário: ")

        if horario_escolhido not in self.janelas_de_tempo or self.refeitorio.contagem_janelas[
            horario_escolhido] >= self.refeitorio.maximo_por_janela:
            print("Erro: Horário inválido ou lotado. Tente novamente.")
            return
#------------------------------------------------------------------------------------------------------------------------------------------
#    Tratamento feito no dia 17|
#                              |
#                              V
        # Composição: o usuário faz parte do sistema e é gerenciado por ele
        usuario = Usuario(nome, matricula, dia_contraturno, senha, self.janelas_de_tempo[horario_escolhido])
        self.usuarios[nome] = usuario
        self.salvar_usuario_arquivo(usuario)
        self.refeitorio.contagem_janelas[horario_escolhido] += 1
        print("Usuário cadastrado com sucesso (°u°)")

    def salvar_usuario_arquivo(self, usuario):
        try:
            with open(self.caminho_arquivo, 'a') as arquivo:
                linha = f"{usuario.nome},{usuario.matricula},{usuario.dia_contraturno},{usuario.senha},{usuario.horario_escolhido}\n"
                arquivo.write(linha)
        except Exception as e:
            print(f"Ocorreu um erro ao salvar o usuário: {e}")

    def carregar_usuarios(self):
        if os.path.exists(self.caminho_arquivo):
            try:
                with open(self.caminho_arquivo, 'r') as arquivo:
                    for linha in arquivo:
                        campos = linha.strip().split(',')
                        if len(campos) == 5:
                            nome, matricula, dia_contraturno, senha, horario_escolhido = campos
                            usuario = Usuario(nome, matricula, dia_contraturno, senha, horario_escolhido)
                            self.usuarios[nome] = usuario

                            for chave, horario in self.janelas_de_tempo.items():
                                if horario == horario_escolhido:
                                    self.refeitorio.contagem_janelas[chave] += 1
                                    break
            except Exception as e:
                print(f"Ocorreu um erro ao carregar os usuários: {e}")

    def login(self):
        matricula = input("Matricula ou CPF: ")
        senha = input("Digite a palavra ultra-hipe-mega-secreta: ")

        for usuario in self.usuarios.values():
            if usuario.matricula == matricula and usuario.senha == senha:
                print("Login bem-sucedido!")
                print("    |")
                print("    |")
                print("    |")
                print("    V")
                self.menu_usuario(usuario)
                return
        print("Erro: Matrícula ou senha incorreta!")

    def menu_usuario(self, usuario):
        while True:
            print("|-----------------------------|")
            print("|       MENU DE USUÁRIO       |")
            print("|-----------------------------|")
            print(" ")
            print("1. Entrar no refeitório")
            print("2. Sair do refeitório")
            print("3. Verificar capacidade do refeitório")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print("Que dia da semana é hoje? (1-5):")
                for chave, dia in self.dias_da_semana.items():
                    print(f"{chave}: {dia}")
                dia_atual = input("Dia de hoje: ")

                if dia_atual not in self.dias_da_semana:
                    print("Erro: Dia inválido.")
                    continue

                hora_atual = input("Que horas são? (HH:MM): ")
                if validar_hora(hora_atual):
                    self.refeitorio.tentar_entrar(usuario, dia_atual, hora_atual)
                else:
                    print("Erro: Formato de hora inválido. Use HH:MM.")
            elif opcao == "2":
                self.refeitorio.sair(usuario)
            elif opcao == "3":
                self.refeitorio.verificar_capacidade()
            elif opcao == "4":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def main(self):
        while True:
            print("|----------------------------------------------------|")
            print("|       Sistema de Gerenciamento de refeitório       |")
            print("|----------------------------------------------------|")
            print("")
            print("1. Cadastrar usuário")
            print("2. Login")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_usuario()
            elif opcao == "2":
                self.login()
            elif opcao == "3":
                print("")
                print("               Saindo do sistema...")
                print("|------------------------------------------------|")
                print("|          Código feito pelo Aluno:              |")
                print("|          -Moisés Claudino Oliveira             |")
                print("|________________________________________________|")

                break
            else:
                print("Opção inválida. Tente novamente.")


# Iniciar o programa
if __name__ == "__main__":
    sistema = SistemaDeGerenciamento('usuarios.txt')
    sistema.main()
