# Classe que representa o Refeitório
import re
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
