# Проект FitLife - MVP версия 1.0
import io
import sys

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

WATER_PER_KG_ML = 30
ML_IN_LITRE = 1000

user_name = input("Доброго времени суток, пожалуйста, напишите ваше имя: ")

user_age = int(input("Введите ваш возраст: "))

user_weight = float(input("Введите ваш вес в кг (пример: 56.6): "))

user_height = float(input("Введите ваш рост в метрах (пример: 1.77): "))

bmi = round(user_weight / (user_height**2), 1)

water_ml = user_weight * WATER_PER_KG_ML
water_l = water_ml / ML_IN_LITRE

print()
print(f"Отчёт для пользователя: {user_name} ({user_age} лет)")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print("Расчёт окончен. Будьте здоровы!")
