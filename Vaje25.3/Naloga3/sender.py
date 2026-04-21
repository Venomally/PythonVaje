import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


message = "Vsebine poslanega sporucila"

channel.basic_publish(exchange='my_new_topic', routing_key='small.fox.original', body=message)
channel.basic_publish(exchange='my_new_topic', routing_key='big.fox.original', body=message)
channel.basic_publish(exchange='my_new_topic', routing_key='small.cat.original', body=message)
channel.basic_publish(exchange='my_new_topic', routing_key='big.cat.original', body=message)

connection.close()
