"""punto 1) ritorna vero se "n" è pari, falso se è "n" dispari"""
def is_pari(n) :
    if(n%2 == 0) : 
        return True
    else : 
        return False
"""punto 2) ritorna un numero positivo che li da l'utente se non va bene richiederlo """
def positive_value(n) : 
    if (n >= 1) : 
        return n
    else : 
        while (n < 1) :
        return input("numero non valido")
def main(): 
    result = int((input("scrivi un numero: ")))
    print(is_pari(result))
    print(positive_value(result))


main()
