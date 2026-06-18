# Usamos Python oficial
FROM python:3.12-slim

# Creamos la carpeta de trabajo
WORKDIR /app

# Copiamos todos los archivos a la imagen
COPY . .

# Comando por defecto para correr la automatización en tiempo real
CMD ["python", "-u", "app.py"]