class No:
     
     def __init__(self, key, dir, esq):
        self.item: int = key
        self.dir: No = dir
        self.esq: No = esq

class Tree:

    def __init__(self):
        self.root = No(None,None,None)
        self.root = None

    def inserir(self, v):
        novo = No(v,None,None) # cria um novo Nó
        if self.root == None:
            self.root = novo
        else: # se nao for a raiz
            atual = self.root
            while True:
                anterior = atual
                if v <= atual.item: # ir para esquerda
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        return
                # fim da condição ir a esquerda
                else: # ir para direita
                    atual = atual.dir
                    if atual == None:
                            anterior.dir = novo
                            return
                # fim da condição ir a direita

    def remover(self, v):
        if self.root == None:
            print("A árvore está vazia")	
            return False
        if self.root.dir == None and self.root.esq == None:
            if self.root.item == v:
                self.root = None
            return
        else:
            atual = self.root
            anterior = atual
            while True:
                if v == atual.item:
                    if atual.dir == None and atual.esq == None: # no folha
                        if anterior.esq == atual: # verificar para qual lado esta o no que quero remover
                            anterior.esq = None
                        else:
                            anterior.dir = None
                        return
                    if atual.esq != None and atual.dir == None: # tem filho a esquerda 
                        if anterior.item > v: # verificar para qual lado esta o no que quero remover
                            anterior.esq = atual.esq
                        if anterior.item < v:
                            anterior.dir = atual.esq
                        if anterior.item == v: # se a raiz tiver apenas um filho a esquerda
                            self.root = atual.esq
                        return
                    if atual.dir != None and atual.esq == None: # tem filho a direita
                        if anterior.item > v: # verificar para qual lado esta o no que quero remover
                            anterior.esq = atual.dir
                        if anterior.item < v:
                            anterior.dir = atual.dir
                        if anterior.item == v: # se a raiz tiver apenas um filho a direita
                            self.root = atual.dir
                        return
                    if atual.dir != None and atual.esq != None:  # tem os dois filhos
                        # variaveis auxiliares: menorNo, anteriorDoMenor, proximoDir
                        menorNo = atual
                        anteriorDoMenor = menorNo
                        proximoDir = atual.dir
                        if proximoDir.esq == None:
                            menorNo = proximoDir
                            anteriorDoMenor = atual
                            anteriorDoMenor.dir = None
                        else:
                            # buscar o menor nó da subarvore direita
                            while proximoDir.esq != None:
                                anteriorDoMenor = proximoDir
                                menorNo = proximoDir.esq

                                proximoDir = proximoDir.esq
                            anteriorDoMenor.esq = None

                        # substituir o nó atual(o que desejo remover) pelo menor nó da subarvore direita
                        if anterior.item > v:
                            anterior.esq = menorNo
                        if anterior.item < v:
                            anterior.dir = menorNo
                        if anterior.item == v:
                            atual.item = menorNo.item
                        
                        # ajustar os ponteiros do menor nó
                        menorNo.esq = atual.esq
                        menorNo.dir = atual.dir
                        return
                
                # percorrer a arvore
                anterior = atual
                atual = atual.esq if v <= atual.item else atual.dir


    # métodos de exibição de árvores binárias 
    def inOrder(self, atual):
        if atual != None:
            self.inOrder(atual.esq)
            print(atual.item,end=" ")
            self.inOrder(atual.dir)
    
    def preOrder(self, atual):
        if atual != None:
            print(atual.item,end=" ")
            self.preOrder(atual.esq)
            self.preOrder(atual.dir)

    def posOrder(self, atual):
        if atual != None:
            self.posOrder(atual.esq)
            self.posOrder(atual.dir)
            print(atual.item,end=" ")

Tree = Tree()
Tree.inserir(75)
Tree.inserir(60)
Tree.inserir(81)
Tree.inserir(78)
Tree.inserir(94)
Tree.inserir(71)
Tree.inserir(76)
Tree.inserir(93)
Tree.inserir(97)
Tree.inserir(10)

Tree.preOrder(Tree.root)
print("\n")

Tree.remover(75)
Tree.remover(81)
Tree.remover(94)
Tree.remover(71)
Tree.remover(97)
Tree.remover(76)
Tree.remover(60)

Tree.remover(78)
Tree.remover(93)
#Tree.remover(93)

Tree.preOrder(Tree.root)