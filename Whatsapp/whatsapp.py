  
import pyautogui as pg      #Automatizar tareas
import time                 #Controla el tiempo
import webbrowser as web    #Controlar el navegador


phone_no = input("Agrega Numero:")  #Agrega el numero. Ejemplo: "+541234567890"
parsedMessage = input("Agrega Mensaje: ") #Agrega un mensaje. Ejemplo: "Hola, estoy usando Python"
cantidad = int (input ("Cantidad de mensajes: ")) #Agrega la cantidad de mensajes

web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage) #Abre whatsapp web con phone_no

time.sleep(10)
pg.click(715, 705) #Click en el cuadro de mensajes para dar enter
time.sleep(15) #Tiempo de Espera

for i in range(cantidad):  #Range (Cantidad de Mensajes)
    pg.write(parsedMessage)
    pg.press('enter')
    print('Mensaje #'+str(i+1)+' enviado')
    pass

pg.alert('Finish') #Alerta





