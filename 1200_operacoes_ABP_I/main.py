# -*- coding: utf-8 -*-
# Autor: George Felipe de M. Silva 
'''
Arvore binária de busca II 
'''
# Criacao de nos, com no esquedo, direito e o valor do no
class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
# insere um novo nó na arvore
# parametros: raiz e valor a ser inserido
def insert(root, value):
    # Caso a arvore esteja vazia: cria uma nova raiz 
    if root is None:
        return Node(value)
    # Ou compara o valor a ser inserido com a rai e decide
    # qual subarvore inserir o valor
    if value < root.key:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
# busca um valor na arvore
# parametros: raiz da arvore e valor a ser buscado
def search(root, value):
    # caso seja a raiz esteja vazia, ou a chave da raiz
    # seja igual o valor, retorna true 
    if root is None or root.key == value:
        return root is not None
    # ou procura o valor nas subarvores 
    if value < root.key:
        return search(root.left, value)
    return search(root.right, value)

# funcoes resposaveis por percorrer a arvore
# em ordem, pre-ordem, pos-ordem respectivamente. 
# parametros: no e a lista result[] para armazenar os valores
def inorder_traversal(node, result):
    if node is not None:
        inorder_traversal(node.left, result)
        result.append(node.key)
        inorder_traversal(node.right, result)

def preorder_traversal(node, result):
    if node is not None:
        result.append(node.key)
        preorder_traversal(node.left, result)
        preorder_traversal(node.right, result)

def postorder_traversal(node, result):
    if node is not None:
        postorder_traversal(node.left, result)
        postorder_traversal(node.right, result)
        result.append(node.key)

# definindo uma raiz vazia 
root = None

# Bloco de execução principal 
while True:
    try:
        result = []
        entry = input().split()
        
        # caso o tamanho da entrada seja maior que 1
        # significa que temos uma pesquisa ou insercao 
        if len(entry) > 1:
            command, value = entry
            # caso o comando seja "I" temos uma insersao 
            if command == "I":
                root = insert(root, value)
            # se não, temos uma busca
            # onde vemos se o valor existe ou não
            else:
                if search(root, value):
                    print(f'{value} existe')
                else:
                    print(f'{value} nao existe')
        # caso a entrada apenas um elemento, temos uma travessia
        # a depender de qual tipo, temos a chamada da funcao correspondente
        else:
            traversal_type = entry[0]
            if traversal_type == "INFIXA":
                inorder_traversal(root, result)
            elif traversal_type == "PREFIXA":
                preorder_traversal(root, result)
            elif traversal_type == "POSFIXA":
                postorder_traversal(root, result)

            print(' '.join(result))
    # Caso de saída do loop: executar ate o final do arquivo
    except EOFError:
        break