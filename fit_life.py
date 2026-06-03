# Проект FitLife - MVP версия 1.0f
WATER_PER_KG_ML = 30
ML_IN_LITRE = 1000

user_name = input("Доброго времени суток, пожалуйста, напишите ваше имя: ")

while True:
    try:
        user_age = int(input("Введите ваш возраст: "))
        if 10 <= user_age <= 150:
            break
        else:
            print("Пожалуйста, поверьте данные,"
                  " ваш возраст должен быть в диапазоне от 10 до 150 лет")
    except ValueError:
        print("Пожалуйста, введите целое число.")

while True:
    try:
        user_weight = float(input("Введите ваш вес в кг (пример: 56.6): "))
        if 10 <= user_weight <= 200:
            break
        else:
            print("Пожалуйста, поверьте данные,"
                  " вес должен быть в диапазоне от 10 до 200 килограм")
    except ValueError:
        print("Пожалуйста, введите целое число.")

while True:
    try:
        user_height = float(input("Введите ваш рост в метрах "
                                  "(пример: 1.77): "))
        if 1.01 <= user_height <= 2.9:
            break
        else:
            print("Пожалуйста, поверьте данные, "
                  "рост должен быть в диапазоне от 1.01 до 2.9 метров")
    except ValueError:
        print("Пожалуйста, введите целое число.")

last_digit = user_age % 10
last_two_digit = user_age % 100

if 11 <= last_two_digit <= 14:
    name_age = "лет"
elif last_digit == 1:
    name_age = "год"
elif 2 <= last_digit <= 4:
    name_age = "года"
else:
    name_age = "лет"

bmi = round(user_weight / (user_height**2), 1)

if bmi < 16.0:
    bmi_category = "выраженный дифецит массы тела"
elif 16 <= bmi < 18.5:
    bmi_category = "недостаточная (дифицит) масса тела"
elif 18.5 <= bmi < 25:
    bmi_category = "Норма"
elif 25 <= bmi < 30:
    bmi_category = "избыточная масса тела (предожирение)"
elif 30 <= bmi < 35:
    bmi_category = "ожирение первой степени"
elif 35 <= bmi < 40:
    bmi_category = "ожирение второй степени"
else:
    bmi_category = "ожирение третьей степени (морбидное)"

water_ml = user_weight * WATER_PER_KG_ML
water_l = water_ml / ML_IN_LITRE

print()
print(f"Отчёт для пользователя: {user_name} ({user_age} {name_age})")
print(f"Ваш Индекс Массы Тела: {bmi} - {bmi_category}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print("Расчёт окончен. Будьте здоровы!")
