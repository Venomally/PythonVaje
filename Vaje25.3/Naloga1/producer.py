import pika
import time
import numpy as np

credentials = pika.PlainCredentials('martin', 'martin00')
parameters =  pika.ConnectionParameters('149.62.71.186', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#Queue ostane živ tudi po restartu RabbitMQ (ampak zgolj metadata!)
channel.queue_declare(queue='task', durable=True)

#MQrabbit zagotovi, da bo sporočilo zapisano! ===> PERSISTENT, isto kot delivery_mode = 2
properties = pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)

for i in range(10):
    body=str(np.random.randint(1,10))
    print(f"task {body} given away!")
    channel.basic_publish(exchange='', routing_key='task', body=body, properties=properties)
    