def plusOne(digits):
    st = ''
    ls = []
    for i in digits:
        st += str(i)
    st = int(st) + 1
    deg = list(str(st))
    for c in range(0, len(deg)):
        ls.append(int(deg[c]))
    return ls


d = [21, 1, 23, 45]
print(plusOne(d))
