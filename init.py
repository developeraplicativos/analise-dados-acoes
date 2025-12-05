"""palavra secreta com _"""
"""após finalizar ser digitada a letra substitui o _"""
"""a qualquer momento a pessoa pode tentar acerta a palavra"""
"""a cada erro um item na forca aparece"""
palavra = 'Halterofilismo'
letras_digitadas = []
contador = 0


def enforcado(valor):
    match valor:
        case 1: 
            print( 'o'.center(20)) 
        case 2: 
            print( 'o'.center(20)) 
            print('/  '.center(20)) 
        case 3: 
            print( 'o'.center(20)) 
            print('/| '.center(20)) 
        case 4: 
            print( 'o'.center(20)) 
            print('/|\\'.center(20)) 
        case 5: 
            print( 'o'.center(20)) 
            print('/|\\'.center(20))
            print('/  '.center(20)) 
    
        case 6: 
            print( 'o'.center(20)) 
            print('/|\\'.center(20))
            print('/ \\'.center(20)) 
 
def procuraLetra(letra):
    if letra not in letras_digitadas:
        letras_digitadas.append(letra)
        if letra in palavra:
            print('ok')
        else:
            enforcado(1 + contador)

    else:
        print('esta letra já foi digitada')



procuraLetra('n')