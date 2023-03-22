import json
from django.utils import timezone
from mainapp.models import PartCard, Cars, Category, Photo
with open('/home/vlad/Programs/RD_Motors/parser/data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

iter = 20
for dct in data:
    category = Category.objects.get(name=dct['category'] + '\n')
    model = ' '.join(dct['car'].split(' ')[1:])
    car = Cars.objects.get(name=dct['car'].split(' ')[0], model=model)
    part = PartCard.objects.create(id=iter, category=category, car=car, car_year=dct['car_year'], description=dct['description'], article=dct['article'], price=dct['price'], published_date=timezone.now())
    if dct['volume']:
        part.volume = dct['volume']
    if dct['fuel']:
        part.fuel = dct['fuel']
    for image in dct['images']:
        img = Photo.objects.create(part_card=part)
        img.save()
        img.image.save(image.split('/')[-1], open(image, 'rb'), save=True)
        img.save()
    iter += 1
