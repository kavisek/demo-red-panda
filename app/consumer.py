import os
import uuid
import psycopg2
import psycopg2.extras
from time import sleep
import json
from kafka import KafkaConsumer

KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")
KAFKA_PORT = os.getenv("KAFKA_PORT", "9092")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "postgres")
POSTGRES_SCHEMA = os.getenv("POSTGRES_SCHEMA", "public")
POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")


def process_message(payload):
    print(f"recieved payload from message broker. Data: {payload}")

    # Convert byte to dictionary.
    payload = json.loads(payload)
    print(type(payload))

    # Inserting data into postgres database.
    connection = psycopg2.connect(
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        database=POSTGRES_DATABASE,
    )
    cursor = connection.cursor()
    psycopg2.extras.register_uuid()
    postgres_insert_query = """ INSERT INTO users.events (id, first_name, last_name, email, status, created_at, updated_at) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (
        uuid.uuid4(),
        payload["first_name"],
        payload["last_name"],
        payload["email"],
        payload["status"],
        payload["created_at"],
        payload["updated_at"],
    )
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into events table")


if __name__ == "__main__":
    print("starting streaming consumer app")
    consumer = KafkaConsumer(
        "user_signups",
        bootstrap_servers=[f"{KAFKA_HOST}:{KAFKA_PORT}"],
        group_id="group1",
    )

    for message in consumer:
        process_message(message.value)
