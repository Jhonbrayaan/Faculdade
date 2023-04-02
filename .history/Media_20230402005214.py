nome = input("Escreva o nome do aluno: ")
matéria = input("Escreva a matéria: ")

nota1 = float(input("Escreva a nota 1 da prova: "))
nota2 = float(input("Escreva a nota 2 da prova: "))

media =  (nota1 + nota2) / 2
print("A média do aluno é: ", media)
if media >= 6:
    print("APROVADO")
elif    