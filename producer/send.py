import pika

credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

# Conexión a RabbitMQ
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

# Declarar la cola (por si no existe)
channel.queue_declare(queue='hello')

# Enviar mensaje
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
