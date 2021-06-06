a, b = input().split()
a, b = [int(x) for x in [a, b]]
if max(a, b) % ((a + b) - max(a, b)) == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
