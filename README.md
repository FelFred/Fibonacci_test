# Fibonacci_test
Desarrollo de servicio http que al recibir un número n como entrada entregue los términos n y n-1 de la sucesión de Fibonacci

## Etapas desarrollo

* Creación del repositorio.
* Implementación de servidor local mediante código sencillo de python, utilizando clases BaseHTTPRequestHandler y HTTPServer.
* Implementación de algoritmo necesario para calcular elementos n y n-1 de sucesión de Fibonacci en python.
* Intento de lectura de datos desde html con python.
* Se decide realizar la lectura y procesamiento de datos con script de javascript por simplicidad.
* Se implementa lectura y despliegue de datos obtenidos desde un campo (recibe entradas numéricas) en página que produce el archivo html.
* Se programma algoritmo para obtener elementos de la sucesión de Fibonacci en JavaScript.
* Se añade verificación de input numérico mediante función isNaN().
* Se incorpora mensaje de error cuando la entrada es negativa, nula, o del estilo "5+5-4".
* Se añade nota respecto a valores muy grandes.

### Prerequisitos
Para montar el servidor local se ha utilizado la librería de python llamada BaseHTTPServer. En este caso se ha utilizado el software Anaconda versión 3.6 (disponible en https://www.anaconda.com/download/) para crear un entorno virtual que utilice python 2.7 ya que la librería mencionada previamente no existe en la versión 3.6 de python.

Una vez que se ha instalado Anaconda, el siguiente paso corresponde a crear un entorno virtual en el cual se instale python 2.7 ingresando la siguiente instrucción en la linea de comandos de Windows:

```
conda create -n py27 python=2.7 anaconda
```

### Dependencias del repositorio
El repositorio se compone de 2 carpetas denominadas html y py respectivamente. En la primera se encuentra el único archivo html utilizado (**Input.html**) para el despliegue de la aplicación web. Es decir, este determina tanto la interfaz apreciable por el usuario como el procesamiento mediante un script en JavaScript. En cuanto al directorio py, aquí se encuentra por una parte el archivo **httpserver.py** utilizado para montar el servidor localmente y además se encuentra el archivo **fibonacci.py**, el cual contiene el algoritmo necesario para la aplicación pero que sin embargo no se ha utilizado finalmente.


### Metodología para la utilización del servicio http

A continuación se explican los pasos a seguir para hacer uso del servicio desarrollado. En primer lugar se debe comprobar la correcta instalación del entorno virtual mencionado previamente, lo cual se puede lograr ejecutando el siguiente comando en el términal:
```
conda info --envs
```
Una vez ingresado el comando anterior, en la consola debería mostrarse un output similar al que se muestra a continuación, donde el asterisco indica el entorno que está activo actualmente. 
```
# conda environments:
#
py27                     C:\InstallDirectory\Anaconda\envs\py27
root                  *  C:\InstallDirectory\Anaconda
```
Para activar el entorno que utiliza python 2.7, denominado py27, se debe ejecutar el siguiente comando:
```
activate py27
```
Posteriormente se debe clonar o copiar el repositorio. Luego se debe navegar a través de la consola a la carpeta correspondiente y ejecutar el script **httpserver.py**
```
cd C:\RepositoryDirectory\Fibonacci_test-master\py
python httpserver.py
```
Si los pasos anteriores han funcionado de manera correcta se observará el siguiente output en el terminal:

```
http server is starting...
http server is running...

```
Finalmente, para utilizar el servicio se debe ingresar en el navegador la dirección **127.0.0.1/Input.html**. En esta página se describe brevemente la aplicación y se provee un campo donde se puede ingresar el número del elemento de la sucesión de Fibonacci que se desea conocer (junto con el que le antecede). Una vez que se ha ingresado el número en el campo, se debe proceder a presionar el botón "Calcula mis números" para obtener el resultado esperado en la parte inferior de la página.


## Tests

Con el fin de comprobar el correcto funcionamiento de la aplicación se propone un conjunto de pruebas a realizar. A continuación se indica el conjunto de entradas que se deben ingresar en la página:

* Una entrada numérica negativa.
* Una entrada nula.
* Una entrada del tipo "5+5-4".
* Una entrada igual a 1.
* Una entrada numérica entre 2 y 1476.
* Una entrada numérica igual a 1477.
* Una entrada numérica igual a 1478 o superior.

Cuando se ingresan estas entradas se deberían los siguientes resultados (o similares para el quinto caso):
```
Error: Por favor ingresar un número mayor o igual a 1
Error: Por favor ingresar un número mayor o igual a 1
Error: Por favor ingresar un número mayor o igual a 1
El primer elemento es: 1, y el elemento anterior no existe.
El elemento número 50 es: 12586269025, y el elemento anterior es: 7778742049
El elemento número 1477 es: Infinity, y el elemento anterior es: 1.3069892237633987e+308
El elemento número 1500 es: Infinity, y el elemento anterior es: Infinity
```
Nota: el campo definido en el archivo html no permite entradas que no sean numéricas. A pesar de esto existe una porción de código que corrobora que esto se cumpla. En caso contrario se despliega un mensaje de error solicitando una entrada válida (numérica).


## Herramientas utilizadas durante el desarrollo

* Anaconda: manejo de entornos virtuales con una versión determinada de python.
* Editey: Visualización sencilla y rápida de página generada por archivo html.

## Comentarios finales

Se agradecerá todo tipo de feedback asociado a la realización de esta actividad. 





