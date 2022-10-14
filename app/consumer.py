import os
from kafka import KafkaConsumer
from time import sleep

KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")
KAFKA_PORT = os.getenv("KAFKA_PORT", "9092")


def process_message(email):
    print(f"sending email to {email}")
    sleep(1)  # pretend to do work
    print(f"updating user {email} status to Waiting Confirmation")
    sleep(1)  # pretend to do work
    print("finished processing message")


if __name__ == "__main__":
    print("starting streaming consumer app")
    consumer = KafkaConsumer(
        "user_signups",
        bootstrap_servers=[f"{KAFKA_HOST}:{KAFKA_PORT}"],
        group_id="group1",
    )

    for message in consumer:
        process_message(message.value)
