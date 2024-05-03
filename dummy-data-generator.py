from faker import Faker
import csv
import random
fake = Faker()


## variable for columns
date = fake.date_time()
username = fake.user_name()
brand = random(['brand1,brand2,brand3,brand4'])
segment = random(['Occasional','Potential','VIP','Inactive'])
deposit_eur = random.randint(0,10000)
revenue_eur = random.randint(-10000,10000)
fee_eur = random.randint(0,100)
cost_eur = random.randint(0,10000)
is_active = random('TRUE', 'FALSE')


## dummy data
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


with open('users.csv','w', newline='') as csv_file:
    fieldnames = ['date', 'username', 'brand', 'segment', 'deposit_eur','revenue_eur','cost_eur','fee_eur','is_active']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(users)