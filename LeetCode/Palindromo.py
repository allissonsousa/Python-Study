"""Verificar se um numero é um palindromo"""


def isPalindrome(num):
    n = str(num)
    ac = 0
    frase = ''
    for i in range(len(n), 0, -1):
        ac = i - 1
        frase += n[ac]
    if frase == n:
        return True
    else:
        return False


numeros = 121
print(isPalindrome(numeros))
