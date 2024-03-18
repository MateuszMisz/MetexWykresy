import numpy
import matplotlib.pyplot as plt
import sys
yaxisname=""
xaxisname=""
arg=sys.argv
for index,value in enumerate(arg):
    if index == 0:
        continue
    if  value=="yname":
        yaxisname=arg[index+1]
        arg.pop(index+1)
        continue
    if value=="xname":
        xaxisname=arg[index+1]
        arg.pop(index+1)
        continue
    filename = value
    ##filename="1_MMJP.csv"
    napiecia=[]
    czas=[]
    with open(filename,"r") as f:
        for line in f:
            print(line)
            if line.startswith("M") or line.startswith("'") or line==(""):
                continue
            parts = line.split(",")
            napiecia.append(parts[0])
            czas.append(parts[3])
    # osx=numpy.array(czas)
    # osy=numpy.array(int(napiecia))
    napiecia = [float(x) for x in napiecia]
    plt.figure(value.split('\\')[-1],figsize=(8,4))
    plt.plot(czas,napiecia)
    plt.xlabel(xaxisname if xaxisname!="" else "czas[s]")
    plt.xticks(czas[::30],rotation=30)
    plt.yticks(numpy.arange(min(napiecia), max(napiecia) + 0.1, 0.1))
    plt.ylabel(yaxisname if yaxisname!="" else "napiecie[V]")
plt.show()