# -*- coding: utf-8 -*-
# Autor: George Felipe de M. Silva 
'''
Implementação de uma arvore binaria de busca
'''
# Criacao de nos, com no esquedo, direito e o valor do no
class TreeNode:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

#Criacao da arvore 
class BinaryTree:
    def __init__(self):
        #Criancao da raiz 
        self.root = None

    #Metodo de insersao de valores
    def insert(self, value):
        #caso a arvore esteja vazia, insere o valor e define como raiz
        if self.root is None:
            self.root = TreeNode(value)
        else:
            #Se não, invoca a funcao recursiva de insersao
            self._insert_recursive(self.root, value)
    # Insersao recursiva, recebe o no a ser inserido e seu valor
    def _insert_recursive(self, node, value):
        #Compara o valor, do no a ser inserido com o no atual
        # e define a subarvore a inserir
        if value <= node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    # Chamada do metodo de pre-ordem
    def list_pre_order(self):
        return self._list_pre_order_recursive(self.root)

    #implementacao pre-ordem
    def _list_pre_order_recursive(self, node):
        if node is None:
            return []
        result = [node.value]
        result.extend(self._list_pre_order_recursive(node.left))
        result.extend(self._list_pre_order_recursive(node.right))
        return result
    # chamada do metodo em ordem 
    def list_in_order(self):
        return self._list_in_order_recursive(self.root)

    #implementacao em ordem
    def _list_in_order_recursive(self, node):
        if node is None:
            return []
        result = self._list_in_order_recursive(node.left)
        result.append(node.value)
        result.extend(self._list_in_order_recursive(node.right))
        return result

    # Chamada do metodo pos-ordem
    def list_post_order(self):
        return self._list_post_order_recursive(self.root)
    
    #implementacao pos-ordem
    def _list_post_order_recursive(self, node):
        if node is None:
            return []
        result = self._list_post_order_recursive(node.left)
        result.extend(self._list_post_order_recursive(node.right))
        result.append(node.value)
        return result

# funcao aux, recebe uma lista de valores e um rotulo
# depois converte em string no formato solicitado pela plataforma
def show_result(results, label):
    str_values = ' '.join(map(str, results))
    return f'{label}: {str_values}'

# instanccciando a arvore e chamando os métodos de saida 
def solve_tree(values):
    tree = BinaryTree()
    for value in values:
        tree.insert(value)
    print(show_result(tree.list_pre_order(), 'Pre.'))
    print(show_result(tree.list_in_order(), 'In..'))
    print(show_result(tree.list_post_order(), 'Post'))
    print()

# laço de execucao do algoritmo
def run():
    # solicita o numero de casos de teste
    n = int(input())
    # para cada caso le o valor e resolve a arvore. 
    for i in range(n):
        c = int(input())
        line = input()
        values = list(map(int, line.split(' ')))
        print(f'Case {i + 1}:')
        solve_tree(values)


run()