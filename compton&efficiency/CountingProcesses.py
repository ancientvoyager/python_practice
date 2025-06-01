# Здесь работа происходит следующим образом:
# Задаётся четыре массива, соответствующих значениям энергии
# и количествам событий, где происходили комптоновские процессы (1+, 2+, 3+).
# Затем, из log-файла берутся данные, обрабатывая которые заполняются
# комптон-массивы (массив для энергии — вручную заполняемый параметр).
# После этого строится график зависимости количества событий (в долях),
# где был эффект Комптона (не менее 1, 2 и 3 раз), от энергии.
# Данные берутся одновременно из нескольких log-файлов в соответствии
# с заданным значением энергии.

# Обновление: теперь помимо Комптон-эффектов учитываются ещё
# и процессы для появления фотонов: тормозное излучение с аннигиляцией.
# Суть работы та же.

import matplotlib.pyplot as plt
import numpy as np
import os

# Переход в папку для работы
os.chdir("C:/Users/1/Geant4/program_files/share/Geant4/my_examples/"
         "SiPlane_Trajectory/build/Release/"
         "100plates_2ndgamma_analysis/0.5mm")

# Массив энергий в МэВах (ПАРАМЕТР для графика)
energy = [0.5, 1, 2, 5, 10, 20, 50, 100]
# compt_1plus = [] # 1+ комптоновских процессов (для графика)
# compt_2plus = [] # 2+ комптоновских процессов (для графика)
# compt_3plus = [] # 3+ комптоновских процессов (для графика)
# gamma2nd = [] # Вторичные фотоны
# brem = [] # Тормозное излучение (для графика)
# annihil = [] # Парная аннигиляция (для графика)
# annihil_brem = [] # Соотношение двух вышеописанных процессов (для графика)
sec_interacted = [] # Отношение: кол-во событий с вторичными фотонами
# к кол-ву событий, где были порождены все вторичные частицы (для графика)
brem_interacted = [] # Отношение: кол-во событий с фотонами тормозного изл.
# к кол-ву событий, где были порождены все вторичные частицы (для графика)
annihil_interacted = [] # Отношение: кол-во событий с аннигиляционными ф-ми
# к кол-ву событий, где были порождены все вторичные частицы (для графика)

for cycle, source in zip(range(8), ["100plates0.5mm_gamma2nd_500keV_2.0.dat",
                                    "100plates0.5mm_gamma2nd_1MeV_2.0.dat",
                                    "100plates0.5mm_gamma2nd_2MeV_2.0.dat",
                                    "100plates0.5mm_gamma2nd_5MeV_2.0.dat",
                                    "100plates0.5mm_gamma2nd_10MeV_2.0.dat",
                                    "100plates0.5mm_gamma2nd_20MeV_2.0.dat",
                                    "100plates0.5mm_gamma2nd_50MeV_2.0.dat",
                                    "100plates0.5mm_gamma2nd_100MeV_2.0.dat"]):
    # Взятие данных из источника по потерям энергии для каждой частицы
    data = open(source, 'r')

    # Наполнение массива счётчиков
    for row in data:
        # if '1+ Compton scatterings (normed):' in row:
        #     # print(row.split()[-1])
        #     compt_1plus.append(float(row.split()[-1]))
        # if '2+ Compton scatterings (normed):' in row:
        #     # print(row.split()[-1])
        #     compt_2plus.append(float(row.split()[-1]))
        # if '3+ Compton scatterings (normed):' in row:
        #     # print(row.split()[-1])
        #     compt_3plus.append(float(row.split()[-1]))
        # if 'Bremsstrahlung processes:' in row:
        #     # print(row.split()[-1])
        #     brem.append(float(row.replace('%', '').split()[-1]))
        # if 'Pair annihilations:' in row:
        #     # print(row.split()[-1])
        #     annihil.append(float(row.replace('%', '').split()[-1]))
        # if 'Secondary photons:' in row:
        #     # print(row.split()[-1])
        #     gamma2nd.append(float(row.replace('%', '').split()[-1]))
        if 'Secondary (in event)/interacted photons ratio:' in row:
            # print(row.split()[-1])
            sec_interacted.append(float(row.replace('%', '').split()[-1]))
        if 'Bremsstrahlung (in event)/interacted photons ratio:' in row:
            # print(row.split()[-1])
            brem_interacted.append(float(row.replace('%', '').split()[-1]))
        if 'Pair annihilations (in event)/interacted photons ratio:' in row:
            # print(row.split()[-1])
            annihil_interacted.append(float(row.replace('%', '').split()[-1]))
