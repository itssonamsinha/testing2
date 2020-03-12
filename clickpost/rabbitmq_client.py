import pika
from django.conf import settings


class RabbitmqConnection():

    # CONNECTION_URL is the url of raabitmq connection can be defined in env file
    def __init__(self):
        self.parameters = pika.URLParameters(
            settings.RABBITMQ_CONNECTION_SETTINGS["CONNECTION_URL"])

    def __enter__(self):
        self.connection = pika.BlockingConnection(self.parameters)
        return self.connection

    def __exit__(self, *args):
        self.connection.close()


def publish_message(body):

    with RabbitmqConnection() as connection:
        channel = connection.channel()
        # QUEUE is the name of queue in which messages are pushed can be defined in env file
        channel.basic_publish(exchange='',
                              routing_key=settings.RABBITMQ_CONNECTION_SETTINGS["QUEUE"],
                              body=body)



