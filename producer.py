import json
from pykafka import KafkaClient

bootstrap_servers = 'localhost:9092'


def pykafka_producer(use_rdkafka=True):
    """Example pykafka-producer to be used."""
    client = KafkaClient(hosts=bootstrap_servers)
    topic = client.topics[b'logstash']
    with topic.get_producer(use_rdkafka=use_rdkafka) as producer:
        for i in xrange(0, 100):
            msg_payload = json.dumps({'key': i, 'key_2': -1 * i})
            producer.produce(msg_payload)


if __name__ == "__main__":
    pykafka_producer()
