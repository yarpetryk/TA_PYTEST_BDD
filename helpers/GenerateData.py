from faker import Faker


fake = Faker()

def first_name():
    name = fake.first_name()
    return name

def last_name():
    name = fake.last_name()
    return name

def full_name():
    full_name = fake.first_name()
    return full_name

def zip_code():
    id_code = fake.postcode()
    return id_code

def email():
    lemberg_email = str(first_name() + last_name() + "@test.co.uk")
    return lemberg_email

def address():
    address = fake.address()
    return address

def city():
    city = fake.city()
    return city

def phone_number():
    phone_number = fake.phone_number()
    return phone_number

def birth_day():
    birth_date = f'{fake.date_of_birth():%m/%d/%Y}'
    return birth_date
