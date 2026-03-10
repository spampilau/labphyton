"""punto 1) ritorna vero se "n" è pari, falso se è "n" dispari"""
def is_pari(n) :
    if(n%2 == 0) : 
        return True
    else : 
        return False

def main(): 
    result = int((input("scrivi un numero: ")))
    print(is_pari(result))


main()