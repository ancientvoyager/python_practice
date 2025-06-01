# Здесь работа происходит следующим образом:
# Из исходного файла берутся две колонки: название процесса и энергия.
# После этого энергия переписывается в отдельную переменную (не np.array),
# откуда уже используются данные для гистограммы.

import matplotlib.pyplot as plt
import numpy as np

# Источник данных
source = ("C:/Users/1/Geant4/program_files/share/Geant4/my_examples/"
          "SiPlane_Trajectory/build/Release/data_2MeV.dat")

# Из источника необходимо взять столбцы с процессами и энергиями (способ 1)
data = np.genfromtxt(source, dtype=None, usecols=[0, 1], encoding="utf-8")
energy = []  # Энергия комптоновских электронов (одномерный массив)
for row in range(len(data)):
    if data[row, 0] == 'compt':
        energy.append(float(data[row, 1][0:-1]))  # Не включается
        # последний элемент, потому что это ";"
particles = len(ELoss)  # Число комптоновских электронов

# Способ 2 (подсказан Дашей)
# data = open(local_filename, 'r')
# energy = []  # Энергия комптоновских электронов (одномерный массив)
# for row in data:
#     if 'compt' in row:
#         energy.append(float(line.replace(';', '').split()[1]))
# particles = len(ELoss)  # Число комптоновских электронов
# print(energy[0:25])  # Проверка элементов массива (для себя)
print('We have in this modeling', particles, 'compton electrons')

# Изображение гистограммы
plt.figure()
plt.title("Spectrum of compton electrons")
plt.xlabel("Energy, keV")
plt.ylabel("Number of electrons")
plt.hist(energy, bins=70)
# plt.hist(energy, bins=70, weights=[1/particles]*particles)
plt.savefig("Spectrum")
plt.show()