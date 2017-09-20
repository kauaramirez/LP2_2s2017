from ex02 import contarVogais

def test_ex02():
    print('contarVogais')

assert contarVogais ("abecedario") == {'a':2, 'e':2, 'i':1, 'o':1, 'u':0}
assert contarVogais ("raio") == {'a':1, 'e':0, 'i':1, 'o':1, 'u':0}