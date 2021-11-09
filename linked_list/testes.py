from linked_list import LinkedList


minha_linked_list = LinkedList()
minha_linked_list.inserir_node(5)
minha_linked_list.inserir_node(6)
minha_linked_list.inserir_node(2)
minha_linked_list.inserir_node(9)

print(minha_linked_list)
print(minha_linked_list.invertida())
print(minha_linked_list.tamanho())
print(minha_linked_list.posicao(6))


outra_linked_list = LinkedList()
outra_linked_list.inserir_node('Python')
outra_linked_list.inserir_node('Java')
outra_linked_list.inserir_node('Kotlin')

print(outra_linked_list)
print(outra_linked_list.tamanho())
print(outra_linked_list.tem('JavaScript'))


minha_linked_list.cortar_cabeca()
print(minha_linked_list)


outra_linked_list.cortar_rabo()
print(outra_linked_list)


minha_linked_list.deletar(6)
print(minha_linked_list)
