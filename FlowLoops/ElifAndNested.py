# if condition:
#   Body of if
#elif condition:
#   Body of elif
#else:
#   Body of else

a = -3.4
if a > 0:
    print("esse número é positivo")
elif a == 0:
    print("isso é zero")
else:
    print("esse número é negativo")


age = 10
if age > 18:
    if age > 60:
        print("Conta cidadão senior")
    else:
        print("Conta padrão aberta")
else:
    print("Sem permissão")