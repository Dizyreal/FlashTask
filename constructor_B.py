# Файл для генерации файлов для пункта б к заданию
# Просто запустить и ждать
# После генерации файла выводится правильный ответ

import random
import time
import os
from math import dist

invalid_tries = 0
is_invalid_file = False

def generate_file():
    f = open("27B.txt", "x+")
    m = 100000
    m2 = m
    checksure = []
    
    zone1_min_x = -100
    zone1_max_x = -60
    zone1_min_y = -95
    zone1_max_y = -55
    for _ in range(random.randint(160, 260)):
        x = f"{random.randint(zone1_min_x, zone1_max_x) * m / m2 + (random.randint(0, 10000) / 10000):.5f}"
        y = f"{random.randint(zone1_min_y, zone1_max_y) * m / m2 + (random.randint(0, 10000) / 10000):.5f}"
        virushka = random.randint(400, 1000)
        rashodi = random.randint(10, 1000)
        pribyl = virushka - rashodi
        while pribyl in checksure:
            virushka = random.randint(400, 1000)
            rashodi = random.randint(10, 500)
            pribyl = virushka - rashodi
        checksure.append(pribyl)
        f.write(f"{x} {y} {virushka} {rashodi}\n".replace(".", ","))
    
    checksure.clear()
    
    zone2_min_x = -30
    zone2_max_x = 30
    zone2_min_y = -25
    zone2_max_y = 15
    for _ in range(random.randint(160, 260)):
        x = f"{random.randint(zone2_min_x, zone2_max_x) * m / m2 + (random.randint(0, 10000) / 10000):.5f}"
        y = f"{random.randint(zone2_min_y, zone2_max_y) * m / m2 + (random.randint(0, 10000) / 10000):.5f}"
        virushka = random.randint(400, 1000)
        rashodi = random.randint(10, 1000)
        pribyl = virushka - rashodi
        while pribyl in checksure:
            virushka = random.randint(400, 1000)
            rashodi = random.randint(10, 500)
            pribyl = virushka - rashodi
        checksure.append(pribyl)
        f.write(f"{x} {y} {virushka} {rashodi}\n".replace(".", ","))
        
    checksure.clear()
        
    zone3_min_x = 60
    zone3_max_x = 100
    zone3_min_y = 55
    zone3_max_y = 95
    for _ in range(random.randint(160, 260)):
        x = f"{random.randint(zone3_min_x, zone3_max_x) * m / m2 + (random.randint(0, 10000) / 10000):.5f}"
        y = f"{random.randint(zone3_min_y, zone3_max_y) * m / m2 + (random.randint(0, 10000) / 10000):.5f}"
        virushka = random.randint(400, 1000)
        rashodi = random.randint(10, 1000)
        pribyl = virushka - rashodi
        while pribyl in checksure:
            virushka = random.randint(400, 1000)
            rashodi = random.randint(10, 500)
            pribyl = virushka - rashodi
        checksure.append(pribyl)
        f.write(f"{x} {y} {virushka} {rashodi}\n".replace(".", ","))

def get_income(p):
    return p[1] - p[2]

def get_region_lowest_income(region_data):
    curr_sum = 0
    for pvz in region_data:
        curr_sum += pvz[1] - pvz[2]
    return curr_sum

def get_region_task_data(region_data):
    global is_invalid_file
    bad_points_data = []
        
    for point in region_data:
        income = get_income(point)
        if income <= 0:
            bad_points_data.append(point)
    
    for point1 in region_data:
        for point2 in region_data:
            if point1 == point2: 
                continue
            if point1 in bad_points_data or point2 in bad_points_data:
                continue
            magnitude = dist(point1[0], point2[0])
            if magnitude <= 3:
                income1 = get_income(point1)
                income2 = get_income(point2)
                if income1 > income2: 
                    bad_points_data.append(point2)
                elif income1 < income2: 
                    bad_points_data.append(point1)
                else:
                    is_invalid_file = True
                    break
        if is_invalid_file: return None
    Np = len(bad_points_data)
    Pp = abs(sum([point_data[1] - point_data[2] for point_data in bad_points_data]))
    return Np, Pp

while True:
    if is_invalid_file: invalid_tries += 1
    is_invalid_file = False
    if invalid_tries >= 150: 
        print("something is wrong")
        exit()
    
    try:
        os.remove("27B.txt")
        os.remove("27B_DIAGRAMM.txt")
    except: pass
    
    generate_file()
    f = open("27B.txt")
    
    global_data = []
    for line in f.readlines():
        line = line.rstrip().replace(",", ".")
        x, y, p, r = line.split()
        x = float(x)
        y = float(y)
        p = int(p)
        r = int(r)
        global_data.append([[x, y], p, r])
    
    region1_data = []
    region2_data = []
    region3_data = []
    
    for p in global_data:
        if p[0][0] > 50:
            region1_data.append(p)
        elif -50 <= p[0][0] <= 50:
            region2_data.append(p)
        else:
            region3_data.append(p)
    
    Np1, Pp1 = get_region_task_data(region1_data)
    Np2, Pp2 = get_region_task_data(region2_data)
    Np3, Pp3 = get_region_task_data(region3_data)
    
    if max(Pp1, Pp2, Pp3) <= 25000:
        is_invalid_file = True
    
    count_biggests = 0
    for var in [Pp1, Pp2, Pp3]:
        if var > 25000: count_biggests += 1
    if count_biggests > 1: is_invalid_file = True
    
    check_list = []
    for var in [Pp1, Pp2, Pp3]:
        if var <= 25000:
            check_list.append(var)
    if len(check_list) != 2: is_invalid_file = True
    
    total_reg1_income = get_region_lowest_income(region1_data)
    total_reg2_income = get_region_lowest_income(region2_data)
    total_reg3_income = get_region_lowest_income(region3_data)
    
    check_set = set()
    check_set.add(total_reg1_income)
    check_set.add(total_reg2_income)
    check_set.add(total_reg3_income)
    if len(check_set) != 3: is_invalid_file = True
    
    if is_invalid_file:
        f.close()
        os.remove("27B.txt")
        continue
    
    min_total_reg_income = min(total_reg1_income, total_reg2_income, total_reg3_income)
    choosing_region = region1_data if min_total_reg_income == total_reg1_income else region2_data if min_total_reg_income == total_reg2_income else region3_data

    Np, Pp = get_region_task_data(choosing_region)
    print(Np, Pp)
    
    # Если нужно составить диаграмму, чтобы увидеть оставшие после закрытия точки
    # f2_res = open("27B_DIAGRAMM.txt", "x+")
    # for p in choosing_region:
    #     f2_res.write(f"{p[0][0]} {p[0][1]}\n".replace(".", ","))
    # f2_res.close()
    break