# print(compt_1plus)
# print(compt_2plus)
# print(compt_3plus)

print(sec_interacted)
print(brem_interacted)
print(annihil_interacted)

# Изображение графика
# plt.figure(figsize = (8, 6))
plt.figure()
plt.title("Secondary photons in events with interactions (depth = 0.5 mm)")
plt.xlabel("Energy, MeV")
plt.ylabel("Percent")
plt.yticks(ticks=[0, 20, 40, 60, 80, 100],
           labels=['0%', '20%', '40%', '60%', '80%', '100%'])
plt.xscale("log")
# plt.plot(energy, compt_1plus, 'o', label = '1+ Compton scatterings')
# plt.plot(energy, compt_2plus, 'o', label = '2+ Compton scatterings')
# plt.plot(energy, compt_3plus, 'o', label = '3+ Compton scatterings')
plt.plot(energy, sec_interacted, 'o-',
         label = 'Secondary photons (total)')
plt.plot(energy, brem_interacted, 'o-',
         label = 'Bremsstrahlung')
plt.plot(energy, annihil_interacted, 'o-',
         label = 'Pair annihilations')
plt.legend(loc = 'best')
# plt.savefig("2ndgamma_interact_100plates0.5mm.png")
plt.show()

# В этом разделе (ниже) хранится блок, который использовался
# для более старого выпуска кода, когда в log-файл выводились
# все процессы появления только электронов (комптон, фотоэффект и т.д.).
# Сохраняю исключительно для красоты и напоминания,
# что я отсюда могу брать некоторые решения для других задач.

# Цикл с учётом изменения источника данных
# for cycle, source in zip(range(11), ["100plates0.5mm_500keV.dat",
#                                     "100plates0.5mm_1MeV.dat",
#                                     "100plates0.5mm_2MeV.dat",
#                                     "100plates0.5mm_5MeV.dat",
#                                     "100plates0.5mm_10MeV.dat",
#                                     "100plates0.5mm_20MeV.dat",
#                                     "100plates0.5mm_50MeV.dat",
#                                     "100plates0.5mm_100MeV.dat",
#                                     "100plates0.5mm_200MeV.dat",
#                                     "100plates0.5mm_500MeV.dat",
#                                     "100plates0.5mm_1GeV.dat"]):
    # Взятие данных из источника по потерям энергии для каждой частицы
    # data = open(source, 'r')
    # ComptonCounter = 0 # Счётчик комптоновских процессов (для одного фотона)
    # counters = [] # Массив данных счётчиков (потребуется для составления графика)
    # counter_1plus = 0 # 1+ комптоновских процессов
    # counter_2plus = 0 # 2+ комптоновских процессов
    # counter_3plus = 0 # 3+ комптоновских процессов

    # Наполнение массива счётчиков
    # for row in data:
    #     if 'compt' in row:
    #         ComptonCounter += 1
    #     elif 'Separating line' in row:
    #         # print(ComptonCounter)
    #         counters.append(ComptonCounter)
    #         ComptonCounter = 0

    # Подсчёт событий с комптоновскими процессами в долях
    # for i in counters:
    #     if i >= 1:
    #         counter_1plus += 1
    #     if i >= 2:
    #         counter_2plus += 1
    #     if i >= 3:
    #         counter_3plus += 1
    # counter_1plus = counter_1plus/len(counters)
    # compt_1plus.append(counter_1plus)
    # counter_2plus = counter_2plus/len(counters)
    # compt_2plus.append(counter_2plus)
    # counter_3plus = counter_3plus/len(counters)
    # compt_3plus.append(counter_3plus)