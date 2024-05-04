from faker import Faker
import csv
import random
import os.path
from datetime import date
fake = Faker()


i = 0

while i < 2:
    ## variable for columns
    transaction_date = fake.date_between(start_date=date(2023,12,1), end_date=date(2024,4,1))
    username = fake.user_name()
    brand = random.choice(['Brand 1','Brand 2','Brand 3','Brand 4'])
    segment = random.choice(['Occasional','Potential','VIP','Inactive'])
    deposit_eur = random.randint(0,1000)
    revenue_eur = random.randint(-1000,1000)
    fee_eur = random.randint(0,100)
    cost_eur = random.randint(0,1000)
    is_active = random.choice(['TRUE', 'FALSE'])


    ## dummy dict
    users = {
            'transaction_date': transaction_date,
            'username': username, 
            'brand': brand,
            'segment': segment,
            'deposit_eur': deposit_eur,
            'revenue_eur': revenue_eur,
            'cost_eur': cost_eur,
            'fee_eur': fee_eur,
            'is_active': is_active,
            }

    file_exists = os.path.isfile("users.csv")


    with open('users.csv','a', newline='') as f:
            fields = ['transaction_date', 'username', 'brand', 'segment', 'deposit_eur','revenue_eur','cost_eur','fee_eur','is_active']
            writer = csv.DictWriter(f, fieldnames=fields)

            if not file_exists:
                writer.writeheader()
            else: 
                writer.writerow(users)  

i += 1