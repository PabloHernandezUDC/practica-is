# MANUAL DE USUARIO

Este manual ha sido desarrollado con el propósito de facilitar el correcto uso e instalación de los usuarios de la aplicación.

### Instrucciones de instalación de la app

Para el correcto funcionamiento de la aplicación necesitamos descargar los archivos .py del repositorio e instalar las siguientes librerías: pandas, tkinter, customtkinter, pickle, matplotlib, sqlite3, numpy, sklearn.linear_model

Para instalarlas, debemos introducir los siguientes comandos en el terminal: 
- pip install pandas
- pip install tkinter
- pip install pickle
- pip install matplotlib
- pip install sqlite3
- pip install numpy
- pip install sklearn.linear_model

### Manual de uso de la app

Para inicializar la interfaz gráfica es necesario ejecutar el archivo *main.py*. Se abrirá una nueva ventana en la que aparecerán dos botones: 'Elegir archivo' y 'Cargar modelo'.

Si hacemos click en el botón 'Elegir archivo', se abrirá el explorador de ficheros de nuestro dispositivo para que elijamos el archivo que queremos utilizar. La aplicación admite archivos de base de datos, Excel y CSV. Seleccionamos el archivo que queramos y hacemos click en el botón 'Abrir'. Al lado de los dos botones que nos aparecían anteriormente podremos ver la ruta del archivo que acabamos de seleccionar, y justo debajo tendremos una tabla con los datos de este y dos filas con radiobuttons donde debemos escoger que datos queremos utilizar como variables X e Y para calcular la recta de regresión. Una vez escogidas, hacemos click en el botón 'Crear modelo y mostrar imagen' y podremos visualizar una gráfica con la recta de regresión, así como su ecuación, coeficiente de determinación y error cuadrado medio. Debajo de la gráfica tendremos la ecuación de la recta, la cual podremos completar con el valor de X que deseemos para hacer una predicción. Por último, para guardar este modelo debemos hacer click en el botón 'Guardar modelo', que está a la derecha de la gráfica. Se abrirá una pequeña ventana donde se nos dará la opción de introducir una descripción del modelo, y tras esto se abrirá el explorador de ficheros para guardar el modelo dandole el nombre que prefiramos, con la extensión .pickle.

Si hacemos click en el botón 'Cargar modelo', se abrirá el explorador de ficheros de nuestro dispositivo para que elijamos el modelo (con extensión .pickle) que queremos utilizar. Seleccionamos el modelo que queramos y hacemos click en el botón 'Abrir'. Al lado de los dos botones que nos aparecían anteriormente podremos ver la ruta del archivo que acabamos de seleccionar, y justo debajo tendremos los datos del modelo (variable X, variableY, ecuación, coeficiente de determinación, error cuadrado medio, descripción) y de nuevo la ecuación de la recta, la cual podremos completar con el valor de X que deseemos para hacer una predicción.
