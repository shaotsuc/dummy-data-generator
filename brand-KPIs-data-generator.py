from faker import Faker
import csv
import random
import os.path
from datetime import date
fake = Faker()

## Default variables 
brand_list = []

n = 1
brand = 'Brand'
while n < 5: 
    new_brand = brand + str(n)
    brand_list.append(new_brand)
    n += 1

segment_list = ['NORMAL','POTENTIAL','VIP','INACTIVE']
offer_list = ['VOUCHER', 'GIFT CARD', 'LOYALTY PROGRAM', 'PROMOTION']
tod_list = ['MORNING (06-12)', 'AFTERNOON (13-18)', 'NIGHT (19-00)']
yes_or_no = ['TRUE', 'FALSE']


i = 0

while i < 30000:
    ## variable for columns
    transaction_date = fake.date_between(start_date=date(2024,1,1), end_date=date(2024,4,1))
    username = fake.user_name()
    brand = random.choice(brand_list)
    segment = random.choice(segment_list)
    offer = random.choice(offer_list)
    most_played_TOD = random.choice(tod_list)
    deposit_eur = random.randint(0,100)
    revenue_eur = random.randint(-100,100)
    fee_eur = random.randint(0,30)
    cost_eur = random.randint(0,50)
    is_active_prev_month = random.choice(yes_or_no)
    is_active_curr_month = random.choice(yes_or_no)


    ## users dict
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


## fieldsname list
    fields = []
    for k in users:
        fields.append(k)


## CSV file generator 
    file_exists = os.path.isfile("brand_kpis_data.csv")
    with open('brand_kpis_data.csv','a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)

            if not file_exists:
                writer.writeheader()
            else: 
                writer.writerow(users)  
    i += 1
