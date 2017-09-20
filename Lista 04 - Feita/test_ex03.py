def media_aluno(nome,n1,n2):
    dicionario = {}
    media = (n1+n2)/2
    dicionario[nome] = media
    return dicionario

def test_media():
    print('media')
    assert media_aluno('thiago', 10, 5) == {'thiago': 7.5}