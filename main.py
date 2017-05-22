from supplies import Supplies


if __name__  == '__main__':
    teste = Supplies()
    teste2=teste.getBlockList(teste.getBinString("hello World!!"))
    print(teste2)
