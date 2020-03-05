import pandas as pd
import matplotlib.pyplot as plt

URL = "https://stepik.org/media/attachments/lesson/8083/genetherapy.csv"
data = pd.read_csv(URL)


grps = pd.unique(data.Therapy.values)
A = data[data["Therapy"] == "A"]["expr"]
Aavg = sum(A)/len(A)
Aerr = 4.1
B = data[data["Therapy"] == "B"]["expr"]
Bavg = sum(B)/len(B)
Berr = 5.8
C = data[data["Therapy"] == "C"]["expr"]
Cavg = sum(C)/len(C)
Cerr = 5.1
D = data[data["Therapy"] == "D"]["expr"]
Davg = sum(D)/len(D)
Derr = 3.8
list = ['therapy A', 'therapy B', 'therapy C', 'therapy D']
listAVG = [Aavg, Bavg, Cavg, Davg]
listERR = [Aerr/2, Berr/2, Cerr/2, Derr/2]
print(list, listAVG)

plt.errorbar(x=list, y=listAVG, yerr=listERR, color="black", capsize=3, marker="s", markersize=5, mfc="red", mec="black")
plt.title('STEPIK')
plt.grid()
plt.xlabel('therapy')
plt.ylabel('valu+error')
plt.show()