from node import Node


class LinkedList:

    def __init__(self):
        self.head = None


    def inserir_node(self, valor):
        # Lembrando: um node tem um valor e talvez um pointer pra o próximo node
        novo_node = Node(valor)

        # Primeira vez
        if self.head is None:
            self.head = novo_node
        # Valor do novo node é menor que o valor do head
        elif self.head.value >= valor:
            novo_node.next = self.head
            self.head = novo_node
        # Valor do novo node é maior que o valor do head
        else:
            # O atual é o próximo node da linked list
            atual = self.head.next
            # O anterior é o head
            anterior = self.head
            
            # Enquanto atual não for None e o valor do novo node for maior que o valor do atual
            while (atual is not None) and (valor > atual.value):
                # Avança na linked list
                anterior = atual
                atual = atual.next

            # Próximo node do novo node é o atual
            novo_node.next = atual
            # Próximo node do anterior é o novo node
            anterior.next = novo_node
            # anterior -> novo_node -> atual


    def __str__(self):
        if not self.head:
            return 'Não tem head'

        string = ""
        atual = self.head

        while atual:
            string += str(atual.value) + " -> "
            atual = atual.next

        return string + "FIM"


    def invertida(self):
        if not self.head:
            return 'Não tem head'

        valores = str(self).split(' -> ')
        valores.pop()
        valores.reverse()

        string = ""
        for valor in valores:
            string += valor + ' -> '

        return string + 'FIM'
    
    
    def tamanho(self):
        if not self.head:
            return 'Não tem cabeça'

        valores = str(self).split(' -> ')
        valores.pop()
        
        return len(valores)


    def posicao(self, alvo):
        if not self.head:
            return 'Não tem head'

        atual = self.head
        
        for c in range(self.tamanho()):
            if atual.value == alvo:
                return c + 1
            atual = atual.next

    
    def tem(self, alvo):
        if not self.head:
            return 'Não tem head'

        atual = self.head
        
        for _ in range(self.tamanho()):
            if atual.value == alvo:
                return True
            atual = atual.next

        return False


    def cortar_cabeca(self):
        if not self.head:
            return 'Não tem head'

        self.head = self.head.next


    def cortar_rabo(self):
        if not self.head:
            return 'Não tem head'

        atual = self.head

        while atual.next.next:
            atual = atual.next
        
        atual.next = None
        
        
    def deletar(self, alvo):
        if self.head is None:
            return False

        elif self.head.value == alvo:
            self.head = self.head.next
            return True

        else:
            atual = self.head.next
            anterior = self.head

            while (atual is not None) and (alvo > atual.value):
                anterior = atual
                atual = atual.next

            if atual is not None and atual.value == alvo:
                anterior.next = atual.next
                return True
            else:
                return False
