#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class TreapNode:
    label: str
    priority: int
    left: object = None
    right: object = None


def rotate_left(node):
    """
    Utilizando a técnica trivial de uma váriavel auxilizar faz a rotação para a
    esquerda dos nós, atralados ao nó passado para parametro para função.

    Em ambos os casos precisamos ter em mente uma coisa, em termos de operação
    de rotação estamos tratando de árvores binárias. Ou seja, precisamos
    manter os maiores valores na sub-árvore direita e analogamente os menores
    na esquerda.

    Dito isso seguem os casos de rotação.
    """
    right = node.right   # obtem o right
    x = node.right.left   # obtem o x

    right.left = node   # raiz desce p/ esquerda
    node.right = x   # x sobe pro lugar do right
    """
                  Sai daqui:              Vai pra cá:

                      __++__                 right
                     /      \               /     \
                 left        right         ++      y
                             /   \                / \
                            x     y           left   x

        Sabendo que o pivô será o nó em questão, devemos move-lo para
        ocupar o lugar do nó a sua esquerda. Para isso uma reação em cadeia
        deve ser realizada, afim de manter as propriedades da árvore
        binária.

        A raiz(++) deve descer, para a esquerda, e o seu filhor
        maior(direito) subir para ser a nova raiz.

        Na sub-árvore direita, com a subida do nó right, precisamos de
        outro nó para ocupa-lo, nitidamente, para manter as
        caracteristicas, subiremos o nó y.

        Agora precisamos de alguém para ocupar o lugar de x, que foi
        promovido a filho maior de y, e como sabemos left é o menor valor
        da árvore, logo poderá ser encaixado como filho menor de y,
        subistituindo o x na estrutura original.
    """
    return right


def rotate_right(node):
    left = node.left   # obtem o left
    y = node.left.right   # obtem o y

    left.right = node   # raiz desce p/ direita
    node.left = y   # y é definido como filho menor da raiz original
    """
                  Sai daqui:              Vai pra cá:

                      __++__                       left
                     /      \                     /    \
                 left        right               x     ++
                 /  \                                 /  \
                x    y                               y    right

        Primeiramente iremos descer a raiz, nesse caso para o lado direito,
        com isso left será a nova raiz.

        Em seguida, precisamos de um novo filho menor para a raiz original.
        E então, por caracteristicas da árvore binária o nó y é definido,
        visto que entre as duas opções disponíveis (x, y) é a que se
        encaixaria na definição desse nó; que deve ser maior que left e
        menor que a raiz original(++).
    """
    return left


def insert(root, node_to_insert):
    """
    A parte mais importante do código, onde realmente a mágica acontece.

    Nos blocos a seguir, são realizadas as decisões que iram nutrir as
    sub-árvores.

    Levando em consideração incialmente o label do nó, e posteriormente sua
    prioridade.
    """
    # Caso BASE de inserção. Sempre que o nó for vázio atribui o nó de inserção
    if root is None:
        return node_to_insert

    # Se o LABEL for MENOR, mandar pra DIREITA
    if node_to_insert.label > root.label:
        root.right = insert(root.right, node_to_insert)

        # se a prioridade do nó atual for menor que o seu filho direito,
        # rotacionar a esquerda.
        if root.priority < root.right.priority:
            root = rotate_left(root)

    # Se o LABEL for MAIOR, mandar pra ESQUERDA
    else:
        root.left = insert(root.left, node_to_insert)

        # se a prioridade do nó atual for menor que o seu filho esquerdo,
        # rotacionar a direita.
        if root.priority < root.left.priority:
            root = rotate_right(root)
    return root


def print_treap(root):
    print('(', end='')
    if root.left:
        print_treap(root.left)
    print(f'{root.label}/{root.priority}', end='')
    if root.right:
        print_treap(root.right)
    print(')', end='')


def run(INPUT: list):
    if len(INPUT) >= 3:
        root = TreapNode(*INPUT[1])
        node = TreapNode(*INPUT[2])
        new_root = insert(root, node)

        for pair in INPUT[3:]:
            node = TreapNode(*pair)
            new_root = insert(new_root, node)
        print_treap(new_root)
        print()
    else:
        return



if __name__ == '__main__':
    while True:
        INPUT = [_ for _ in map(lambda ent: ent.split('/'), input().split())]

        if INPUT == [['0']]:
            break
        elif INPUT == []:
            continue
        else:
            run(INPUT)
