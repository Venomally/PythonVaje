import pika
import time

credentials = pika.PlainCredentials('martin', 'martin00')
parameters =  pika.ConnectionParameters('149.62.71.186', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='task', durable=True)

def callback(ch, method, properties, body):
    time.sleep(int(body))
    print(f"Task {int(body)} completed!")
    #Ročno ack, ker ni nujno, da task opravimo!
    ch.basic_ack(delivery_tag = method.delivery_tag)

#don't dispatch a new message to a worker until it has processed and acknowledged the previous one
channel.basic_qos(prefetch_count=1)


channel.basic_consume(queue='task', 
                      auto_ack=False,
                      on_message_callback=callback)

print(' [*] Waiting for messages.')
channel.start_consuming()
