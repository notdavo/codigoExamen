def conteo_cuatro(num_inicial):
    num_uno = False;
    num_dos = False;
    num_tres = False;
    num_cuatro = False;

    if num_inicial < 1 or num_inicial > 4:
        return False
    else:
        for i in range(1, (num_inicial+1)):
            if i == 1:
                num_uno = True
            elif i == 2:
                num_dos = True
            elif i == 3:
                num_tres = True
            num_cuatro = True
        if num_cuatro == True:
            return True
        else:
            return False


print(conteo_cuatro(1))