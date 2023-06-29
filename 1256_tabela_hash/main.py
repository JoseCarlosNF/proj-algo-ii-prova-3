# -*- encodign:
def func_dispersao(x: int, tamanho_tabela: int = 13) -> int:
    return x % tamanho_tabela


def imprime_resultado(tabela):
    for i_chave in range(len(tabela)):
        print(i_chave, end=' -> ')

        for valor in tabela[i_chave]:
            print(valor, end=' -> ')
        print('\\')


if __name__ == '__main__':
    # obtem os dados de qdte. de testes
    for _ in range(int(input())):

        # obtem tam. da tabela e qtde. de chaves que devem ser armazenadas
        tamanho_tabela, qtde_chaves = map(int, input().split())

        # instancia uma lista de listas, estrutura base p/ tabela
        tabela = [[] for _ in range(tamanho_tabela)]

        # obtem os valores que devem ser armazenados na tabela
        valores = map(int, input().split())

        # para cada valor que deve ser aramazenado, é aplicado a função de
        # dispersão. E o resultado é o índice da lista dentro da tabela, que
        # será utilizado para incrementar a lista, do respectivo índice.
        for valor in valores:
            tabela[func_dispersao(valor, tamanho_tabela)].append(valor)

        if _ > 0:
            print()
        imprime_resultado(tabela)
