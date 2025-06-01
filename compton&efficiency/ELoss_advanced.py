# Здесь работа происходит следующим образом:
# Из исходного файла берутся данные по потерям энергии: все элементы строки,
# кроме первого (название), второго (начальная энергия)
# и последнего (поглощение/побег).
# После этого все данные значения суммируются для получения
# полной потери энергии определённой частицы.
# На основе этих данных дальше составляются гистограммы
# (в том числе по отдельным процессам: Комптон, ионизация и т.д.).
# "Advanced": сразу строится несколько требуемых гистограмм вместо одной.

import matplotlib.pyplot as plt

# Источник данных
source = ("C:/Users/1/Geant4/program_files/share/Geant4/my_examples/"
          "SiPlane_Trajectory/build/Release/ELoss_2MeV.dat")
plt.figure(figsize=[7, 6])

# Взятие данных из источника по потерям энергии для каждой частицы
with open(source, 'r') as data:
    ELoss = [[] for temp1 in range(4)]  # Потеря энергии (двумерный массив)
    particles = [0 for temp2 in range(4)]  # Число частиц (одномерный массив)
    print('We have in this modeling:')
    for row in data:
        # Все частицы (раскрыть в случае необходимости)
        # ELoss[0].append(sum(
        #     list(map(float, row.replace(';', '').split()[2:-1]))))
        if 'compt' in row:  # Эффект Комптона
            ELoss[1].append(sum(
                list(map(float, row.replace(';', '').split()[2:-1]))))
        elif 'eIoni' in row:  # Ионизация
            ELoss[2].append(sum(
                list(map(float, row.replace(';', '').split()[2:-1]))))
        elif 'phot' in row:  # Фотоэффект
            ELoss[3].append(sum(
                list(map(float, row.replace(';', '').split()[2:-1]))))
        elif 'conv' in row:  # Рождение пар
            ELoss[3].append(sum(
                list(map(float, row.replace(';', '').split()[2:-1]))))
    for i in range(4):
        particles[i] = len(ELoss[i])

# Для вывода четырёх гистограмм
for i, effect in zip(range(4), ['Compton effects',
                                'ionisations',
                                'photoelectric effects',
                                'pair productions']):
    print(particles[i], effect)

# Как пример: если нет пар, но всё же хочется четыре гистограммы
# for i, effect in zip(range(4), ['in total',
#                                 'Compton effects',
#                                 'ionizations',
#                                 'photoelectric effects']):
#     print(particles[i], effect)

    # Изображение гистограмм
    plt.subplot(2, 2, i + 1)
    plt.title("Energy losses by " + effect)
    plt.xlabel("Energy, keV")
    plt.ylabel("Number of particles")
    plt.hist(ELoss[i], bins=70, weights=[1/particles[i]]*particles[i])
    plt.subplots_adjust(hspace=0.5)
    plt.subplots_adjust(wspace=0.5)
    # plt.savefig("AllLosses_10MeV")
plt.show()