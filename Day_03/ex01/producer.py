import json
import logging
import sys
import time
import redis
import random

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)


def generate_message():
    """
    Generate a random message containing a sender ID, receiver ID, and a transaction amount.

    Parameters:
        None

    Returns:
        dict: A dictionary containing:
            - metadata (dict): A dictionary with 'from' and 'to' keys representing
              the sender and receiver IDs respectively.
            - amount (int): A randomly generated transaction amount between -10000 and 10000,
              with increments of 1000.
    """
    num_length = 10
    numbers = '0123456789'
    start, stop, step = -10000, 10001, 1000
    sender = int(''.join(random.choice(numbers) for _ in range(num_length)))
    receiver = int(''.join(random.choice(numbers) for _ in range(num_length)))
    amount = random.randrange(start, stop, step)
    return {"metadata": {"from": sender, "to": receiver}, "amount": amount}


def produce_messages(queue_name, num_messages):
    """
    Produce JSON messages and push them to a Redis queue.

    Parameters:
    queue_name (str): The name of the Redis queue to which messages will be sent.
    num_messages (int): The number of JSON messages to generate and send.

    Returns:
    None
    """
    num_messages = 3 # use for testing
    test_messages = [ # use for testing
        {"metadata": {"from": 1111111111, "to": 2222222222}, "amount": 10000},
        {"metadata": {"from": 3333333333, "to": 4444444444}, "amount": -3000},
        {"metadata": {"from": 2222222222, "to": 5555555555}, "amount": 5000}
    ]
    for i in range(num_messages):
        # json_message = generate_message() # use for generating message
        # message = json.dumps(json_message)
        message = json.dumps(test_messages[i]) # use for testing
        redis_client.lpush(queue_name, message)
        logging.info(message)
        time.sleep(1)


if __name__ == "__main__":
    with redis.Redis(host='localhost', port=6379, db=0) as redis_client:
        produce_messages("channel_1", 3)
