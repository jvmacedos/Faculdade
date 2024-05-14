import random

class NoProcesso:
    def __init__(self, processo_id, tamanho):
        self.processo_id = processo_id
        self.tamanho = tamanho
        self.proximo = None

class Memoria:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.inicio = None

    def alocar_primeiro_fit(self, processo):
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.tamanho >= processo.tamanho:
                novo_no = NoProcesso(processo.processo_id, processo.tamanho)
                novo_no.proximo = atual.proximo

                if anterior is not None:
                    anterior.proximo = novo_no
                else:
                    self.inicio = novo_no

                return True
            else:
                anterior = atual
                atual = atual.proximo

        return False

    def alocar_best_fit(self, processo):
        melhor_ajuste = None
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.tamanho >= processo.tamanho:
                if melhor_ajuste is None or atual.tamanho < melhor_ajuste.tamanho:
                    melhor_ajuste = atual
                    melhor_anterior = anterior

            anterior = atual
            atual = atual.proximo

        if melhor_ajuste is not None:
            novo_no = NoProcesso(processo.processo_id, processo.tamanho)
            novo_no.proximo = melhor_ajuste

            if melhor_anterior is not None:
                melhor_anterior.proximo = novo_no
            else:
                self.inicio = novo_no

            return True

        return False

    def alocar_worst_fit(self, processo):
        pior_ajuste = None
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.tamanho >= processo.tamanho:
                if pior_ajuste is None or atual.tamanho > pior_ajuste.tamanho:
                    pior_ajuste = atual
                    pior_anterior = anterior

            anterior = atual
            atual = atual.proximo

        if pior_ajuste is not None:
            novo_no = NoProcesso(processo.processo_id, processo.tamanho)
            novo_no.proximo = pior_ajuste

            if pior_anterior is not None:
                pior_anterior.proximo = novo_no
            else:
                self.inicio = novo_no

            return True

        return False

    def alocar_random_fit(self, processo):
        blocos_livres = []
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.tamanho >= processo.tamanho:
                blocos_livres.append((atual, anterior))

            anterior = atual
            atual = atual.proximo

        if blocos_livres:
            bloco_escolhido, anterior_bloco = random.choice(blocos_livres)

            novo_no = NoProcesso(processo.processo_id, processo.tamanho)
            novo_no.proximo = bloco_escolhido

            if anterior_bloco is not None:
                anterior_bloco.proximo = novo_no
            else:
                self.inicio = novo_no

            return True

        return False

    def alocar_fifo(self, processo):
        novo_no = NoProcesso(processo.processo_id, processo.tamanho)

        if self.inicio is None:
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no

        return True

    def desalocar_processo(self, processo_id):
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.processo_id == processo_id:
                if anterior is not None:
                    anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo

                return True
            else:
                anterior = atual
                atual = atual.proximo

        return False

class GeradorDeProcessos:
    def __init__(self):
        self.processo_id_counter = 0

    def gerar_processo(self):
        processo_id = self.processo_id_counter
        self.processo_id_counter += 1
        tamanho = random.randint(10, 50)

        return NoProcesso(processo_id, tamanho)

def main():
    memoria = Memoria(1000)
    gerador = GeradorDeProcessos()
    processos_gerados = []
    processos_descartados = []

    for segundo in range(100):
        for _ in range(2):
            processo = gerador.gerar_processo()
            processos_gerados.append(processo)

            if not memoria.alocar_fifo(processo):
                processos_descartados.append(processo)

        if segundo % 1 == 0:
            for _ in range(random.randint(1, 2)):
                if processos_gerados:
                    processo_remover = random.choice(processos_gerados)
                    memoria.desalocar_processo(processo_remover.processo_id)
                    processos_gerados.remove(processo_remover)

    # Calcular e imprimir as métricas globais
    tamanho_medio = sum([processo.tamanho for processo in processos_gerados]) / len(processos_gerados) if len(processos_gerados) > 0 else 0

    # Corrigir o cálculo da ocupação média
    ocupacao_media = (len(processos_gerados) / memoria.tamanho) * 100 if memoria.tamanho > 0 else 0

    # Corrigir o cálculo da taxa de descarte
    taxa_descarte = (len(processos_descartados) / len(processos_gerados)) * 100 if len(processos_gerados) > 0 else 0

    print(f"Tamanho Médio dos Processos Gerados: {tamanho_medio}")
    print(f"Ocupação Média da Memória por Segundo: {ocupacao_media}%")
    print(f"Taxa de Descarte: {taxa_descarte}%")

if __name__ == "__main__":
    main()


