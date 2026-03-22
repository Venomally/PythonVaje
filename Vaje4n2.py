import pika


credentials = pika.PlainCredentials("martin", "martin00")
parameters = pika.ConnectionParameters("149.62.71.186", credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue="hello Amer", durable=True)
