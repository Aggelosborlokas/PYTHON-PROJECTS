def paragontes():
    number = int(input('ΕΙΣΑΓΕΤΕ ΑΚΕΡΑΙΟ ΑΡΙΘΜΟ:'))
    i = 2
    factors = []
    while i <= number:
        if (number % i) == 0:
            factors.append(i)
            number = number / i
        else:
            i = i + 1
    return factors


b = paragontes()
x = 0
j = 1
y = len(b)
while x <= (y-2):
    if b[x] == b[x+1]:
        j += 1
    elif b[x+1] > b[x]:
        print('(', b[x], '**', j, ')', end='')
        j = 1
    x += 1
print('(', b[x], '**', j, ')', end='')
