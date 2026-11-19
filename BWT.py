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
    return bwt