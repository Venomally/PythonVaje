import pika

# Povezivanje
credentials = pika.PlainCredentials('martin', 'martin00')
parameters = pika.ConnectionParameters('149.62.71.186', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()



def callback(ch, method, properties, body):
    print(f"Primljeno: {body.decode()}")

# Povezivanje callback funkcije na queue
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
