import pika
import time

#the definition of callback function must strictly be such!
def callback(ch, method, properties, body):
    print(f"Msg recieved: {body.decode()}")
    # Simulate processing (replace with your actual processing logic)
    try:
        # Process the message (e.g., print, store in database)
        print(f"Processing message: {body}")
        # Acknowledge the message after successful processing
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Error processing message: {body}")
        # Optionally redeliver the message using nack with requeue=True
        # ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

host = '149.62.71.186'
queue = 'test_queue_2023'
credentials = pika.PlainCredentials('martin', 'martin00')
parameters = pika.ConnectionParameters(host=host, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue=queue)
#auto ack = False !!
channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=False)

for i in range(0, 10):
    time.sleep(1)
    channel.basic_publish(exchange='', routing_key=queue, body=f'my msg n.{i+1}')
    print(f'my msg n.{i+1}')

channel.start_consuming()
