# Usa una imagen base oficial de Python
FROM python:3.12

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias (requirements.txt) al contenedor
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido de la aplicación al contenedor
COPY . .

# Expone el puerto en el que corre la aplicación (Flask usa 5000 por defecto)
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python3", "app.py"]
