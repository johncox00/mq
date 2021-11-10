import ssl
import os
import pika
from dotenv import load_dotenv

load_dotenv()

class BasicPikaClient:

    def __init__(self):
        # SSL Context for TLS configuration of Amazon MQ for RabbitMQ
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')
        rabbitmq_broker_id = os.getenv('MQ_BROKER')
        rabbitmq_user = os.getenv('MQ_USER')
        rabbitmq_password = os.getenv('MQ_PW')
        region = os.getenv('MQ_REGION', 'us-east-1')
        url = f"amqps://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_broker_id}.mq.{region}.amazonaws.com:5671"
        parameters = pika.URLParameters(url)
        parameters.ssl_options = pika.SSLOptions(context=ssl_context)

        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()