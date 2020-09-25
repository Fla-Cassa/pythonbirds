class Pessoa:
    # Metodo nada mais é do que uma função, que pertence a uma classe
    #e portanto sempre está conectada/atrelada a um objeto. Portanto sempre
    # deve ser declarada em um primeiro parametro o objeto a ser recebido.
    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())

