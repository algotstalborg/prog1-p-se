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

    elif val.lower() in ("lista", "l"):
        for i in range(len(påse)):
            print(f"{påse[i]}", end=" ")
            print("")
    elif val.lower() in ("lägg till", "g"):
        påse.append(input())
    elif val.lower() in ("sortera", "s"):
        påse.sort()
    elif val.lower() in ("avsluta", "q"):
        kör = False