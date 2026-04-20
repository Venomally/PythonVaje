import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()


# Naloga  a)
channel.queue_declare(queue="hello", durable=True, arguments={"x-queue-type": "quorum"})

channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Hello World!'")
