from faker import Faker
import csv
import random
import os.path
from datetime import date
fake = Faker()


i = 0

while i < 30000:
    ## variable for columns
    transaction_date = fake.date_between(start_date=date(2023,11,1), end_date=date(2024,4,1))
    first_name = fake.first_name()
    last_name = fake.last_name()
    region = random.choice(['NORTH', 'WEST', 'SOUTH','EAST'])
    age = random.randint(0,90)
    martial_status = random.choice(['SINGLE', 'MARRIED', 'DIVORCED'])
    dependant = random.randint(0,4)
    education = random.choice(['ELEMENTARY','SECONDARY','BACHELOR','MASTER','DOCTORATE'])
    field_of_activity = random.choice(['MANAGEMENT','SKILLED WORKER','STUDENT','UNEMPLOYED','RETIRED'])
    active_loan = random.choice(['TRUE','FALSE'])
    has_credit_card = random.choice(['TRUE','FALSE'])
    balance = random.randint(-100,100000)
    account_main_fee = random.randint(0,17)
    main_contact_media = random.choice(['PHONE','EMAIL','MAIL'])



    ## dummy dict
    users = {
            'transaction_date': transaction_date,
            'first_name': first_name,
            'last_name': last_name,
            'region': region,
            'age': age,
            'martial_status': martial_status,
            'dependant': dependant,
            'education': education,
            'field_of_activity': field_of_activity,
            'active_loan': active_loan,
            'has_credit_card': has_credit_card,
            'balance': balance,
            'account_main_fee': account_main_fee,
            'main_contact_media': main_contact_media,
            }


    file_exists = os.path.isfile("bank_customer.csv")

    with open('bank_customer.csv','a', newline='') as f:
            fields = ['transaction_date', 'first_name', 'last_name', 'region', 'age', 'martial_status', 'dependant','education','field_of_activity','active_loan','has_credit_card','balance','account_main_fee','main_contact_media']
            writer = csv.DictWriter(f, fieldnames=fields)

            if not file_exists:
                writer.writeheader()
            else: 
                writer.writerow(users)  
    i += 1