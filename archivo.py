if __name__ == "__main__":

    paisesPop = []
    with open('TextFiles/paises.csv.mod.mod', 'r') as p:
        reader = p.read().splitlines()
        reader.pop(0)
        for i in reader:
            linea = i.split(',')
            paisesPop.append([float(linea[31]),str(linea[0])])
    ordenado = sorted(paisesPop, reverse=True) #ordenado de mayor a menor

    print()
    print("Lo 5 paises más poblados: ","\n1.- ",ordenado[1],"\n2.- ",ordenado[2],"\n3.- ",ordenado[3],"\n4.- ",ordenado[4],"\n5.- ",ordenado[5])
    print()

    paisesEfecto = []
    paises = []
    with open('TextFiles/efecto.csv','r') as f:
        r = f.read().splitlines()
        r.pop(0)
        for j in r:
            lin = j.split(',')
            paisesEfecto.append([float(lin[2]),int(lin[1]),str(lin[0])])

        for i in paisesEfecto:
            if i[1] == 2010:
                paises.append(i)
        order = sorted(paises, reverse=True) #ordenado de mayor a menor
    print()
    print("los paises 5 paises mas productores de gases de invernadero:", "\n1.-", order[0], "\n2.-", order[3], "\n3.-",order[6], "\n4.-", order[9], "\n5.-", order[12])
    print()