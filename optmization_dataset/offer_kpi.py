from faker import Faker
import csv
import random
import os.path
from datetime import date
fake = Faker()


## default variables
user_list = []
game_list = []
offer_id_list = []

n = 1
user = 'USER'
game = 'GAME'
offer = 'OFFER'
while n < 31: 
    new_user = user + str(n)
    user_list.append(new_user)
    
    new_offer = offer + '-' + str(random.randint(123789, 894719))
    offer_id_list.append(new_offer)

    if n < 5:
        new_game = game + str(n)
        game_list.append(new_game)
    n += 1

yes_or_no = ['TRUE', 'FALSE']


## Main script for dataset
i = 0
while i < 30000:
    ## variable for columns
    transaction_date = fake.date_between(start_date=date(2024,1,1), end_date=date(2024,4,1))
    user = random.choice(user_list)
    game = random.choice(game_list)
    offer_id = random.choice(offer_id_list)
    revenue_eur = random.randint(-100,100)
    offer_cost_eur = random.randint(0,100)
    is_using_offer = random.choice(yes_or_no)
    is_active_prev_month = random.choice(yes_or_no)
    is_active_curr_month = random.choice(yes_or_no)


    ## users dict
    users = {
            'transaction_date': transaction_date,
            'user': user, 
            'game': game,
            'offer_id': offer_id,
            'revenue_eur': revenue_eur,
            'offer_cost_eur': offer_cost_eur,
            'is_using_offer': is_using_offer,
            'is_active_prev_month': is_active_prev_month,
            'is_active_curr_month': is_active_curr_month,
            }


## fieldsname list
    fields = []
    for k in users:
        fields.append(k)


## CSV file generator 
    file_exists = os.path.isfile("offer_kpis.csv")
    with open('offer_kpis.csv','a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)

            if not file_exists:
                writer.writeheader()
            else: 
                writer.writerow(users)  
    i += 1
