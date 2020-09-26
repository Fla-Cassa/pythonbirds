class Pessoa:
    # Metodo nada mais é do que uma função, que pertence a uma classe
    # e portanto sempre está conectada/atrelada a um objeto. Portanto sempre
    # deve ser declarada em um primeiro parametro o objeto a ser recebido.
    def __init__(self, * filhos, nome=None, idade=25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'


if __name__ == '__main__':
    giovanna = Pessoa(nome='giovanna')
    flavio = Pessoa(nome='flavio')
    print(Pessoa.cumprimentar(flavio))
    print(id(giovanna))
    print(giovanna.cumprimentar())
    print(giovanna.nome)
    print(giovanna.idade)
    for filho in giovanna.filhos:
        print((giovanna.filhos))
