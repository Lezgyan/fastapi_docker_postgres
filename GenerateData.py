import psycopg2
from mimesis import Person, Text, Datetime, Generic
from mimesis.enums import Gender
from mimesis.locales import Locale
from random import choice, randint
from datetime import datetime, timedelta

# Инициализация провайдеров

generic_ru = Generic('ru')
text_en = generic_ru.text
datetime_provider = generic_ru.datetime
science_en = generic_ru.science
person_ru = generic_ru.person
text_ru = text_en
# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()

# Установка схемы
cur.execute("SET search_path TO hospital;")

# 1. Добавление отделений
medicines = [
    "Аспирин",
    "Ибупрофен",
    "Парацетамол",
    "Цефтриаксон",
    "Амоксициллин",
    "Азитромицин",
    "Метформин",
    "Лозартан",
    "Аторвастатин",
    "Омепразол",
    "Левотироксин",
    "Метопролол",
    "Симвастатин",
    "Габапентин",
    "Рамиприл",
    "Амлодипин",
    "Диклофенак",
    "Дротаверин",
    "Фуросемид",
    "Эналаприл",
    "Кларитин",
    "Супрастин",
    "Цетрин",
    "Димедрол",
    "Нурофен",
    "Де-нол",
    "Креон",
    "Панкреатин",
    "Мезим",
    "Ренни",
    "Алмагель",
    "Нольпаза",
    "Эспумизан",
    "Лоперамид",
    "Смекта",
    "Имодиум",
    "Анальгин",
    "Кеторол",
    "Кетонал",
    "Мидокалм",
    "Новокаин",
    "Лидокаин",
    "Дексаметазон",
    "Преднизолон",
    "Сальбутамол",
    "Беродуал",
    "Флуимуцил",
    "Лазолван",
    "Амбробене",
    "АЦЦ",
    "Гексорал",
    "Септолете",
    "Тантум Верде"
]

diseases = [
    "Артериальная гипертензия",
    "Сахарный диабет",
    "Ишемическая болезнь сердца",
    "Астма",
    "Хроническая обструктивная болезнь легких (ХОБЛ)",
    "Пневмония",
    "Туберкулез",
    "Гепатит B",
    "Гепатит C",
    "Малярия",
    "Лихорадка денге",
    "Грипп",
    "Вирус иммунодефицита человека (ВИЧ)",
    "Инсульт",
    "Болезнь Паркинсона",
    "Болезнь Альцгеймера",
    "Артрит",
    "Остеопороз",
    "Рак легкого",
    "Рак молочной железы",
    "Рак простаты",
    "Рак толстой кишки",
    "Лейкемия",
    "Лимфома",
    "Эпилепсия",
    "Мигрень",
    "Анемия",
    "Заболевания щитовидной железы",
    "Псориаз",
    "Экзема",
    "Подагра",
    "Серповидно-клеточная анемия",
    "Почечная недостаточность",
    "Инфекция мочевыводящих путей",
    "Язвенная болезнь желудка",
    "Гастрит",
    "Синдром раздраженного кишечника",
    "Болезнь Крона",
    "Язвенный колит",
    "Целиакия",
    "Ожирение",
    "Депрессия",
    "Тревожные расстройства",
    "Биполярное расстройство",
    "Шизофрения",
    "Синдром дефицита внимания и гиперактивности (СДВГ)",
    "Расстройства аутистического спектра",
    "Дислексия",
    "Рассеянный склероз",
    "Системная красная волчанка",
    "Ревматоидный артрит"
]

departments = [
    'Кардиология',
    'Неврология',
    'Онкология',
    'Педиатрия',
    'Ортопедия',
    'Травматология',
    'Дерматология',
    'Гастроэнтерология',
    'Офтальмология',
    'Радиология'
]

for dept_name in departments:
    cur.execute(
        "INSERT INTO departments (name) VALUES (%s)",
        (dept_name,)
    )
print("УРААА!!")
conn.commit()

# 2. Добавление должностей
positions = [
    'Хирург',
    'Медсестра',
    'Терапевт',
    'Рентгенолог',
    'Анестезиолог',
    'Педиатр',
    'Кардиолог',
    'Невролог',
    'Ортопед',
    'Дерматолог'
]

