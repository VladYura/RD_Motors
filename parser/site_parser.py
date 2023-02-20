import requests
import json
from bs4 import BeautifulSoup
import lxml
from config import URL_CATEGORIES


def parser_categories(url):
    req = requests.get(url=url)
    soup = BeautifulSoup(req.text, 'lxml')
    cat = soup.find('div', class_='brands-list').find_all('option')
    categories = [item.text for item in cat]
    values = [item['value'] for item in cat]
    return categories, values


def parser_cars(url):
    req = requests.get(url=url)
    soup = BeautifulSoup(req.text, 'lxml')
    cars = soup.find('select', class_='form-control js-ajax-count select2').find_all('option')
    cars_data = [item.text for item in cars]
    cars_value = [item['value'] for item in cars]
    return cars_data, cars_value


def parser_model():
    with open('data_txt/cars_values.txt', 'r', encoding='utf-8') as file:
        values = file.readlines()

    dict_list = []
    for value in values:
        url = f'https://bamper.by/ajax/getModelList.php?CODE={value}'
        req = requests.get(url)
        items = req.text
        dict_list.append(json.loads(items))
        print(f'Load {value}')

    model_out_list, value_out_list = [], []
    for dct in dict_list:
        model_lst = []
        value_list = []
        for itm in dct['ITEMS']:
            model_lst.append(itm['NAME'])
            value_list.append(itm['CODE'])
        model_out_list.append('|'.join(model_lst))
        value_out_list.append('|'.join(value_list))
        del model_lst, value_list

    return model_out_list, value_out_list


def load_in_file(name, data):
    with open(f'data_txt/{name}.txt', 'w', encoding='utf-8') as file:
        for item in data:
            file.write(item + '\n')


if __name__ == "__main__":
    # !-- Parsing spare parts category --!
    cars_parts, parts_cat = parser_categories(URL_CATEGORIES)
    load_in_file('cars_parts', cars_parts)
    load_in_file('parts_categories', parts_cat)

    # !-- Parsing car`s names and values (for parsing car`s models) --!
    # cars_names, cars_values = parser_cars(URL_CATEGORIES)
    # load_in_file('cars_brands', cars_names)
    # load_in_file('cars_values', cars_values)

    # !-- Parsing car`s models --!
    # cars_models, models_values = parser_model()
    # load_in_file('cars_models', cars_models)
    # load_in_file('models_values', models_values)
