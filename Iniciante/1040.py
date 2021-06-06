n1, n2, n3, n4 = input().split()
n1, n2, n3, n4 = [float(x) for x in [n1, n2, n3, n4]]
media = ((2 * n1) + (3 * n2) + (4 * n3) + n4) / 10
print('Media: {:.1f}'.format(media))
if media >= 7:
    print('Aluno aprovado.')
if media < 5:
    print('Aluno reprovado.')
if 5 <= media <= 6.9:
    print('Aluno em exame.')
    nota = float(input())
    print('Nota do exame: {}'.format(nota))
    media2 = (nota + media) / 2
    if media2 >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(media2))
