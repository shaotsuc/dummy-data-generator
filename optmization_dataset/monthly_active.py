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

months = ['2024-01-01', '2024-02-01', '2024-03-01','2024-04-01','2024-05-01',]
time_of_day = ['MORNING (06-12)', 'AFTERNOON (13-18)', 'NIGHT (19-00)']
yes_or_no = ['TRUE', 'FALSE']


## Main script for dataset
i = 0
while i < 30000:
    ## variable for columns
    transaction_month = random.choice(months)
    user = random.choice(user_list)
    game = random.choice(game_list)
    most_played_TOD = random.choice(time_of_day)
    is_active_prev_month = random.choice(yes_or_no)
    is_active_curr_month = random.choice(yes_or_no)


    ## users dict
    users = {
            'transaction_month': transaction_month,
            'user': user, 
            'game': game,
            'most_played_TOD': most_played_TOD,
            'is_active_prev_month': is_active_prev_month,
            'is_active_curr_month': is_active_curr_month,
            }

## fieldsname list
    fields = []
    for k in users:
        fields.append(k)

## CSV file generator 
    file_exists = os.path.isfile("monthly_kpis.csv")
    with open('monthly_kpis.csv','a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)

            if not file_exists:
                writer.writeheader()
            else: 
                writer.writerow(users)  
    i += 1
