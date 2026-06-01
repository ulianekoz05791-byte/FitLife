# Проект FitLife - MVP версия 1.0
import sys
import io
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


WATER_PEG_KG = 30
ML_IN_LITRE = 1000

user_name = input('Доброго времени суток, пожайлуста, напишите ваше имя:')

user_age = int(input('Введите Ваш возраст:'))

user_weight = float(input('Введите Ваш вес в кг. (пример: 56.6):'))

user_height = float(input('Введите ваш рост в метрах (пример: 1.77):'))

bmi = round(user_weight / (user_height**2), 1)

water_ml = user_weight * WATER_PEG_KG
water_l = water_ml / 1000

print()

print(f'Отчёт для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день ')

print("Расчет окончен. Будьте здоровы!")
