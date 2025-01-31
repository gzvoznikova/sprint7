import random
import string



def fill_adress_field():
    street_name = ['Хорошевская', 'Ленина', 'Гагарина', 'Аустрина', 'Московская', 'Пушкина', 'Лермонтова']
    street = random.choice(street_name)
    house = random.randint(1, 100)
    flat = random.randint(1, 100)
    return f"Москва, {street}, {house}, {flat}"

def generation_new_data_order():
    letters = string.ascii_lowercase
    firstName_new = random.choice(['Иван', 'Петр', 'Игорь', 'Василий'])
    lastName_new = random.choice(['Петров', 'Иванов', 'Смирнов', 'Сидоров'])
    address_new = fill_adress_field()
    metroStation_new = random.choice(['Хорошевская', 'Сокольники', 'Новослободская', 'Рижская'])
    phone_new =  f"+7{random.randint(900, 999)}{random.randint(1000000, 9999999)}"
    rentTime_new = f"{random.randint(1, 28)}"
    deliveryDate_new = f"2025-{random.randint(1, 12)}-{random.randint(1, 28)}"
    comment_new = ''.join(random.choice(letters) for i in range(15))
    color_new = random.choice(['BLACK', 'GREY'])


    return {"firstName": firstName_new,
            "lastName": lastName_new,
            "address": address_new,
            "metroStation": metroStation_new,
            "phone": phone_new,
            "rentTime": rentTime_new,
            "deliveryDate": deliveryDate_new,
            "comment": comment_new,
            "color": color_new
            }



