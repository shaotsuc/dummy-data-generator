from faker import Faker
import csv
import random
import os.path
from datetime import date
fake = Faker()


i = 0

while i < 30000:
    ## variable for columns
    transaction_date = fake.date_between(start_date=date(2024,1,1), end_date=date(2024,4,1))
    username = fake.user_name()
    brand = random.choice(['Brand 1','Brand 2','Brand 3','Brand 4'])
    segment = random.choice(['Occasional','Potential','VIP','Inactive'])
    offer = random.choice(['Voucher', 'Gift Card', 'Loyalty Program', 'Promotion'])
    most_played_TOD = random.choice(['Morning (06-12)', 'Afternoon (13-18)', 'Night (19-00)'])
    deposit_eur = random.randint(0,100)
    revenue_eur = random.randint(-100,100)
    fee_eur = random.randint(0,30)
    cost_eur = random.randint(0,50)
    is_active_prev_month = random.choice(['TRUE', 'FALSE'])
    is_active_curr_month = random.choice(['TRUE', 'FALSE'])


    ## dummy dict
    users = {
            'transaction_date': transaction_date,
            'username': username, 
            'brand': brand,
            'segment': segment,
            'offer': offer,
            'most_played_TOD': most_played_TOD,
            'deposit_eur': deposit_eur,
            'revenue_eur': revenue_eur,
            'cost_eur': cost_eur,
            'fee_eur': fee_eur,
            'is_active_prev_month': is_active_prev_month,
            'is_active_curr_month': is_active_curr_month,
            }

    file_exists = os.path.isfile("users.csv")


    with open('users.csv','a', newline='') as f:
            fields = ['transaction_date', 'username', 'brand', 'segment', 'offer', 'most_played_TOD', 'deposit_eur','revenue_eur','cost_eur','fee_eur','is_active_curr_month','is_active_prev_month']
            writer = csv.DictWriter(f, fieldnames=fields)

            if not file_exists:
                writer.writeheader()
            else: 
                writer.writerow(users)  
    i += 1