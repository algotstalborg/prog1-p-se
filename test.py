def tabortsistavärdet(lista):
    lista.pop(len(lista))

kör = True

påse = []

while kör:
    val = input("vad är planen? ")
    if val.lower() in ("alternativ", "a"):
        print("alternativ [A]")
        print("lista [L]")
        print("avsluta [Q]")
        print("lägg till [G]")
        print("Sortera [S]")
        print("Ta bort [T]")
    elif val.lower() in ("lista", "l"):
        for i in range(len(påse)):
            print(f"{påse[i]}", end="")
            print("")
    elif val.lower() in ("lägg till", "g"):
        påse.append(input())
    elif val.lower() in ("sortera", "s"):
        påse.sort()
    elif val.lower() in ("avsluta", "q"):
        kör = False
    elif val.lower() in ("ta bort", "t"):
        ta_bort_val = input("vill du ta bort ett värde [v] eller en position [p] eller sista värdet [s]?")
        if ta_bort_val in ("värde", "v"):
            påse.remove(input("vad vill du ta bort?"))
        elif ta_bort_val in ("position", "p"): 
            påse.pop(int(input("vilken position vill du ta bort? (från 1)"))-1)
        elif ta_bort_val in ("sista", "s"):
            tabortsistavärdet(påse)
    else: print("eeh lär dig stava typ")