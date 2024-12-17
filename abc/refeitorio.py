import re

# Classe que representa o Refeitório
class Refeitorio:
    def __init__(self, capacidade_maxima):
        self.capacidade_maxima = capacidade_maxima
        self.refeitorio_atual = []
        self.fila_espera = []
        self.contagem_janelas = {str(i): 0 for i in range(1, 9)}
        self.maximo_por_janela = 5
    def verificar_capacidade(self):
        try:
            capacidade_atual = len(self.refeitorio_atual)
            print(f"Capacidade do refeitório: {capacidade_atual}/{self.capacidade_maxima}")
            if capacidade_atual == 0:
                print("O refeitório não tem ninguém (°_°).")
            elif capacidade_atual == self.capacidade_maxima:
                print("O refeitório está cheio <3.")
        except Exception as e:
            print(f"Ocorreu um erro ao verificar a capacidade: {e}")  # Tratamento de exceção para erros gerais

    def tentar_entrar(self, usuario, dia_atual, hora_atual):
        try:
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
        except AttributeError as e:
            print(f"Erro de Atributo: {e}. Verifique os dados do usuário.")  # Caso os atributos do usuário estejam ausentes ou incorretos
        except Exception as e:
            print(f"Ocorreu um erro ao tentar entrar no refeitório: {e}")  # Tratamento de exceção genérica

    def sair(self, usuario):
        try:
            if usuario.nome in self.refeitorio_atual:
                self.refeitorio_atual.remove(usuario.nome)
                print("Você se auto-Retirou do refeitório <3.")
                if self.fila_espera:
                    proximo = self.fila_espera.pop(0)
                    self.refeitorio_atual.append(proximo)
                    print(f"{proximo} entrou no refeitório.")
            else:
                print("Erro:Oxe,voce nem entrou no refeitório.")
        except ValueError as e:
            print(f"Erro de Valor: {e}. O usuário não foi encontrado na lista.")  # Caso não consiga remover um usuário da lista
        except Exception as e:
            print(f"Ocorreu um erro ao sair do refeitório: {e}")  # Tratamento de exceção genérica


# Classe que gerencia o sistema
def validar_hora(hora):
    try:
        # Tentando validar o formato de hora
        if not re.match(r'^\d{2}:\d{2}$', hora):
            raise ValueError("Formato de hora inválido. Use HH:MM.")  # Lançando uma exceção personalizada
        return True
    except ValueError as e:
        print(f"Erro de validação: {e}")  # Captura de exceção de formato
        return False
    except Exception as e:
        print(f"Ocorreu um erro ao validar a hora: {e}")  # Tratamento de exceção genérica
        return False
