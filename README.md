<h1> Cadenas de Mensajes en Whatsapp Web Con PY 3.9.5 </h1>

Un pequeño codigo con el que puedes enviar el mensaje que desees, con la cantidad de repeticiones que indiques.

## Instalacion de Python 3.9

- [Descargar Python](https://www.python.org/downloads/)
- [Tutorial](https://www.youtube.com/watch?v=BNcpRwxH8So)

## Ejecutar el codigo
```
python Whatsapp/whatsapp.py 
```

## Variables principales: 

```
phone_no      #Agrega el numero. Ejemplo: "+541234567890"
parsedMessage #Agrega un mensaje. Ejemplo: "Hola, estoy usando Python"
cantidad      #Agrega la cantidad de mensajes
```

## Paquetes: 
  Pyautogui
  ```
  pip install pyautogui
  ```

## Recomendacion:
  En las lineas de time.sleep, el tiempo debe de ir de acuerdo con las caracteristicas de la velocidad de tu PC y/o Velocidad de internet.
  ```
  time.sleep(segundos)
  ```
  
  En linea pg.click, debemos indicar las coordenadas de la barra de mensaje para que posteriormente al ejecutar pg.press('enter') se pueda enviar el mensaje.
  ```
  pg.click(x, y)
  ```
  
  
