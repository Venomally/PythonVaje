import pika
import sys

def callback(ch, method, properties, body):
        print(f"Msgs recieved: {body.decode()}")


host = '149.62.71.186'
credentials = pika.PlainCredentials('martin', 'martin00')
parameters =  pika.ConnectionParameters(host=host, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')
result = channel.queue_declare(queue='', exclusive=True)
queue = result.method.queue
channel.queue_bind(exchange='logs', queue=queue)

channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
connection.close()