for pos_name in positions:
    cur.execute(
        "INSERT INTO positions (name) VALUES (%s)",
        (pos_name,)
    )
print("УРААА!!")
conn.commit()

# 3. Добавление типов квалификаций
qualification_types = [
    'Сертифицированный специалист',
    'Прошел ординатуру',
    'Доктор медицинских наук',
    'Кандидат медицинских наук',
    'Специалист',
    'Консультант',
    'Интерн',
    'Резидент',
    'Профессор'
]

for qual_name in qualification_types:
    cur.execute(
        "INSERT INTO qualification_type (name) VALUES (%s)",
        (qual_name,)
    )
print("УРААА!!")
conn.commit()

# 4. Добавление пациентов
num_patients = 200

for _ in range(num_patients):
    full_name = person_ru.full_name()
    date_of_birth = person_ru.birthdate(1950, 2010)
    snils = ''.join([str(randint(0, 9)) for _ in range(11)])
    medical_policy = ''.join([str(randint(0, 9)) for _ in range(16)])
    cur.execute(
        "INSERT INTO patients (full_name, date_of_birth, snils, medical_policy) VALUES (%s, %s, %s, %s)",
        (full_name, date_of_birth, snils, medical_policy)
    )
print("УРААА!!")
conn.commit()

# 5. Добавление заболеваний
cnt = 1
for des in diseases:
    disease_name = des
    cnt += randint(1, 30)
    icd_code = f"ICD-{cnt}.{randint(0, 9)}"
    description = text_en.sentence()
    cur.execute(
        "INSERT INTO diseases (name, icd_code, description) VALUES (%s, %s, %s)",
        (disease_name, icd_code, description)
    )
print("УРААА!!")
conn.commit()

# 6. Добавление типов операций
operation_types_list = [
    'Аппендэктомия',
    'Шунтирование коронарных артерий',
    'Кесарево сечение',
    'Тонзиллэктомия',
    'Замена тазобедренного сустава',
    'Замена коленного сустава',
    'Гистерэктомия',
    'Удаление желчного пузыря',
    'Операция катаракты',
    'Ангиопластика'
]

for op_name in operation_types_list:
    cur.execute(
        "INSERT INTO operation_types (name) VALUES (%s)",
        (op_name,)
    )
print("УРААА!!")
conn.commit()

# 7. Добавление лекарств

for med in medicines:
    medicine_name = med
    description = text_en.sentence()
    cur.execute(
        "INSERT INTO medicine (name, description) VALUES (%s, %s)",
        (medicine_name, description)
    )
print("УРААА!!")
conn.commit()

# Получение списков для внешних ключей
cur.execute("SELECT position_id FROM positions")
positions_list = [row[0] for row in cur.fetchall()]

cur.execute("SELECT department_id FROM departments")
departments_list = [row[0] for row in cur.fetchall()]

# 8. Добавление врачей
num_doctors = 100

for _ in range(num_doctors):
    full_name = person_ru.full_name()
    position_id = choice(positions_list)
    department_id = choice(departments_list)
    cur.execute(
        "INSERT INTO doctors (full_name, position_id, department_id) VALUES (%s, %s, %s)",
        (full_name, position_id, department_id)
    )
print("УРААА!!")
conn.commit()

# Получение списка врачей
cur.execute("SELECT doctor_id FROM doctors")
doctors_list = [row[0] for row in cur.fetchall()]

# 9. Добавление палат
for dept_id in departments_list:
    for i in range(2):
        count_bunk = randint(10, 30)
        name = f"Палата {i+1}"
        cur.execute(
            "INSERT INTO ward (count_bunk, name, department_id) VALUES (%s, %s, %s)",
            (count_bunk, name, dept_id)
        )
print("УРААА!!")
conn.commit()

# Получение списка палат
cur.execute("SELECT id FROM ward")
wards_list = [row[0] for row in cur.fetchall()]

# 10. Добавление медицинских историй
cur.execute("SELECT patient_id FROM patients")
patients_list = [row[0] for row in cur.fetchall()]

