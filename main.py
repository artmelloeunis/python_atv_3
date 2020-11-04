primeiro_num = int(input("Primeiro número: "))
segundo_num = int(input("Segundo número : "))
terceiro_num = int(input("Terceiro número: "))

menor_num = primeiro_num

if(segundo_num < menor_num):
    menor_num = segundo_num
if(terceiro_num < menor_num):
    menor_num = terceiro_num

print("O menor número é:", menor_num)