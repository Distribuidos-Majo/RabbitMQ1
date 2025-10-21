import pika
import sys

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Mensaje por defecto'

# Conexión a RabbitMQ
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

# Declarar la cola (por si no existe)
channel.queue_declare(queue='hello')

# Se declara el exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# Enviar mensaje

#channel.basic_publish(exchange='direct_logs',
 #                     routing_key='warning',
 #                    body='Mensaje de warning')

channel.basic_publish(
    exchange='direct_logs',
    routing_key=severity,
    body=message
)

print(" [x] Sent 'Hello World!'")

connection.close()
