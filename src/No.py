class No(object):
    def __init__(self, valor):
        self.valor = valor  # valores de entrada
        self.pai = None #ponteiro para o pai
        self.esquerda = None # ponteiro para o filho esquerdo
        self.direita = None #ponteiro para o filho direito
        self.cor = 1 # 1 . vermelho, 0 . preto