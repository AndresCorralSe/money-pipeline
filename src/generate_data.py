import random
from datetime import datetime, timedelta

import pandas as pd 
from faker import Faker

SEED = 42
N_USERS = 200
N_POOLS = 50
N_CONTRIBUTIONS = 1000

random.seed(SEED)
Faker.seed(SEED)
fake = Faker("es_MX")


def generate_users(n):
    rows = []
    for user_id in range(1, n + 1):
        rows.append(
            {"user_id": user_id,
             "full_name": fake.name(),
             "email": fake.unique.email(),
             "created_at": fake.date_time_between(start_date="-2y", end_date="-1y"),
             })
    return pd.DataFrame(rows)

if __name__ == '__main__':
    users = generate_users(N_USERS)
    print(users.head())
    print(users.dtypes)