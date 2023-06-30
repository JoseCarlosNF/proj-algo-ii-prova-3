#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
import logging
from dataclasses import dataclass
from typing import Union

logging.basicConfig(
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    format='%(asctime)s %(levelname)-8s %(message)s',
    handlers=[logging.StreamHandler()],
)


@dataclass
class TreapNode:
    label: str
    priority: int
    left: object = None
    right: object = None


def rotate(node: TreapNode, to: Union['left', 'right']) -> TreapNode:
    """
    Utilizando a técnica trivial de uma váriavel auxilizar faz a rotação para a
    esquerda dos nós, atralados ao nó passado para parametro para função.

    Em ambos os casos precisamos ter em mente uma coisa, em termos de operação
    de rotação estamos tratando de árvores binárias. Ou seja, precisamos
    manter os maiores valores na sub-árvore direita e analogamente os menores
    na esquerda.

    Dito isso seguem os casos de rotação.
    """
    if to == 'left':
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

    elif to == 'right':
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
    return node


def print_treap(root: TreapNode):
    print('(', end='')
    print(f'{root.label}/{root.priority}', end='')
    if root.left:
        print_treap(root.left)
    if root.right:
        print_treap(root.right)
    print(')', end='')


if __name__ == '__main__':
    n1 = TreapNode('a', 7)
    n2 = TreapNode('b', 6)
    n3 = TreapNode('c', 5)
    n4 = TreapNode('d', 4)
    n5 = TreapNode('e', 3)
    n6 = TreapNode('f', 2)
    n7 = TreapNode('g', 1)

    n1.right = n2
    n2.right = n3
    n3.right = n4
    n4.right = n5
    n5.right = n6
    n6.right = n7

    print_treap(n1)
    print()

    """
    INPUT = None

    while INPUT != '0':
        INPUT = input()

        for pair in INPUT.split()[1:]:
            print(pair)
    """
