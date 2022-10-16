import os
import uuid
import json
from datetime import datetime
from time import sleep

from faker import Faker
from kafka import KafkaAdminClient, KafkaProducer
from kafka.admin import NewTopic

KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")
KAFKA_PORT = os.getenv("KAFKA_PORT", "9092")
SLEEP_INTERVAL = 0.005

if __name__ == "__main__":

    topic_name = "user_signups"

    try:
        # Create Kafka topic
        topic = NewTopic(name=topic_name, num_partitions=1, replication_factor=1)
        admin = KafkaAdminClient(bootstrap_servers=f"{KAFKA_HOST}:{KAFKA_PORT}")
        admin.create_topics([topic])
    except Exception:
        print(f"Topic {topic_name} is already created")

    producer = KafkaProducer(bootstrap_servers=[f"{KAFKA_HOST}:{KAFKA_PORT}"])

    while True:
        payload = {
            "first_name": Faker().first_name(),
            "last_name": Faker().last_name(),
            "email": Faker().email(),
            "status": "pending",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
        }
        payload = json.dumps(payload)

        producer.send(topic_name, payload.encode())
        sleep(SLEEP_INTERVAL)
        print(f"Published message to message broker. Data: {payload}")
