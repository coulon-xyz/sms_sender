import random
import nexmo
import pandas as pd
import os
import datetime
from config import config

if __name__ == "__main__":
    cwd = os.path.dirname(os.path.abspath(__file__))
    db = pd.read_csv(os.path.join(cwd, 'data', 'db_names.csv'))
    dice_number = random.randint(1, 6)
    print("##############")
    print("date: ", datetime.datetime.now())
    print("dice: ", dice_number)

    if dice_number == 1:
        client = nexmo.Client(key=config.NEXMO_KEY, secret=config.NEXMO_SECRET)

        remote_number = config.REMOTE_PHONE_NUMBER
        firstname = db['firstname'][random.randint(1, len(db))]
        r = client.send_message({
            'from': firstname,
            'to': remote_number,
            'text': '{} est en ligne et te propose un duel !'.format(firstname),
        })
        print("name: ", firstname)
        print(r)
