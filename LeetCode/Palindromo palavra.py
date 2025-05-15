def isPalindrome(num):
    l = str(num)
    frase = ''
    for i in range(len(l), -1, 1):
        frase += l[i]
    if frase == l:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
print(isPalindrome(num))