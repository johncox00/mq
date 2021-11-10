from basicClient import BasicPikaClient

class Consumer:
    def __init__(self, consumer_id):
        channel = BasicPikaClient().channel

        channel.exchange_declare(exchange='pubsub', exchange_type='fanout')

        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange='pubsub', queue=queue_name)

        print(f' [*] Consumer {consumer_id} waiting for messages. To exit press CTRL+C')

        def callback(ch, method, properties, body):
            print(f" [{consumer_id}] {body}")

        channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)

        channel.start_consuming()

