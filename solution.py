from math import dist

# Решение пункта а
 

# Считываем данные
f = open("27A.txt").readlines()
task_A_data = []
for line in f:
    x, y, v, r = line.replace(",", ".").split()
    x = float(x)
    y = float(y)
    v = int(v)
    r = int(r)
    task_A_data.append([[x, y], v, r])

# Функция для получения прибыли ПВЗ
def get_prib(p):
    return p[1] - p[2]

# Функция, которая находая общую прибыль региона за последний месяц
def get_region_total_prib(region_data):
    s = 0
    for point in region_data:
        s += get_prib(point)
    return s

# Функция, которая находить количество закрытых ПВЗ и сэкономленную сумму денег
# ОБЯЗАТЕЛЬНО ДОЛЖНО БЫТЬ УСЛОВИЕ ПРОВЕРКИ "if p1 in bad_data or p2 in bad_data: continue"
# ИМЕННО ВО ВТОРОМ ЦИКЛЕ С p2
# В ИНОМ СЛУЧАЕ ЛОГИКА ПРОГРАММЫ НЕПРАВИЛЬНАЯ И ЗАДАЧА РЕШАЕТСЯ НЕВЕРНО!
# Если проверять ПВЗ p1 до второго цикла, то решение неверное, так как
# ПВЗ p1 тоже может стать плохим в ходе проверок второго цикла с ПВЗ p2
def get_region_task_data(region_data):
    bad_data = []
    for point in region_data:
        prib = get_prib(point)
        if prib <= 0:
            bad_data.append(point)

    for p1 in region_data:
        for p2 in region_data:
            if p1 in bad_data or p2 in bad_data: continue
            if p1 == p2: continue
            magnitude = dist(p1[0], p2[0])
            if magnitude <= 3:
                prib1 = get_prib(p1)
                prib2 = get_prib(p2)
                if prib1 > prib2:
                    bad_data.append(p2)
                else:
                    bad_data.append(p1)
    
    return len(bad_data), abs(sum(point_data[1] - point_data[2] for point_data in bad_data))

# Находим количество закрытых ПВЗ в пункте А и сэкономленную сумму, вписываем их в ответ
Np, Pp = get_region_task_data(task_A_data)
print(Np, Pp)

# Решение пункта б

# Считываем данные
f2 = open("27B.txt").readlines()
task_B_data = []
for line in f2:
    x, y, v, r = line.replace(",", ".").split()
    x = float(x)
    y = float(y)
    v = int(v)
    r = int(r)
    task_B_data.append([[x, y], v, r])

# Распределяем ПВЗ по районам. Стандартное разделение по графику в Excel
region1_data = []
region2_data = []
region3_data = []
for point in task_B_data:
    if point[0][0] > 50:
        region1_data.append(point)
    elif -50 <= point[0][0] <= 50:
        region2_data.append(point)
    else:
        region3_data.append(point)

# Получаем количество закрытых ПВЗ каждого района и сэкономленную сумму
Np1, Pp1 = get_region_task_data(region1_data)
Np2, Pp2 = get_region_task_data(region2_data)
Np3, Pp3 = get_region_task_data(region3_data)

# Определяем регион Евгения, выбираем по суммарной прибыли нужый нам регион
evgeniy_prib = max(Pp1, Pp2, Pp3)
evgeniy_data = region1_data if Pp1 == evgeniy_prib else region2_data if Pp2 == evgeniy_prib else region3_data
petr_regions = [x for x in [region1_data, region2_data, region3_data] if x != evgeniy_data]
choosen_region = petr_regions[1] if get_region_total_prib(petr_regions[0]) > get_region_total_prib(petr_regions[1]) else petr_regions[0]

# Находим количество закрытых ПВЗ в пункте B и сэкономленную сумму, вписываем их в ответ
Np, Pp = get_region_task_data(choosen_region)
print(Np, Pp)