# Файл для генерации файлов для пункта а к заданию
# Просто запустить и ждать
# После генерации файла выводится правильный ответ

import random
import time
import os
from math import dist

invalid_tries = 0
is_invalid_file = False

def generate_file():
    f = open("27A.txt", "x+")
    m = 100000
    m2 = m / 50
    checksure = []
    for _ in range(250):
        x = f"{random.randint(-m, m) / m2:.5f}"
        y = f"{random.randint(-m, m) / m2:.5f}"
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

while True:
    if is_invalid_file: invalid_tries += 1
    is_invalid_file = False
    if invalid_tries >= 15: 
        print("something is wrong")
        exit()
    
    try:
        os.remove("27A.txt")
        os.remove("27A_DIAGRAMM.txt")
    except: pass
    
    generate_file()
    f = open("27A.txt")
    
    data = []
    bad_points_data = []
    
    for line in f.readlines():
        line = line.rstrip().replace(",", ".")
        x, y, p, r = line.split()
        x = float(x)
        y = float(y)
        p = int(p)
        r = int(r)
        data.append([[x, y], p, r])
        
    for point in data:
        income = get_income(point)
        if income <= 0:
            bad_points_data.append(point)
    
    for point1 in data:
        for point2 in data:
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
        if is_invalid_file: break
    
    if is_invalid_file:
        f.close()
        os.remove("27A.txt")
        continue
    Np = len(bad_points_data)
    Pp = abs(sum([point_data[1] - point_data[2] for point_data in bad_points_data]))
    
    print(Np, Pp)
    
    # Если нужно составить диаграмму, чтобы увидеть оставшие после закрытия точки
    # f2_res = open("27A_DIAGRAMM.txt", "x+")
    # for p in data:
    #     if p not in bad_points_data:
    #         f2_res.write(f"{p[0][0]} {p[0][1]}\n".replace(".", ","))
    # f2_res.close()
    
    break