cur.execute("SELECT disease_id FROM diseases")
diseases_list = [row[0] for row in cur.fetchall()]

num_histories = num_patients * 2

for _ in range(num_histories):
    patient_id = choice(patients_list)
    disease_id = choice(diseases_list)
    doctor_id = choice(doctors_list)
    admission_date = datetime_provider.date(start=2015, end=2023)
    discharge_date = None
    if randint(0, 1):
        discharge_date = admission_date + timedelta(days=randint(1, 20))
    notes = text_ru.sentence()
    ward_id = choice(wards_list)
    cur.execute(
        "INSERT INTO medical_history (patient_id, disease_id, doctor_id, admission_date, discharge_date, notes, ward_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (patient_id, disease_id, doctor_id, admission_date, discharge_date, notes, ward_id)
    )
print("УРААА!!")
conn.commit()

# Получение списка историй болезней
cur.execute("SELECT history_id FROM medical_history")
histories_list = [row[0] for row in cur.fetchall()]

# 11. Добавление операций
cur.execute("SELECT operation_type_id FROM operation_types")
operation_types_ids = [row[0] for row in cur.fetchall()]

num_operations = 400

for _ in range(num_operations):
    history_id = choice(histories_list)
    doctor_id = choice(doctors_list)
    operation_type_id = choice(operation_types_ids)
    operation_date = datetime_provider.date(start=2015, end=2023)
    description = text_ru.sentence()
    cur.execute(
        "INSERT INTO operations (history_id, doctor_id, operation_type_id, operation_date, description) VALUES (%s, %s, %s, %s, %s)",
        (history_id, doctor_id, operation_type_id, operation_date, description)
    )
print("УРААА!!")
conn.commit()

# 12. Добавление связей между операциями и квалификациями
cur.execute("SELECT id FROM qualification_type")
qualification_types_ids = [row[0] for row in cur.fetchall()]

for operation_type_id in operation_types_ids:
    num_qualifications = randint(1, 3)
    qualification_ids = [choice(qualification_types_ids) for _ in range(num_qualifications)]
    for qualification_id in qualification_ids:
        cur.execute(
            "INSERT INTO operation_to_qualification_type (operation_type_id, qualification_type_id) VALUES (%s, %s)",
            (operation_type_id, qualification_id)
        )
print("УРААА!!")
conn.commit()

# 13. Добавление связей между врачами и квалификациями
for doctor_id in doctors_list:
    num_qualifications = randint(1, 3)
    qualification_ids = [choice(qualification_types_ids) for _ in range(num_qualifications)]
    for qualification_id in qualification_ids:
        cur.execute(
            "INSERT INTO qualification_doctor (doctor_id, qualification_id) VALUES (%s, %s)",
            (doctor_id, qualification_id)
        )
print("УРААА!!")
conn.commit()

# 14. Добавление курсов лечения
num_courses = num_histories

for _ in range(num_courses):
    history_id = choice(histories_list)
    description = text_ru.sentence()
    receipt_date = datetime_provider.date(start=2015, end=2023)
    doctor_id = choice(doctors_list)
    cur.execute(
        "INSERT INTO course_of_treatment (history_id, description, receipt_date, doctor_id) VALUES (%s, %s, %s, %s)",
        (history_id, description, receipt_date, doctor_id)
    )
print("УРААА!!")
conn.commit()

# Получение списка курсов лечения
cur.execute("SELECT id FROM course_of_treatment")
courses_list = [row[0] for row in cur.fetchall()]

# 15. Добавление приемов пациентов
cur.execute("SELECT id FROM medicine")
medicine_list = [row[0] for row in cur.fetchall()]

num_receptions = num_histories * 2

for _ in range(num_receptions):
    date = datetime_provider.date(start=2015, end=2023)
    description = text_ru.sentence()
    course_of_treatment_id = choice(courses_list)
    medication_id = choice(medicine_list)
    cur.execute(
        "INSERT INTO patient_reception (date, description, course_of_treatment_id, medication_id) VALUES (%s, %s, %s, %s)",
        (date, description, course_of_treatment_id, medication_id)
    )
print("УРААА!!")
conn.commit()

# Закрытие соединения
cur.close()
conn.close()
