import pika
import sys

credentials = pika.PlainCredentials('martin', 'martin00')
parameters =  pika.ConnectionParameters('149.62.71.186', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue



channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key='info')
channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key='warning')
channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key='error')


print('Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print("Received %r:%r" % (method.routing_key, body.decode()))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)


channel.start_consuming()
