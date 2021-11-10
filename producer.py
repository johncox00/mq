from basicClient import BasicPikaClient

class BasicMessageSender(BasicPikaClient):

    def declare_queue(self, queue_name):
        print(f"Trying to declare queue({queue_name})...")
        self.channel.queue_declare(queue=queue_name)

    def send_message(self, exchange, routing_key, body):
        channel = self.connection.channel()
        channel.basic_publish(exchange=exchange,
                              routing_key=routing_key,
                              body=body)
        print(f"Sent message. Exchange: {exchange}, Routing Key: {routing_key}, Body: {body}")
    
    def declare_exchange(self, exchange_name):
        print(f"Trying to declare exchange({exchange_name})...")
        self.channel.exchange_declare(exchange=exchange_name,
                         exchange_type='fanout')

    def close(self):
        self.channel.close()
        self.connection.close()

if __name__ == "__main__":

    # Initialize Basic Message Sender which creates a connection
    # and channel for sending messages.
    basic_message_sender = BasicMessageSender()

    # Declare a queue
    basic_message_sender.declare_queue("hello world queue")

    # Declare an exchange
    basic_message_sender.declare_exchange("pubsub")

    # # Send a message to the queue.
    # basic_message_sender.send_message(exchange="", routing_key="hello world queue", body=b'Hello World!')

    # Broadcast a message.
    basic_message_sender.send_message(exchange="pubsub", routing_key='', body=b"To all the consumers out there!")

    # Close connections.
    basic_message_sender.close()