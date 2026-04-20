import pika
import threading
import sys

up_ime = input("Uporabniško ime: ")
len_user = len(up_ime)

credentials = pika.PlainCredentials('martin', 'martin00')
parameters = pika.ConnectionParameters('149.62.71.186', credentials=credentials)

# Dvije odvojene veze - jedna za primanje, jedna za slanje
# (RabbitMQ ne voli kad jedan channel radi dvije stvari odjednom)
connection_recv = pika.BlockingConnection(parameters)
channel_recv = connection_recv.channel()

connection_send = pika.BlockingConnection(parameters)
channel_send = connection_send.channel()

# Postavljanje exchangea i queuea
channel_recv.exchange_declare(exchange='logs', exchange_type='fanout')
channel_send.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel_recv.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel_recv.queue_bind(exchange='logs', queue=queue_name)

# Ova funkcija se poziva automatski kad stigne poruka
def callback(ch, method, properties, body):
    decoded = body.decode()
    # Prikaži poruku samo ako nije naša vlastita
    if decoded[:len_user] != up_ime:
        # \r\033[K - briše trenutni redak (gdje korisnik tipka)
        # pa ispiše poruku, pa vrati prompt natrag
        print(f"\r\033[K{decoded}")
        print(f"{up_ime}: ", end='', flush=True)

# Funkcija koja stalno sluša poruke u pozadini
def slušaj_poruke():
    channel_recv.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel_recv.start_consuming()

# Pokretanje slušanja u zasebnom threadu (pozadina)
thread = threading.Thread(target=slušaj_poruke)
thread.daemon = True  # thread se ugasi kad se ugasi glavni program
thread.start()

# Glavni program - čeka unos korisnika
print(f"Spojeni kao: {up_ime}. Počni pisati!\n")
while True:
    message_content = input(f"{up_ime}: ")
    if message_content.strip() == "":
        continue  # ignoriraj prazne poruke
    message = f"{up_ime}: {message_content}"
    channel_send.basic_publish(exchange='logs', routing_key='', body=message)
