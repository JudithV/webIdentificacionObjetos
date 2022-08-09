# Identificación de objetos en imágenes subidas por un usuario
Código fuente de una web en la que el usuario sube una imagen y obtiene una predicción de qué hay en ella.
El servidor se ejecuta con el comando "python manage.py runserver". La URL principal es localhost:8000/subirImagen. En esta solo es necesario subir la imagen de la cual se quiera predecir su contenido, hacer click en Enviar y esperar un poco a que se realicen los cálculos necesarios para obtener un resultado aproximado, utilizando el modelo preentrenado ResNet50, de la biblioteca Keras.
