great_old_ones = """
Azathoth Baalzebub Cthulhu Dagon Elder Fenelon Hastur Hastur Innsmouth Jzahar
Xulophant Lirgrot Migo Nyarlathotep Othokon Phnglui Rlyeh Safalet Tzatlya
Ubbos Vgaa Shubniggurath Erebus Yuggoth Zinburo Anneke Blottulpa Chaugnar
Dranduil Elgoth Fahlu Glitzul Hiellik Iggdrasil Jogsotthot Kuraltai
Lingvard Migo Niarlothotep Oggotai Phnglui Quinyahth Raggas Sargot Tlentx Unnauth
Velgor Gangrelt Hargo Tzifraak Arcturus Beldran Coralith Drimgot Eldritch Furgo
Gorgunt Horrent Izzaret Gentakul Kravend Lashutt Murgos Nocturn Orbant Praetor
Kiargunt Rifta Sictor Targant Urmagon Viligent Hendrat Yggvir Jirmokt Krantl
Latreng Mikotah Nyogarn Orvent Platoon Quadrat Ratgarn Sikatra Trekkant Umbraagot
Vergont Gormul Hiltrang Ingrolt Djontral Kragmot Lorgant Morgont Nerbont Orgont
Pargont Quulent Reltant Sugont Trellont Urgont Vagrant Holent Irrant Yotrant Kelont
Lagont Meront Nagont Orgont Peront Queront Rogont Suront Taront Urunt Voront
Huront Irunt Yurunt Karont Loront Murunt Naront Orunt Purunt Queront Roront Suront
Taront Urunt Voront Huront Irunt Yurunt Kuront Wrothgarn Wazalthar Warpshadow
""".lower()
great_old_ones = great_old_ones.split()

import random

# Обучение статистической модели
def build_model(names):
    model = {}
    for name in names:
        name = name.lower()
        for i in range(len(name) - 1):
            current_char = name[i]
            next_char = name[i + 1]
            if current_char not in model:
                model[current_char] = {}
            if next_char not in model[current_char]:
                model[current_char][next_char] = 1
            else:
                model[current_char][next_char] += 1
    return model

# Функция для генерации имен, принимает статистическкую модель, стартовый символ и длину имени
def generate_necronomicon_name(model, starting_char, length):
    current_char = starting_char.lower()
    generated_name = starting_char

    for _ in range(length - 1):
        if current_char not in model or not model[current_char]:
            break
        next_char = random.choices(
            list(model[current_char].keys()),
            list(model[current_char].values())
        )[0]
        generated_name += next_char
        current_char = next_char

    return generated_name.capitalize()

# Создаем модель на основе списка имен great_old_ones
model = build_model(great_old_ones)

# Пример использования
starting_char = 'A'
name_length = 8
generated_name = generate_necronomicon_name(model, starting_char, name_length)
print("Сгенерированное имя:", generated_name)
