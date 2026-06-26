"""Consume order events to drive billing (confluent-kafka)."""
from confluent_kafka import Consumer

consumer = Consumer({"group.id": "billing", "bootstrap.servers": "kafka:9092"})
consumer.subscribe(["orders"])


def run():
    while True:
        msg = consumer.poll(1.0)
        if msg is not None:
            charge(msg.value())
