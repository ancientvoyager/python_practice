# Здесь работа происходит следующим образом:
# Из исходного файла берутся данные по потерям энергии: все элементы строки,
# кроме первого (название), второго (начальная энергия)
# и последнего (поглощение/побег).
# После этого все данные значения суммируются для получения
# полной потери энергии определённой частицы.
# На основе этих данных дальше составляются гистограммы
# (в том числе по отдельным процессам: Комптон, ионизация и т.д.).

import matplotlib.pyplot as plt
import numpy as np

# Источник данных
source = ("C:/Users/1/Geant4/program_files/share/Geant4/my_examples/"
          "SiPlane_Trajectory/build/Release/ELoss_5MeV_3cm.dat")

# Взятие данных из источника по потерям энергии для каждой частицы
data = open(source, 'r')
ELoss = []  # Потеря энергии (одномерный массив)
# ELoss_norm = []  # Потеря энергии, нормированная на число частиц

# Наполнение массива: сумма каждой строки потери энергии (по каждому процессу)
for row in data:
    if 'eIoni' in row:
        ELoss.append(sum(list(map(float, row.replace(';', '').split()[2:-1]))))
particles = len(ELoss)  # Число частиц
# for i in range(particles):
#     ELoss_norm.append(ELoss[i]/particles)
# for row in ELoss: print(row)
print('Minimum energy loss:', min(ELoss), 'keV',
      '\nMaximum energy loss:', max(ELoss), 'keV')
print('We have in this modeling', particles, 'ionisations')

bins = 70
# Нормировка (как оказалось, вообще не та, но решение прикольное)
# values, edges=np.histogram(ELoss,bins=bins)
# weights=[]
# for value in ELoss:
#     for i in range(len(edges)-1):
#         # print(edges[i],edges[i+1])
#         if edges[i]<=value<edges[i+1]:
#             weights.append(1/values[i])
#         elif i==len(edges)-2 and edges[i]<=value<=edges[i+1]:weights.append(1/values[i])

# Изображение гистограммы
plt.figure()
plt.title('Energy losses (electron: ionisation)')
plt.xlabel('Energy, keV')
plt.ylabel("Number of particles")
plt.hist(ELoss, bins=bins)
plt.savefig("IonisLosses_normed_5MeV_3cm")
plt.show()