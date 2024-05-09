from faker import Faker
import csv
import random
import os.path
from datetime import date
fake = Faker()

## default variables
user_list = []
game_list = []

n = 1
user = 'USER'
game = 'GAME'
while n < 31: 
    new_user = user + str(n)
    user_list.append(new_user)
    if n < 5:
        new_game = game + str(n)
        game_list.append(new_game)
    n += 1

segment_list = ['NORMAL','POTENTIAL','VIP','INACTIVE']
yes_or_no = ['TRUE', 'FALSE']



## Main script for dataset
i = 0
while i < 30000:
    ## variable for columns
    transaction_date = fake.date_between(start_date=date(2024,1,1), end_date=date(2024,5,1))
    user = random.choice(user_list)
    game = random.choice(game_list)
    segment = random.choice(segment_list)
    deposit_eur = random.randint(0,100)
    revenue_eur = random.randint(-100,100)
    cost_eur = random.randint(0,50)
    is_active = random.choice(yes_or_no)

    ## users dict
    users = {
            'transaction_date': transaction_date,
            'user': user, 
            'game': game,
            'segment': segment,
            'deposit_eur': deposit_eur,
            'revenue_eur': revenue_eur,
            'cost_eur': cost_eur,
            'is_active': is_active,
            }
    
## fieldsname list
    fields = []
    for k in users:
        fields.append(k)

## CSV file generator 
    file_exists = os.path.isfile("daily_kpi.csv")
    with open('daily_kpi.csv','a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)

            if not file_exists:
                writer.writeheader()
            else: 
                writer.writerow(users)  
    i += 1
