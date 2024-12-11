
#importing needed libraries
from faker import Faker
import pandas as pd

#creating an instance of faker
fake = Faker(locale='yo_NG')   #specifying multiple locales

#creating a function
def create_transactions(num_transactions):
    #creating an empty list to add transactions dictionaries
    transactions_list = []

    #creating transactions dictionary
    for i in range(num_transactions):
        transactions = {}
        transactions['customer_id'] = fake.random_int()
        transactions['customer_name'] = fake.name()
        transactions['transaction_date'] = fake.date()
        transactions['transaction_type'] = fake.random_element(elements=('credit', 'debit', 'transfer', 'withdrawal'))
        transactions['amount'] = fake.random_int()
        transactions['account_type'] = fake.random_element(elements=('current', 'money market', 'senior checking', 'cash management', 'basic savings', 'NRI', 'savings', 'fixed deposit', 'recurring deposit', 'checking', 'domiciliary', 'Cds', 'student checking'))
        transactions['branch_code'] = fake.random_int()
        transactions['transaction_mode'] = fake.random_element(elements=('online', 'ATM', 'ussd', 'counter', 'mobile'))
        transactions['transaction_id'] = fake.random_int()
        transactions_list.append(transactions)
    return pd.DataFrame(transactions_list)

df = create_transactions(4)
path = 'C:/Users/LATEEF/OneDrive/Documents/faker/fakedata.csv'
#df.to_csv(path_or_buf= path, index=True)
print(df)
