"""Billing event producer (confluent-kafka)."""
from confluent_kafka import Producer

producer = Producer({"bootstrap.servers": "kafka:9092"})


def publish_payment(payment: bytes) -> None:
    producer.produce("payments", value=payment)
