import random
import nexmo

from config import config

if __name__ == "__main__":
    client = nexmo.Client(key=config.NEXMO_KEY, secret=config.NEXMO_SECRET)

    remote_number = config.REMOTE_PHONE_NUMBER

    r = client.send_message({
        'from': 'GoldenB{}'.format(random.randint(1, 100)),
        'to': remote_number,
        'text': 'David est en ligne et te propose un duel !',
    })

    print(r)
