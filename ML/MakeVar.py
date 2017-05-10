import numpy as np
from sklearn import preprocessing

def MakeVar1(data, n):
    Var = []
    FinalData = []

    x_data = data[3:-1].astype(np.float32)  # 3행 6열

    basis = x_data[0]
    #x_data = preprocessing.normalize(x_data[1:], norm='l2')
    x_data = x_data[1:]
    if(n==2):
        for i in range(0, len(x_data)):
            for j in range(0, len(x_data)):
                if (i >= j):
                    pass
                else:
                    Var.append(basis)
                    Var.append(x_data[i])
                    Var.append(x_data[j])
                    Var.append(i)
                    Var.append(j)
                    FinalData.append((Var))
                    Var = []
    if(n==3):
        for i in range(0, len(x_data) - 2):
            for j in range(i + 1, len(x_data) - 1):
                for k in range(j + 1, len(x_data)):
                    Var.append(basis)
                    Var.append(x_data[i])
                    Var.append(x_data[j])
                    Var.append(x_data[k])
                    Var.append(i)
                    Var.append(j)
                    Var.append(k)
                    FinalData.append((Var))
                    Var = []
    if(n==4):
        for i in range(0, len(x_data) - 3):
            for j in range(i + 1, len(x_data) - 2):
                for k in range(j + 1, len(x_data) - 1):
                    for l in range(k + 1, len(x_data)):
                        Var.append(basis)
                        Var.append(x_data[i])
                        Var.append(x_data[j])
                        Var.append(x_data[k])
                        Var.append(x_data[l])
                        Var.append(i)
                        Var.append(j)
                        Var.append(k)
                        Var.append(l)
                        FinalData.append((Var))
                        Var = []
    if(n==5):
        for i in range(0, len(x_data) - 4):
            for j in range(i + 1, len(x_data) - 3):
                for k in range(j + 1, len(x_data) - 2):
                    for l in range(k + 1, len(x_data) - 1):
                        for m in range(l + 1, len(x_data)):
                            Var.append(basis)
                            Var.append(x_data[i])
                            Var.append(x_data[j])
                            Var.append(x_data[k])
                            Var.append(x_data[l])
                            Var.append(x_data[m])
                            Var.append(i)
                            Var.append(j)
                            Var.append(k)
                            Var.append(l)
                            Var.append(m)
                            FinalData.append((Var))
                            Var = []
    if(n==6):
        for i in range(0, len(x_data) - 5):
            for j in range(i + 1, len(x_data) - 4):
                for k in range(j + 1, len(x_data) - 3):
                    for l in range(k + 1, len(x_data) - 2):
                        for m in range(l + 1, len(x_data) - 1):
                            for n in range(m + 1, len(x_data)):
                                Var.append(basis)
                                Var.append(x_data[i])
                                Var.append(x_data[j])
                                Var.append(x_data[k])
                                Var.append(x_data[l])
                                Var.append(x_data[m])
                                Var.append(x_data[n])
                                Var.append(i)
                                Var.append(j)
                                Var.append(k)
                                Var.append(l)
                                Var.append(m)
                                Var.append(n)
                                FinalData.append((Var))
                                Var = []
    return FinalData
