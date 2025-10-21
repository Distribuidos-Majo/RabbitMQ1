import pika

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

# Conexión a RabbitMQ
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key='error')

# Callback para procesar mensajes
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Consumir mensajes
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
