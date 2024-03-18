import numpy
import matplotlib.pyplot as plt
import sys
filename = sys.argv[1]
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
plt.figure(figsize=(8,4))
plt.plot(czas,napiecia)
plt.xlabel("czas[s]")
plt.xticks(czas[::30],rotation=30)
plt.yticks(numpy.arange(min(napiecia), max(napiecia) + 0.1, 0.1))
plt.ylabel("napiecie[V]")
plt.show()
