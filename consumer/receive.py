import pika

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

# Conexión a RabbitMQ
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declarar la cola (por si no existe)
channel.queue_declare(queue='hello')

# Callback para procesar mensajes
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Consumir mensajes
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
