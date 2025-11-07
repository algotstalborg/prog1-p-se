from random import randint
def scramble(lista):
    temporär_lista = []
    temporär_lista.extend(lista)
    lista.clear()
    while len(temporär_lista) > 0:
        random_val = randint(0, len(temporär_lista)-1)
        lista.append(temporär_lista[random_val])
        temporär_lista.pop(random_val)

påse = ["test", "test2", "äpple", "test"]
print(len(påse))

kör = True
print("alternativ [A]")

while kör:
    val = input("vad är planen? ")
    if val.lower() in ("alternativ", "a"):
        print("alternativ [A]")
        print("lista [L]")
        print("avsluta [Q]")
        print("lägg till [G]")
        print("Sortera [S]")
        print("Ta bort [T]")
        print("Sök")
        print("Scramble")
    elif val.lower() in ("lista", "l"):
        for i in range(len(påse)):
            print(f"{påse[i]}", end=" ")
        print("")
    elif val.lower() in ("lägg till", "g"):
        if len(påse) <= 10:
            påse.append(input())
        else:
            print("påsen är full testa ta bort något")
    elif val.lower() in ("sortera", "s"):
        påse.sort()
    elif val.lower() in ("avsluta", "q"):
        kör = False
    elif val.lower() in ("ta bort", "t"):
        ta_bort_val = input("vill du ta bort ett värde [v] eller en position [p] eller sista värdet [s]?")
        if ta_bort_val in ("värde", "v"):
            ta_bort_försök = input("vad vill du ta bort?")
            if ta_bort_försök in påse:
                påse.remove(ta_bort_försök)
        elif ta_bort_val in ("position", "p"):
            for i in range(len(påse)):
                print(f"{påse[i]} [{i}]")
            ta_bort_försök = int(input("vilken position vill du ta bort?"))
            if ta_bort_försök <= len(påse)-1: 
                påse.pop(ta_bort_försök)
        elif ta_bort_val in ("sista", "s"):
            if len(påse) > 0:
                påse.pop(len(påse))
    elif val.lower() == "sök":
        sök = input("vad vill du söka ")
        if sök.lower() in påse:
            print(f"hittade {sök}")
    elif val.lower() == "scramble":
        scramble(påse)
    else: 
        print("eeh lär dig stava typ")