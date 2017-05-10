
def Refining(Toofine, Liabfine):

    if (Toofine >= 0 and Toofine < 100000000):
        tooja = 1
    elif (Toofine > 100000000 and Toofine < 50000000):
        tooja = 2
    elif (Toofine > 50000000 and Toofine < 100000000):
        tooja = 3
    elif (Toofine > 100000000 and Toofine < 500000000):
        tooja = 4
    elif (Toofine > 500000000 and Toofine < 1000000000):
        tooja = 5
    elif (Toofine > 1000000000 and Toofine < 3000000000):
        tooja = 6
    elif (Toofine > 3000000000 and Toofine < 6000000000):
        tooja = 7
    elif (Toofine > 6000000000 and Toofine < 10000000000):
        tooja = 8
    elif (Toofine > 10000000000):
        tooja = 9
    elif (Toofine <= 0 and Toofine > -100000000):
        tooja = -1
    elif (Toofine < -100000000 and Toofine > -50000000):
        tooja = -2
    elif (Toofine < -50000000 and Toofine > -100000000):
        tooja = -3
    elif (Toofine < -100000000 and Toofine > -500000000):
        tooja = -4
    elif (Toofine < -500000000 and Toofine > -1000000000):
        tooja = -5
    elif (Toofine < -1000000000 and Toofine > -3000000000):
        tooja = -6
    elif (Toofine < -3000000000 and Toofine > -6000000000):
        tooja = -7
    elif (Toofine < -6000000000 and Toofine > -10000000000):
        tooja = -8
    elif (Toofine < -10000000000):
        tooja = -9


    if (Liabfine >= 0 and Liabfine < 100000000):
        liab = 1
    elif (Liabfine > 100000000 and Liabfine < 500000000):
        liab = 2
    elif (Liabfine > 500000000 and Liabfine < 1000000000):
        liab = 3
    elif (Liabfine > 1000000000 and Liabfine < 5000000000):
        liab = 4
    elif (Liabfine > 5000000000 and Liabfine < 10000000000):
        liab = 5
    elif (Liabfine > 10000000000 and Liabfine < 30000000000):
        liab = 6
    elif (Liabfine > 30000000000 and Liabfine < 50000000000):
        liab = 7
    elif (Liabfine > 50000000000 and Liabfine < 100000000000):
        liab = 8
    elif (Liabfine > 100000000000):
        liab = 9
    return liab, tooja