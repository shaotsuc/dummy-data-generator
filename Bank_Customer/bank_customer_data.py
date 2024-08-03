from faker import Faker
import os.path
import random
from datetime import date
import pandas as pd
fake = Faker()


## default variables
region_list = ['NORTH', 'WEST', 'SOUTH','EAST']
martial_status_list = ['SINGLE', 'MARRIED', 'DIVORCED']
education_list = ['ELEMENTARY','SECONDARY','BACHELOR','MASTER','DOCTORATE']
segment_list = ['Normal','Potential','VIP','Inactive']
fields_list = ['MANAGEMENT','SKILLED WORKER','STUDENT','UNEMPLOYED','RETIRED']
transfer_type_list = ['DEPOSIT','WITHDRAW','TRANSFER']
media_list = ['PHONE','EMAIL','MAIL']
yes_or_no = ['TRUE', 'FALSE']


## Main script for dataset
i = 0
while i < 30000:
    ## variable for columns
    transaction_date = fake.date_between(start_date=date(2023,11,1), end_date=date(2024,8,1))
    bank_number = fake.iban()
    region = random.choice(region_list)
    age = random.randint(0,90)
    martial_status = random.choice(martial_status_list)
    dependant = random.randint(0,4)
    education = random.choice(education_list)
    field_of_activity = random.choice(fields_list)
    active_loan = random.choice(yes_or_no)
    has_credit_card = random.choice(yes_or_no)
    transfer_type = random.choice(transfer_type_list)
    amount = random.randint(1,1000)
    balance = random.randint(-100,100000)
    account_main_fee = random.randint(0,17)
    main_contact_media = random.choice(media_list)


    ## users dict
    users = {
            'transaction_date': transaction_date,
            'bank_number': bank_number,
            'region': region,
            'age': age,
            'martial_status': martial_status,
            'dependant': dependant,
            'education': education,
            'field_of_activity': field_of_activity,
            'active_loan': active_loan,
            'has_credit_card': has_credit_card,
            'transfer_type': transfer_type,
            'amount': amount,
            'balance': balance,
            'account_main_fee': account_main_fee,
            'main_contact_media': main_contact_media,
            }
    
    ## Pandas data frame
    new_users = {k: [v] for k, v in users.items()}
    df = pd.DataFrame.from_dict(new_users)


    ## CSV output
    file_exists = os.path.isfile("Brand-KPIs/brand_kpis_data.csv")
    if not file_exists:
        df.to_csv('Brand-KPIs/brand_kpis_data.csv', index=False)
    else: 
        df.to_csv('Brand-KPIs/brand_kpis_data.csv', mode='a', header=False, index=False) 

    i += 1





