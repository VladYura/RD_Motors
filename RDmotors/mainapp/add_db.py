def open_file_models():
    output = []
    with open('D:\proj pyrhon\workProject\parser\data_txt\cars_models.txt', 'r', encoding='utf-8') as models, \
            open('D:\proj pyrhon\workProject\parser\data_txt\models_values.txt', 'r', encoding='utf-8') as values, \
            open('D:\proj pyrhon\workProject\parser\data_txt\cars_values.txt', 'r', encoding='utf-8') as car:
        lines_1 = models.readlines()
        lines_2 = values.readlines()
        lines_3 = car.readlines()
        for i in range(len(lines_1)):
            temp1 = lines_1[i].split('|')
            temp2 = lines_2[i].split('|')
            for j in range(len(temp1)):
                output.append((temp1[j], f'{lines_3[i][:-1]}_' + temp2[j]))

    return output


def open_two_files():
    output = []
    with open('D:\proj pyrhon\workProject\parser\data_txt\cars_models.txt', 'r', encoding='utf-8') as models, \
            open('D:\proj pyrhon\workProject\parser\data_txt\cars_brands.txt', 'r', encoding='utf-8') as car, \
            open('D:\proj pyrhon\workProject\parser\data_txt\cars_values.txt', 'r', encoding='utf-8') as values:
        model_data = models.readlines()
        cars_data = car.readlines()
        car_values = values.readlines()
        for i in range(len(model_data)):
            output.append((cars_data[i][:-1], car_values[i][:-1], model_data[i].split('|')))

    return output


print(open_two_files())


def add_cat():
    output = []
    with open('D:\proj pyrhon\workProject\parser\data_txt\cars_parts.txt', 'r', encoding='utf-8') as cat, \
            open('D:\proj pyrhon\workProject\parser\data_txt\parts_categories.txt', 'r', encoding='utf-8') as part_cat:
        categories = cat.readlines()
        values = part_cat.readlines()
        for i in range(len(categories)):
            output.append((categories[i], values[i]))
    return output


def add_cars_values():
    output = []
    with open('D:\proj pyrhon\workProject\parser\data_txt\cars_values.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in lines:
            output.append(i)
    return output

