dic = {
    "musicas": [
        {'nome': 'Hey Jude', 'banda': 'Beatles'},
        {'nome': 'November Rain', 'banda': "Guns n' Roses"},
        {'nome': 'How Deep Is Your Love', 'banda': 'Bee Gees'}
    ],
    "filmes": {
        'X-men': ["Wolverine", "Xavier", "Tempestade", "Vampira"],
        "Avengers": ["Homem de Ferro", "Hulk", "Thanos", "Capitão América", "Thor"],
        "Star Wars": ["Luke", "Leia", "Darth Vader", "Chewbaca", "Han Solo"]
    }
}


def func1(a, b, c, d):
    for x in a:
        if x[b] == d:
            return x[c]
    return "naosei"


def sera_que_funk_eh_musica():
    return "funk" in dic["musicas"]

# print("Homem de Ferro" in dic["musicas"][2])
# print(func1(dic["musicas"], "banda", "nome", "Guns n' Roses") == "November Rain")
# print("Hey Jude" in dic["musicas"]["Beatles"])
# print("Thor" in dic["filmes"]["Avengers"])
# print("November Rain" == dic["musicas"][1]["banda"])
# print(func1(dic["filmes"], 1, 2, "Homem de Ferro"))
# print(func1(dic, ["filmes"], ["musicas"], "Avengers", "Capitão América"))
# print(dic[dic] + dic[dic[dic]]])
# print(dic["filmes"]["X-men"][3] == "Vampira")
# print("Han Solo" in dic["jogos"]["Star Wars"])

def analisa_string(string):
    string = string.upper()
    if string[0] == 'B' and string[-1] == 'A':
        return True
    return False

# print(analisa_string('Banana banana'))

"""Considerando a a sequência numérica a seguir (11, 18, 25, 32, 39... )faça uma função que recebe como entrada uma posição e devolve qual o valor do número naquela posição, considerando a sequência numérica apresentada.
Ex:
print_valor(x=1) retornará 11; print_valor(x=6) retornará 46; print_valor(x=254) retornará 1.782;
print_valor(x=3.542.158) retornará 24.795.110;"""


def qual_valor(posicao):
    valor = 11
    if int(posicao) == 1:
        return valor
    for x in range(1, int(posicao)):
        valor += 7
    return valor

print(qual_valor(254))
print(qual_valor(6))

