import pika
import time

def callback(ch, method, properties, body):
        print(f"Msg recieved: {body.decode()}")


host = '149.62.71.186'
queue = 'test_queue_2'
credentials = pika.PlainCredentials('martin', 'martin00')
parameters =  pika.ConnectionParameters(host=host, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
#channel.queue_purge(queue=queue) #če želite izbrisati queue
channel.queue_declare(queue=queue)

#auto ack = True!
channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

for i in range(0,10):
    time.sleep(0.1)
    channel.basic_publish(exchange='', routing_key=queue, body=f'Msg n.{i+1}ššđđ')

#tole bo bralo podatke, a blokiralo program
channel.start_consuming()
