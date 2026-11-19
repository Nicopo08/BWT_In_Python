<<<<<<< HEAD
def trasformazione(str1):  
    str1+= "$"
    lung = len(str1)
    rotazioni = []
    for i in range(lung):
    
        rotazione = str1[i:] + str1[:i]
        rotazioni.append(rotazione)

    rotazioni.sort()
    bwt = ""
    for rot in rotazioni:
        bwt += rot[-1]
=======
def trasformazione(str1):  
    str1+= "$"
    lung = len(str1)
    rotazioni = []
    for i in range(lung):
    
        rotazione = str1[i:] + str1[:i]
        rotazioni.append(rotazione)

    rotazioni.sort()
    bwt = ""
    for rot in rotazioni:
        bwt += rot[-1]
>>>>>>> 47458654b71e112f99eaf58ab8b26a76dae394f3
    return bwt