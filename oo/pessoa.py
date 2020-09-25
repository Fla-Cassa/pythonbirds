class Pessoa:
    # Metodo nada mais é do que uma função, que pertence a uma classe
    # e portanto sempre está conectada/atrelada a um objeto. Portanto sempre
    # deve ser declarada em um primeiro parametro o objeto a ser recebido.
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Giovanna')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Flávio'
    print(p.nome)
    print(p.idade)
