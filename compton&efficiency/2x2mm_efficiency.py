# График: зависимость эффективности от длины "слоёв".
# Каждая линия на графике отвечает за свою энергию (см. легенду).

import matplotlib.pyplot as plt
import numpy as np
import os

# Переход в папку для работы
os.chdir("C:/Users/1/Geant4/program_files/share/Geant4/my_examples/"
          "SiPlane_Efficiency/build/Release/2x2 (mm^2)/ExceptGamma/")

layer_length = [10, 20, 40, 50, 100]  # Параметр для графика: микрометры слоя

plt.figure(figsize=(8,6))
plt.title("The efficiency of obtaining both coordinates")
plt.xlabel("Length of layer, μm")
plt.ylabel("Efficiency")
plt.ylim(0, 1)

# for energy, color in zip (["200keV", "300keV", "500keV", "1MeV",
#                            "2MeV", "5MeV", "10MeV"],
#                           ["c", "b", "r", "g", "orange", "m", "k"]):
for energy, color in zip(["200keV", "300keV", "500keV", "2MeV", "10MeV"],
                             ["c", "b", "r", "g", "orange"]):
    efficiency = []  # Массив значений долей 1+ комптон-эффектов с переходами
    for micrometers in layer_length:
        # Взятие данных из источника
        source = "2x2x0.5mm_NotPh_layer"+str(micrometers)+"um_"+energy+".dat"
        with open(source, 'r') as data:
            for row in data:
                if ('Ratio of interacted photons '
                    'with transitions and interacted photons:') in row:
                    efficiency.append(float(row.split()[-1]))
                    # print(efficiency)
    # Изображение графика
    # plt.plot(layer_length, efficiency, '.',
    #          linestyle = 'dashed', label = energy)
    plt.plot(layer_length, efficiency, '.', color = color,
             linestyle = 'solid', label = energy)

plt.legend(loc = "upper right")
plt.savefig("2x2x0.5mm_NotPh_efficiency_5energies_1angle.png")
plt.show()