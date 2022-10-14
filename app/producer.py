import os
from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
from time import sleep
from datetime import datetime

KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")
KAFKA_PORT = os.getenv("KAFKA_PORT", "9092")

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
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        email = f"user_{current_date}@gmail.com"
        producer.send(topic_name, email.encode())
        sleep(2)
        print(f"Published message to message broker. User email: {email}")
