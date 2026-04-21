import pika 


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='My_new_topic', exchange_type='topic')



result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

def callback(ch, method, properties, body):
    velikost, zival, tip = method.routing_key.split('.')
    print(velikost, zival, tip)
    if velikost == 'big':
        channel.basic_publish(exchange='My_new_topic', routing_key='%s.%s.%s' % (velikost, zival, 'resend'), body=body)
        print('Key binding je bil big.*.*, zato imamo resend')
    print("Z binding %r smo prejeli sporočilo %r" % (method.routing_key, body.decode()))

channel.queue_bind(exchange='My_new_topic', queue=queue_name, routing_key='*.fox.*')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Consuming')
channel.start_consuming()
