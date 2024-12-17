import os
from usuarios import Usuario
from refeitorio import Refeitorio, validar_hora


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
        try:
            nome = input("Digite o seu Nickname da vida Real: ")
            matricula = input("Matricula ou CPF: ")

            if not matricula:
                raise ValueError("Matrícula ou CPF não pode ser vazia!!!")  # Criação de exceção personalizada

            print("Escolha seu dia de contraturno:")
            for chave, dia in self.dias_da_semana.items():
                print(f"{chave}: {dia}")
            dia_contraturno = input("Dia de contraturno: ")

            if dia_contraturno not in self.dias_da_semana:
                raise ValueError("Dia de contra-turno inválido.")  # Exceção personalizada

            senha = input("Digite a palavra ultra-hipe-mega-secreta: ")

            print("Escolha uma janela de horário para você almoçar:")
            for chave, horario in self.janelas_de_tempo.items():
                print(f"{chave}: {horario}")
            horario_escolhido = input("Escolha um horário: ")

            if horario_escolhido not in self.janelas_de_tempo or self.refeitorio.contagem_janelas[
                horario_escolhido] >= self.refeitorio.maximo_por_janela:
                raise ValueError("Horário inválido ou lotado. Tente novamente.")  # Exceção personalizada

            # Composição: o usuário faz parte do sistema e é gerenciado por ele
            usuario = Usuario(nome, matricula, dia_contraturno, senha, self.janelas_de_tempo[horario_escolhido])
            self.usuarios[nome] = usuario
            self.salvar_usuario_arquivo(usuario)
            self.refeitorio.contagem_janelas[horario_escolhido] += 1
            print("Usuário cadastrado com sucesso (°u°)")
        except ValueError as e:  # Tratamento de exceções para valores inválidos
            print(f"Erro: {e}")
        except Exception as e:  # Captura de outros tipos de erro
            print(f"Ocorreu um erro ao cadastrar o usuário: {e}")
        finally:
            print("Fim do processo de cadastro.")  # Mensagem final sempre será mostrada

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
        try:
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
            raise ValueError("Matrícula ou senha incorreta!")  # Exceção personalizada
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao tentar fazer login: {e}")

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

            try:
                if opcao == "1":
                    print("Que dia da semana é hoje? (1-5):")
                    for chave, dia in self.dias_da_semana.items():
                        print(f"{chave}: {dia}")
                    dia_atual = input("Dia de hoje: ")

                    if dia_atual not in self.dias_da_semana:
                        raise ValueError("Dia inválido.")  # Exceção personalizada

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
                    raise ValueError("Opção inválida. Tente novamente.")  # Exceção personalizada
            except ValueError as e:
                print(f"Erro: {e}")
            except Exception as e:
                print(f"Ocorreu um erro no menu do usuário: {e}")
            finally:
                print("Fazendo a validação do menu...")

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

            try:
                if opcao == "1":
                    self.cadastrar_usuario()
                elif opcao == "2":
                    self.login()
                elif opcao == "3":
                    print("")
                    print("               Saindo do sistema...")
                    print("|------------------------------------------------|")
                    print("|                  Aluna:              |")
                    print("|      Sarha Sthefanny Araripe Silva|")
                    print("|________________________________________________|")
                    break
                else:
                    raise ValueError("Opção inválida. Tente novamente.")  # Exceção personalizada
            except ValueError as e:
                print(f"Erro: {e}")
            except Exception as e:
                print(f"Ocorreu um erro no sistema principal: {e}")
            finally:
                print("Processo principal finalizado.")