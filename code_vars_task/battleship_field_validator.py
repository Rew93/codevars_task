def find_coordinate(field):  # шукаємо координати всіх 1
    l = []
    [l.append([i, j]) for i in range(10) for j in range(10) if field[i][j] == 1]
    return l


def find_1(coordinate):  # шукаємо координати всіх кубиків 1 на 1
    l_1 = []
    for i in coordinate:
        a = i[0]
        b = i[1]
        l_axp_1 = [[a, b + 1], [a - 1, b - 1], [a - 1, b], [a - 1, b + 1], [a, b - 1],
                   [a + 1, b - 1], [a + 1, b + 1], [a + 1, b]]
        if len(list(filter(lambda x: x not in coordinate, l_axp_1))) == 8:
            l_1.append(i)
    return l_1


def find_2_3_4(lst):
    l_2 = []
    l_3 = []
    l_4 = []
    for i in lst:
        a = i[0]  # координати 1-шой клітинки
        b = i[1]
        l_dop_kubic = [[a, b + 1], [a, b - 1], [a + 1, b], [a - 1, b]]
        c = list(filter(lambda x: x in lst, l_dop_kubic))

        if len(c) == 1 and c[-1][0] == a + 1 and b == c[-1][1]:  # в низ по вертикалі
            a_1 = c[-1][0]  # координати 2-гої клітинки
            b_1 = c[-1][1]
            l_audit_2_v = [[a - 1, b - 1], [a - 1, b], [a - 1, b + 1], [a, b - 1], [a, b + 1],
                           [a + 1, b - 1], [a + 1, b + 1], [a_1 + 1, b_1 - 1], [a_1 + 1, b_1],
                           [a_1 + 1, b_1 + 1]]  # перевірка для 2-х палубного корабля
            all_kub = len(list(filter(lambda x: x not in lst, l_audit_2_v)))
            if all_kub == 10:
                l_2.append([[a, b], [a_1, b_1]])
            elif all_kub == 9 and [a_1 + 1, b_1] in lst:  # знаходимо коокдинати 3 палубного корябля
                a_2 = a_1 + 1
                b_2 = b_1
                l_audit_3_v = [[a_2 + 1, b_2 - 1], [a_2 + 1, b_2],
                               [a_2 + 1, b_2 + 1]]  # перевірка для 3-х палубного корабля
                all_kub = len(list(filter(lambda x: x not in lst, l_audit_3_v)))
                if all_kub == 3:
                    l_3.append([[a, b], [a_1, b_1], [a_2, b_2]])
                elif all_kub == 2 and [a_2 + 1, b_2] in lst:
                    a_3 = a_2 + 1
                    b_3 = b_2
                    l_audit_4_v = [[a_3 + 1, b_3 - 1], [a_3 + 1, b_3],
                                   [a_3 + 1, b_3 + 1]]  # перевірка для 4-х палубного корабля
                    all_kub = len(list(filter(lambda x: x not in lst, l_audit_4_v)))
                    if all_kub == 3:
                        l_4.append([[a, b], [a_1, b_1], [a_2, b_2], [a_3, b_3]])
        elif len(c) == 1 and c[-1][0] == a and c[-1][1] == b + 1:  # координати другої клітинки по горизонталі правіше
            a_1 = c[-1][0]  # координати 2-гої клітинки
            b_1 = c[-1][1]
            l_audit_2_h = [[a - 1, b - 1], [a - 1, b], [a - 1, b + 1], [a, b - 1],
                           [a + 1, b - 1], [a + 1, b + 1], [a + 1, b], [a_1 - 1, b_1 + 1], [a_1, b_1 + 1],
                           [a_1 + 1, b_1 + 1]]  # перевірка для 2-х палубного корабля
            all_kub = len(list(filter(lambda x: x not in lst, l_audit_2_h)))
            if all_kub == 10:
                l_2.append([[a, b], [a_1, b_1]])
            elif all_kub == 9 and [a_1, b_1 + 1] in lst:  # знаходимо коокдинати 3 палубного корябля
                a_2 = a_1
                b_2 = b_1 + 1
                l_audit_3_h = [[a_2 - 1, b_2], [a_2, b_2 + 1],
                               [a_2 + 1, b_2 + 1]]  # перевірка для 3-х палубного корабля
                all_kub = len(list(filter(lambda x: x not in lst, l_audit_3_h)))
                if all_kub == 3:
                    l_3.append([[a, b], [a_1, b_1], [a_2, b_2]])
                elif all_kub == 2 and [a_2, b_2 + 1] in lst:
                    a_3 = a_2
                    b_3 = b_2 + 1
                    l_audit_4_h = [[a_3 - 1, b_3], [a_3, b_3 + 1],
                                   [a_3 + 1, b_3 + 1]]  # перевірка для 4-х палубного корабля
                    all_kub = len(list(filter(lambda x: x not in lst, l_audit_4_h)))
                    if all_kub == 3:
                        l_4.append([[a, b], [a_1, b_1], [a_2, b_2], [a_3, b_3]])
    if len(l_2) == 3 and len(l_3) == 2 and len(l_4) == 1:
        return True
    else:
        return False


def validate_battlefield(field):
    lst = find_coordinate(field)  # список координат всіх 1
    if len(lst) != 20:
        return False
    else:
        lst_1 = find_1(lst)  # список координат 1 на 1
        if len(lst_1) != 4:
            return False
        else:
            [lst.remove(i) for i in lst_1]  # видаляемо координати всіх 1 на 1
            if find_2_3_4(lst):
                return True
            else:
                return False

