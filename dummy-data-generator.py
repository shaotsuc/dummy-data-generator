from faker import Faker
import csv
import random
import os.path
fake = Faker()


## variable for columns
date = fake.date_time()
username = fake.user_name()
brand = random.choice(['brand1','brand2','brand3','brand'])
segment = random.choice(['Occasional','Potential','VIP','Inactive'])
deposit_eur = random.randint(0,10000)
revenue_eur = random.randint(-10000,10000)
fee_eur = random.randint(0,100)
cost_eur = random.randint(0,10000)
is_active = random.choice(['TRUE', 'FALSE'])


## dummy dict
users = {
        'date': date,
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
            fields = ['date', 'username', 'brand', 'segment', 'deposit_eur','revenue_eur','cost_eur','fee_eur','is_active']
            writer = csv.DictWriter(f, fieldnames=fields)
            if not file_exists:
                writer.writeheader()
            else: 
                writer.writerow(users)