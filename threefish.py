#Funções de bitwise:
#Como tivemos problemas de tipagem, utilizamos um tipo próprio para a criptografia
#No caso, um array de 1s e 0s representando bits.
#E, claro, tivemos que criar operadores pra agir sobre esse novo "tipo".

def xor( a, b ):
    result = [0] * 8
    for i in range( 7, -1, -1 ):
        result[i] = a[i] ^ b[i]
    return result

def mod( a, b ):
    result = [0] * 8
    for i in range( 7, -1, -1 ):
        result[i] = a[i] & b[i]
    return result

def add( a, b ):
    result  = [0] * 8
    c = 0
    for i in range( 7, -1, -1 ):
        result[i] = ( a[i] ^ b[i] ) ^ c
        c = ( ( a[i] | c ) & b[i] )  | ( a[i] & ( b[i] | c ) )
    return result

def comp( a ):
    return add( xor( a, [1,1,1,1,1,1,1,1]), [0,0,0,0,0,0,0,1])

def rol( a, b ):
    result = [0] * 8
    q = b % 8
    for i in range( 7, -1, -1 ):
        if ( i - q ) >= 0:
            result[ i - q ] = a[i]
        else:
            result[ 8 + i - q ] = a[i]
    return result

def ror( a, b ):
    result = [0] * 8
    q = b % 8
    for i in range( 7, -1, -1 ):
        if ( i + q ) < 8:
            result[ i + q ] = a[i]
        else:
            result[ i + q - 8 ] = a[i]
    return result

#Funções da criptografia em si:

def permute( v, c = True ):
  p = { True: [2,1,4,7,6,5,0,3], False : [6,1,0,7,2,5,4,3] }
  aux = [ v[i] for i in p[c] ]
  return aux

def mix( x0, x1, j, d, c = True):
    R = [[46,33,17,44,39,13,25,8],
        [36,27,49,9,30,50,29,35],
        [19,14,36,54,34,10,39,56],
        [37,42,39,56,24,17,43,22]] #Mais constantes fixas da descrição do algorítmo

    if( c ):
        y0 = add( x0, x1 )
        y1 = xor( rol( x1, R[j][d%8] ), y0 )
    else:
        y1 = ror( xor(x0, x1), R[j][d%8] )
        y0 = add(x0, comp( y1 ) ) #sub = add( a, ~b )

    return y0, y1

def key_schedule( k, t ):
    ks = []
    kn = to_bit( 0x1BD11BDAA9FC1A22.to_bytes( 8, "big" ) ) #Tem um pq dessa constante em específico no pdf do algorítmo. É basicamente um nothing-up-my-sleeve number.
    for i in range( 7 ): #Nw - 1
        kn = xor( kn[0], k[i])
    t2 = xor( t[1], t[2] )
    t.extend(t2)
    k.extend(kn)
    for i in range( 19 ): #Nr/4 + 1
        s = [None] * 8
        for j in range( 5 ):
            s[j] = k[ ( i + j ) % 9 ]
        s[5] =  add( k[ ( i + 5 ) % 9 ], t[ i % 3 ] )
        s[6] = add( k[ ( i + 6 ) % 9 ], t[ ( i + 1 ) % 3 ] )
        s[7] = add( k[ ( i + 7 ) % 9 ], to_bit( [i] )[0] )
        ks.append( s )
    return ks

#Algoritmo implementado a partir das instruções oficiais, disponiveis em:
#https://www.schneier.com/academic/paperfiles/skein1.3.pdf
#Nossa sugestão para melhorar seria adicionar um timestamp junto a mensagem a ser cifrada, que seria análisado pela aplicação.
#Isso impediria cópias de mensagens sniffadas.

def Threefish( w, k, t, c = True ):
    w = to_bit( w )
    k = to_bit( k )
    t = to_bit( t )
    ks = key_schedule( k, t )
    result = []
    for k in range( 0, len( w ), 8 ):
        block = w[k:k+8]
        if( c ):
            for i in range( 72 ):
                if( ( i % 4 ) == 0 ):
                    for j in range( 8 ):
                        block[j] = add( block[j], ks[int( i/4 )][j] )
                for j in range( 4 ):
                    block[2*j], block[2*j+1] = mix( block[2*j], block[2*j+1], j, i, True )
                block = permute( block, True )
        else:
            for i in range( 71, -1, -1 ):
                block = permute( block, False )
                for j in range( 4 ):
                    block[2*j], block[2*j+1] = mix( block[2*j], block[2*j+1], j, i, False )
                if( ( i % 4 ) == 0 ):
                    for j in range( 8 ):
                        block[j] = add( block[j], comp( ks[int( i/4 )][j] ) )
        result.extend( block )

    if c:
        return from_bit( result )
    else:
        padwan = ""
        for digit in from_bit( result ):
            padwan += chr( digit )
        return pad( padwan, False )

#Abaixo, funções de conversão de string/int para um vetor de bits.
#Por problemas de tipagem, bytes davam erro no endereçamento, strings nas operações, e inteiros no numero de casas.
#(BTW, a função nativa bin() retorna uma string, por isso tive q fazer na mão)

#Esse ficou bonito ;)
def to_bit( data ):
    if( isinstance( data, str ) ):
        data = pad( data )
        data = [ ord( data[i] ) for i in range( len( data ) ) ]
    return [ [0] * ( 8 - len( bin( datum )[2:] ) ) + [ 1 if digit=='1' else 0 for digit in bin( datum )[2:] ] for datum in data ]

#Esse nem tanto =/
def from_bit( data ):
    result = []
    for datum in data:
        c = 0
        for i in range( 8 ):
            c += datum[ 7 - i ] << i
        result.append( c )
    return result

#Padding especial que eu vi por aí mas não lembro o nome
#Adiciona como algarismo de pad o numero de casas cobertas, assim nunca exclui um caractér errado
#(Exceto caso a frase termine com um "1" e seja múltiplo de 8. Mas é bem mais border q acabar com 0, dos pads normais)
def pad( w, c = True):
    result = w * 1
    if c:
        i = 8 - ( len( result ) % 8 )
        if i < 8:
            result += str(i) * i
    else:
        try:
            p = int( result[-1] )
            for i in range( -1, -p - 1, -1 ):
                if( int( result[ i ] ) != p ):
                    raise
            result = result[:-p]
        except:
            return result #Falha no padding

    return result

def example_use( w = "Frase de Exemplo", k = "gurulhu!", t = "oi"):

    print("Plaintext: ", w, "\nKey: ", k, "\nTweak: ", t )
    cy = Threefish( w, k, t )
    print("\nCypher:", [ chr( i ) for i in cy] )

    cy = Threefish( cy, k, t, False )
    print("\nResult: ", cy )

if __name__ == "__main__":
    import sys
    if len( sys.argv ) < 5:
        print("Usage: threefish [plaintext] [key] [tweak] [encript]")
    else:
        if( sys.argv[4] in ["FALSE", "False", "false", "F", "f", "0", "D", "U", "d", "u", 0]  ):
            with open( sys.argv[1] ) as plainfile:
                plaintext = [ int( c ) for c in plainfile.readlines() ]
            print( Threefish( w = plaintext, k = sys.argv[2], t = sys.argv[3], c = False ) )
        else:
            with open( sys.argv[1] ) as plainfile:
                plaintext = plainfile.read()
            [ print( c ) for c in Threefish( w = plaintext, k = sys.argv[2], t = sys.argv[3] ) ]
