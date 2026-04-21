import time
import pika
import sys
import numpy as np
import datetime

credentials = pika.PlainCredentials('martin', 'martin00')
parameters =  pika.ConnectionParameters('149.62.71.186', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')



while True:
    time.sleep(1)
    key = np.random.choice(['info', 'warning', 'error', 'OTHER'])
    channel.basic_publish(exchange = 'direct_logs', routing_key = key, body = str(datetime.datetime.now()))

