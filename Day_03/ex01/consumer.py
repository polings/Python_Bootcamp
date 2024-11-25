import argparse
import json
import logging
import sys
import time
import redis

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)


def get_args():
    """
    Parse command-line arguments.

    Parameters:
        None

    Returns:
        Namespace with attributes:
        - bad_guys: The input provided for the bad guys' numbers (type: str).
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--bad_guys", help="Bad guys numbers")
    return parser.parse_args()


def swap_recipients(json_message: dict, recipients: list):
    """
    Swap the sender and receiver in a JSON message based on recipient list.

    Parameters:
        json_message (dict): A JSON message containing 'amount' and metadata with 'from' and 'to' fields.
        recipients (list): A list of recipient identifiers to bad guys.

    Returns:
        dict: A new JSON message with swapped 'from' and 'to' fields if the conditions are met,
              otherwise returns the original sender and receiver.
    """
    amount = json_message["amount"]
    sender = json_message["metadata"]["from"]
    receiver = json_message["metadata"]["to"]
    if amount > 0 and str(receiver) in recipients:
        return {"metadata": {"from": receiver, "to": sender}, "amount": amount}
    return {"metadata": {"from": sender, "to": receiver}, "amount": amount}


if __name__ == "__main__":
    bad_guys_numbers = get_args().bad_guys.split(',')
    with redis.Redis(host='localhost', port=6379, db=0) as redis_client:
        queue_name = "channel_1"
        p = redis_client.pubsub()
        p.subscribe(queue_name)
        while True:
            item = redis_client.brpop(queue_name)
            if item:
                queue_name, message = item
                message = message.decode('utf-8')
                json_data = json.loads(message)
                data = swap_recipients(json_data, bad_guys_numbers)
                logging.info(json.dumps(data))
            time.sleep(0.01)
