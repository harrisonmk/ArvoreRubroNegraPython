from No import No

class ArvoreRubroNegra(object):
    
    def __init__(self):
        self.TNULL = No(0)
        self.TNULL.cor = 0
        self.TNULL.esquerda = None
        self.TNULL.direita = None
        self.raiz = self.TNULL


    def __pre_order_ajudante(self, node):
        if node != self.TNULL:
            print(node.valor, " ", end="")
            self.__pre_order_ajudante(node.esquerda)
            self.__pre_order_ajudante(node.direita)

    def __in_order_ajudante(self, node):
        if node != self.TNULL:
            self.__in_order_ajudante(node.esquerda)
            print(node.valor, " ", end="")
            self.__in_order_ajudante(node.direita)

    def __post_order_ajudante(self, node):
        if node != self.TNULL:
            self.__post_order_ajudante(node.esquerda)
            self.__post_order_ajudante(node.direita)
            print(node.valor, " ", end="")

 
    def __busca_arvore_ajudante(self, node, chave):
        if node == TNULL or chave == node.valor:
            return node

        if chave < node.valor:
            return self.__busca_arvore_ajudante(node.esquerda, chave)
        return self.__busca_arvore_ajudante(node.direita, chave)

    def __conserta_exclusao(self, x):
        while x != self.raiz and x.cor == 0:
            if x == x.pai.esquerda:
                s = x.pai.direita
                if s.cor == 1:
                    # case 3.1
                    s.cor = 0
                    x.pai.cor = 1
                    self.left_rotate(x.pai)
                    s = x.pai.direita

                if s.esquerda.cor == 0 and s.direita.cor == 0:
                    # case 3.2
                    s.cor = 1
                    x = x.pai
                else:
                    if s.direita.cor == 0:
                        # case 3.3
                        s.esquerda.cor = 0
                        s.cor = 1
                        self.rotacaoDireita(s)
                        s = x.pai.direita

                    # case 3.4
                    s.cor = x.pai.cor
                    x.pai.cor = 0
                    s.direita.cor = 0
                    self.rotacaoEsquerda(x.pai)
                    x = self.raiz
            else:
                s = x.pai.esquerda
                if s.cor == 1:
                    # case 3.1
                    s.cor = 0
                    x.pai.cor = 1
                    self.rotacaoDireita(x.pai)
                    s = x.pai.esquerda

                if s.direita.cor == 0 and s.direita.cor == 0:
                    # case 3.2
                    s.cor = 1
                    x = x.pai
                else:
                    if s.esquerda.cor == 0:
                        # case 3.3
                        s.direita.cor = 0
                        s.cor = 1
                        self.left_rotate(s)
                        s = x.pai.esquerda 

                    # case 3.4
                    s.cor = x.pai.cor
                    x.pai.cor = 0
                    s.esquerda.cor = 0
                    self.right_rotate(x.pai)
                    x = self.raiz
        x.color = 0

    def __rb_transplante(self, u, v):
        if u.pai == None:
            self.raiz = v
        elif u == u.pai.esquerda:
            u.pai.esquerda = v
        else:
            u.pai.direita = v
        v.pai = u.pai

    def __exluir_node_ajudante(self, node, chave):
        
        z = self.TNULL
        while node != self.TNULL:
            if node.valor == chave:
                z = node

            if node.valor <= chave:
                node = node.direita
            else:
                node = node.esquerda

        if z == self.TNULL:
            print ("Nao foi possivel encontrar a chave na arvore")
            return

        y = z
        y_original_color = y.cor
        if z.esquerda == self.TNULL:
            x = z.direita
            self.__rb_transpante(z, z.direita)
        elif (z.direita == self.TNULL):
            x = z.esquerda
            self.__rb_transpante(z, z.esquerda)
        else:
            y = self.minimo(z.direita)
            y_original_color = y.cor
            x = y.direita
            if y.pai == z:
                x.pai = y
            else:
                self.__rb_transpante(y, y.direita)
                y.direita = z.direita
                y.direita.parent = y

            self.__rb_transplante(z, y)
            y.esquerda = z.esquerda
            y.esquerda.pai = y
            y.cor = z.cor
        if y_original_color == 0:
            self.__conserta_exclusao(x)

    
    def  __conserta_insercao(self, k):
        while k.pai.cor == 1:
            if k.pai == k.pai.pai.direita:
                u = k.pai.pai.esquerda # tio
                if u.cor == 1:
                    # case 3.1
                    u.cor = 0
                    k.pai.cor = 0
                    k.pai.pai.cor = 1
                    k = k.pai.pai
                else:
                    if k == k.pai.esquerda:
                        # case 3.2.2
                        k = k.pai
                        self.rotacaoDireita(k)
                    # case 3.2.1
                    k.pai.cor = 0
                    k.pai.pai.cor = 1
                    self.rotacaoEsquerda(k.pai.pai)
            else:
                u = k.pai.pai.direita # tio

                if u.cor == 1:
                   
                    u.cor = 0
                    k.pai.cor = 0
                    k.pai.pai.cor = 1
                    k = k.pai.pai 
                else:
                    if k == k.pai.direita:
                        
                        k = k.pai
                        self.rotacaoEsquerda(k)
                    
                    k.pai.cor = 0
                    k.pai.pai.cor = 1
                    self.rotacaoDireita(k.pai.pai)
            if k == self.raiz:
                break
        self.raiz.cor = 0
    

    def preorder(self):
        self.__pre_order_ajudante(self.raiz)

   
    def inorder(self):
        self.__in_order_ajudante(self.raiz)

    
    def postorder(self):
        self.__post_order_ajudante(self.raiz)



    # rotacao à esquerda do nó x
    def rotacaoEsquerda(self, x):
        y = x.direita
        x.direita = y.esquerda
        if y.esquerda != self.TNULL:
            y.esquerda.pai = x

        y.pai = x.pai
        if x.pai == None:
            self.raiz = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y
        y.esquerda = x
        x.pai = y

    # rotacao à direita do nó x
    def rotacaoDireita(self, x):
        y = x.esquerda
        x.esquerda = y.direita
        if y.direita != self.TNULL:
            y.direita.pai = x

        y.pai = x.pai
        if x.pai == None:
            self.raiz = y
        elif x == x.pai.direita:
            x.pai.direita = y
        else:
            x.pai.esquerda = y
        y.direita = x
        x.pai = y


    def buscaArvore(self, k):
        return self.__busca_arvore_ajudante(self.raiz, k)


    def inserir(self, chave):
        
        node = No(chave)
        node.pai = None
        node.valor = chave
        node.esquerda = self.TNULL
        node.direita = self.TNULL
        node.cor = 1 

        y = None
        x = self.raiz

        while x != self.TNULL:
            y = x
            if node.valor < x.valor:
                x = x.esquerda
            else:
                x = x.direita

        # y eh pai de x
        node.pai = y
        if y == None:
            self.raiz = node
        elif node.valor < y.valor:
            y.esquerda = node
        else:
            y.direita = node

        # se o novo nó for um nó raiz, simplesmente retorne
        if node.pai == None:
            node.cor = 0
            return

        
        if node.pai.pai == None:
            return

        
        self.__conserta_insercao(node)
 

    # encontre o nó com a chave minima
    def minimo(self, node):
        while node.esquerda != self.TNULL:
            node = node.esquerda
        return node

    # encontra o nó com a chave máxima
    def maximo(self, node):
        while node.direita != self.TNULL:
            node = node.direita
        return node

    # encontra o sucessor de um determinado nó
    def sucessor(self, x):
     
        if x.direita != self.TNULL:
            return self.maximo(x.direita)

       
        y = x.pai
        while y != self.TNULL and x == y.direita:
            x = y
            y = y.pai
        return y

    # encontra o antecessor de um determinado nó
    def antecessor(self, x):
        
        if (x.esquerda != self.TNULL):
            return self.maximo(x.esquerda)

        y = x.pai
        while y != self.TNULL and x == y.esquerda:
            x = y
            y = y.pai

        return y

    
    


    def get_raiz(self):
        return self.raiz

    # delete the node from the tree
    def exluir_no(self, data):
        self.__exluir_node_ajudante(self.raiz, data)



    

    
