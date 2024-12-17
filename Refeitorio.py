# Classe que representa o Refeitório

class ErroRetiradaRefeitorio(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
#Esse erro ocorre quando o usuário tenta se retirar do refeitório sem estar presente nele, ou quando ele tenta sair sem ter entrado de maneira adequada.
class Refeitorio:
    def __init__(self, capacidade_maxima):
        self.capacidade_maxima = capacidade_maxima
        self.refeitorio_atual = []
        self.fila_espera = []
        self.contagem_janelas = {str(i): 0 for i in range(1, 9)}
        self.maximo_por_janela = 5

    def verificar_capacidade(self):
         try: # Tenta calcular a capacidade atual do refeitório.
             capacidade_atual = len(self.refeitorio_atual)
             print(f"Capacidade do refeitório: {capacidade_atual}/{self.capacidade_maxima}")
             if capacidade_atual == 0:
                 print("O refeitório não tem ninguém (°_°).")
             elif capacidade_atual == self.capacidade_maxima:
                 print("O refeitório está cheio <3.")
         except Exception as e:#captura qualquer erro inesperado durante a execução do código e exibe uma mensagem de erro.
             print(f"Erro ao verificar capacidade: {e}")

    def tentar_entrar(self, usuario, dia_atual, hora_atual):
        try:
            if usuario.dia_contraturno != dia_atual:# Associação: O usuário é associado ao refeitório
                print("Erro: Opa, hoje não é o seu dia de contraturno.")
                return
            if hora_atual != usuario.horario_escolhido:
                print("Erro: Não é o seu Horário  <3.")
                return
            if len(self.refeitorio_atual) < self.capacidade_maxima: # Composição: o usuário só pode estar no refeitório se houver capacidade
                print("lugares sobrando... Você entrou no refeitório!")
                self.refeitorio_atual.append(usuario.nome)
            else: # Agregação: o usuário é agregado à fila de espera, mas existe fora dela
                print("O refeitorio esta cheio, voce foi colocado na fila de espera!.")
                self.fila_espera.append(usuario.nome)
        except ValueError as e:#Captura erros específicos relacionados ao dia ou horário incorretos.
            print(e)
        except Exception as e:
            # Captura qualquer erro inesperado (por exemplo, erros de manipulação de objetos).
            print(f"Erro ao tentar entrar no refeitório: {e}")
    
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
                print("Erro: Oxe, você nem entrou no refeitório.")
    
        except ErroRetiradaRefeitorio as e:
            print(f"Erro: {e}")