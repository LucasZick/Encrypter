import random


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789,.!@#$%*()_-+=[]{}ãõáéíóúÃẼÁÉÍÓÚâêÂÊ '
chars_pointer = chars

dictKey = {}


def getKey(chars=chars, chars_pointer=chars_pointer):
    key = ''
    for i in chars:
        selectedChar = random.choice(chars_pointer)
        chars_pointer = chars_pointer.replace(selectedChar, '')
        key = key + selectedChar

    for i in range(len(chars)):
        dictKey[chars[i]] = key[i]


    return dictKey, key

def Encrypt(inp, dictKey=dictKey):
    output = ''
    key = getKey()
    for i in inp:
        output = output + dictKey.get(i)
    return output, key[1]

def Uncrypt(key, text):
    output = ''
    dictUncrypt = {}
    for i in range(len(chars)):
        dictUncrypt[key[i]] = chars[i]
    for i in text:
        output = output+dictUncrypt.get(i)
    return output

if __name__ == "__main__":
    while True:
        opt = int(input('___________________________________________________'+
        '\n1 - CRIPTOGRAFAR // 2 - DESCRIPTOGRAFAR // 3 - SAIR\n_'))
        if opt == 1:
            inp = input('Digite o texto a ser criptografado: ')
            retorno = (Encrypt(inp=inp))
            print(f'FRASE CRIPTOGRAFADA: {retorno[0]}\nKEY DA CRIPTOGRAFIA: {retorno[1]}')
        elif opt == 2:
            keyUncrypt = input('Cole aqui sua chave de criptografia: ')
            inpUncrypt = input('Cole aqui o seu texto criptografado: ')
            print(f'\nTexto original: {Uncrypt(keyUncrypt,inpUncrypt)}')
        else:
            break




