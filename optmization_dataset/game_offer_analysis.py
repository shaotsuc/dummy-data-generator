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
while n < 101: 
    new_user = user + str(n)
    user_list.append(new_user)

    new_offer = offer + '-' + str(random.randint(123789, 200000))
    offer_id_list.append(new_offer)

    if n < 5:
        new_game = game + str(n)
        game_list.append(new_game)
    n += 1

offer_stage_list = ['CLAIMED', 'USED', 'EXPIRED', 'LOST', 'COMPLETED']
segment_list = ['NORMAL','POTENTIAL','VIP','INACTIVE']
yes_or_no = ['TRUE', 'FALSE']



## Main script for dataset
i = 0
while i < 30000:
    ## variable for columns
    transaction_date = fake.date_between(start_date=date(2023,6,1), end_date=date(2024,4,1))
    user = random.choice(user_list)
    game = random.choice(game_list)
    offer_id = random.choice(offer_id_list)
    offer_stage = random.choice(offer_stage_list)
    active_curr_month_offer = random.choice(yes_or_no)
    active_prev_month_offer = random.choice(yes_or_no)
    active_curr_month_overall = random.choice(yes_or_no)
    active_prev_month_overall = random.choice(yes_or_no)
    deposit_eur = random.randint(0,10000)
    deposit_cnt = random.randint(0,10)
    revenue_eur = random.randint(-100,10000)
    conversion_eur = random.randint(0,100)
    offer_amt_eur = random.randint(1,100)
    offer_cost_eur = random.randint(0,100)

    ## users dict
    users = {
            'transaction_date': transaction_date,
            'user': user, 
            'game': game,
            'offer_id': offer_id,
            'offer_stage': offer_stage,
            'deposit_eur': deposit_eur,
            'deposit_cnt': deposit_cnt,
            'revenue_eur': revenue_eur,
            'conversion_eur': conversion_eur,
            'offer_amt_eur': offer_amt_eur,
            'offer_cost_eur': offer_cost_eur,
            'active_curr_month_offer': active_curr_month_offer,
            'active_prev_month_offer': active_prev_month_offer,
            'active_curr_month_overall': active_curr_month_overall,
            'active_prev_month_overall': active_prev_month_overall,
            }
    
## fieldsname list
    fields = []
    for k in users:
        fields.append(k)

## CSV file generator 
    file_exists = os.path.isfile("game_offer_analysis.csv")
    with open('game_offer_analysis.csv','a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)

            if not file_exists:
                writer.writeheader()
            else: 
                writer.writerow(users)  
    i += 1
