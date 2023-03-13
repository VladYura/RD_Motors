import requests
from bs4 import BeautifulSoup
import json

cookies = {
    '_ym_uid': '1674247344783474644',
    '_ym_d': '1674247344',
    'BX_USER_ID': '97350de67a97c61981abff6891ccd6f5',
    '_ga': 'GA1.2.1460552130.1674247344',
    'USER_CLICK_ID': 'c4s7gr1q',
    '_gid': 'GA1.2.1630214685.1678125434',
    '_ym_isad': '1',
    'PHPSESSID': 'pnhrip3agp3enc174esgdakk88',
    '_gat_UA-31751536-4': '1',
    'BITRIX_SM_aLastSearch': 'a%3A10%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3BN%3Bs%3A3%3A%22url%22%3Bs%3A76%3A%22%2Fzchbu%2Flocal%2Ftemplates%2Fbsclassified%2Fassets%2Fplugins%2Fswipperswiper.min.js.map%2F%22%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3Bs%3A30%3A%22%D0%97%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8++%D1%83+RD-motors%22%3Bs%3A3%3A%22url%22%3Bs%3A20%3A%22%2Fzchbu%2Fseller_24360%2F%22%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3BN%3Bs%3A3%3A%22url%22%3Bs%3A76%3A%22%2Fzchbu%2Flocal%2Ftemplates%2Fbsclassified%2Fassets%2Fplugins%2Fswipperswiper.min.js.map%2F%22%3B%7Di%3A3%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3Bs%3A30%3A%22%D0%97%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8++%D1%83+RD-motors%22%3Bs%3A3%3A%22url%22%3Bs%3A20%3A%22%2Fzchbu%2Fseller_24360%2F%22%3B%7Di%3A4%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3BN%3Bs%3A3%3A%22url%22%3Bs%3A76%3A%22%2Fzchbu%2Flocal%2Ftemplates%2Fbsclassified%2Fassets%2Fplugins%2Fswipperswiper.min.js.map%2F%22%3B%7Di%3A5%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3Bs%3A30%3A%22%D0%97%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8++%D1%83+RD-motors%22%3Bs%3A3%3A%22url%22%3Bs%3A20%3A%22%2Fzchbu%2Fseller_24360%2F%22%3B%7Di%3A6%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3BN%3Bs%3A3%3A%22url%22%3Bs%3A76%3A%22%2Fzchbu%2Flocal%2Ftemplates%2Fbsclassified%2Fassets%2Fplugins%2Fswipperswiper.min.js.map%2F%22%3B%7Di%3A7%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3Bs%3A30%3A%22%D0%97%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8++%D1%83+RD-motors%22%3Bs%3A3%3A%22url%22%3Bs%3A20%3A%22%2Fzchbu%2Fseller_24360%2F%22%3B%7Di%3A8%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3BN%3Bs%3A3%3A%22url%22%3Bs%3A76%3A%22%2Fzchbu%2Flocal%2Ftemplates%2Fbsclassified%2Fassets%2Fplugins%2Fswipperswiper.min.js.map%2F%22%3B%7Di%3A9%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3Bs%3A30%3A%22%D0%97%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8++%D1%83+RD-motors%22%3Bs%3A3%3A%22url%22%3Bs%3A20%3A%22%2Fzchbu%2Fseller_24360%2F%22%3B%7D%7D',
}

