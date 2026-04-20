import pika
import sys

host = '149.62.71.186'
credentials = pika.PlainCredentials('martin', 'martin00')
parameters = pika.ConnectionParameters(host=host, credentials = credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

name = input("ime: ")

while True:
    msg  = input(f"{name}: ")
    channel.basic_publish(exchange='logs', routing_key='', body=f'{name}: {msg}')
    connection.close()