headers = {
    'authority': 'bamper.by',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,be;q=0.6',
    'cache-control': 'max-age=0',
    # 'cookie': '_ym_uid=1674247344783474644; _ym_d=1674247344; BX_USER_ID=97350de67a97c61981abff6891ccd6f5; _ga=GA1.2.1460552130.1674247344; USER_CLICK_ID=c4s7gr1q; _gid=GA1.2.1630214685.1678125434; _ym_isad=1; PHPSESSID=pnhrip3agp3enc174esgdakk88; _gat_UA-31751536-4=1; BITRIX_SM_aLastSearch=a%3A10%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3BN%3Bs%3A3%3A%22url%22%3Bs%3A76%3A%22%2Fzchbu%2Flocal%2Ftemplates%2Fbsclassified%2Fassets%2Fplugins%2Fswipperswiper.min.js.map%2F%22%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3Bs%3A30%3A%22%D0%97%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8++%D1%83+RD-motors%22%3Bs%3A3%3A%22url%22%3Bs%3A20%3A%22%2Fzchbu%2Fseller_24360%2F%22%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3BN%3Bs%3A3%3A%22url%22%3Bs%3A76%3A%22%2Fzchbu%2Flocal%2Ftemplates%2Fbsclassified%2Fassets%2Fplugins%2Fswipperswiper.min.js.map%2F%22%3B%7Di%3A3%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3Bs%3A30%3A%22%D0%97%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8++%D1%83+RD-motors%22%3Bs%3A3%3A%22url%22%3Bs%3A20%3A%22%2Fzchbu%2Fseller_24360%2F%22%3B%7Di%3A4%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3BN%3Bs%3A3%3A%22url%22%3Bs%3A76%3A%22%2Fzchbu%2Flocal%2Ftemplates%2Fbsclassified%2Fassets%2Fplugins%2Fswipperswiper.min.js.map%2F%22%3B%7Di%3A5%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3Bs%3A30%3A%22%D0%97%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8++%D1%83+RD-motors%22%3Bs%3A3%3A%22url%22%3Bs%3A20%3A%22%2Fzchbu%2Fseller_24360%2F%22%3B%7Di%3A6%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3BN%3Bs%3A3%3A%22url%22%3Bs%3A76%3A%22%2Fzchbu%2Flocal%2Ftemplates%2Fbsclassified%2Fassets%2Fplugins%2Fswipperswiper.min.js.map%2F%22%3B%7Di%3A7%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3Bs%3A30%3A%22%D0%97%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8++%D1%83+RD-motors%22%3Bs%3A3%3A%22url%22%3Bs%3A20%3A%22%2Fzchbu%2Fseller_24360%2F%22%3B%7Di%3A8%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3BN%3Bs%3A3%3A%22url%22%3Bs%3A76%3A%22%2Fzchbu%2Flocal%2Ftemplates%2Fbsclassified%2Fassets%2Fplugins%2Fswipperswiper.min.js.map%2F%22%3B%7Di%3A9%3Ba%3A2%3A%7Bs%3A5%3A%22title%22%3Bs%3A30%3A%22%D0%97%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8++%D1%83+RD-motors%22%3Bs%3A3%3A%22url%22%3Bs%3A20%3A%22%2Fzchbu%2Fseller_24360%2F%22%3B%7D%7D',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

response = requests.get('https://bamper.by/zchbu/seller_24360/', cookies=cookies, headers=headers)

# with open('site.html', 'r', encoding='utf-8') as file:
#     site_text = file.read()
soup = BeautifulSoup(response.text, 'lxml')
div_data = soup.find('div', class_='tab-pane active').find_all('div', class_='item-list')
output = []
i = 0

for data in div_data:
    h5 = data.find('h5', class_='add-title').find('a').text.split(' к ')

    category = h5[0][:-1].strip()

    car = h5[1].split(',')[0].strip()

    year = h5[1].split(',')[1][:-5].strip()

    span_data = data.find('div', class_='add-details').find('span', class_='info-row')
    if len(span_data.find_all('div')) > 1:
        volume_and_fuel = span_data.div.text.strip()
        description = span_data.div.next_sibling.next_sibling.text.strip()
    else:
        volume_and_fuel = ''
        description = span_data.div.text.strip()

    if volume_and_fuel:
        description = volume_and_fuel + ', ' + description

    article = span_data.find('span', class_='date').text.strip()

    price_list = data.find('h2', class_='item-price').span.strings
    price = next(price_list).strip()

    image_list = data.find('div', class_='add-image').find_all('img')
    images = ['https://bamper.by/' + item['src'] for item in image_list]

    print(f'{i} item')
    print('volume = ' + volume_and_fuel.strip())
    print('desc = ' + description.strip())
    print('article = ' + article)
    print(f'images = {images}')
    print(f'price = {price.strip()} \n')
    temp_data = {
        'category': category,
        'car': car,
        'car_year': int(year),
        'description': description,
        'article': article,
        'price': int(price),
    }
    output.append(temp_data)

    # for it, url in enumerate(images):
    #     res = requests.get(url)
    #
    #     if res.status_code == 200:
    #         with open(f'photo/image_{i}_{it}.jpg', 'wb') as f:
    #             f.write(res.content)
    #     else:
    #         print('Ошибка ' + str(res.status_code))
    i += 1
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(output, file, ensure_ascii=False)

