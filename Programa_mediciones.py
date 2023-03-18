import tkinter as tk
from tkinter import messagebox, ttk
import datetime
from datetime import date, time, datetime
import requests
import json
import sqlite3
from base64 import b64decode
import sys

icono_datos = "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"

def obtenerTemperatura():
    api_key = leer_archivo("key.txt")
    city = leer_archivo("ubicacion.txt")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status() # Genera una excepción en caso de que la respuesta tenga un código de estado de error (>= 400)
        data = response.json()
        temperature = data["main"]["temp"]
        return int(temperature)
    except requests.exceptions.RequestException as e:
        tk.Tk().withdraw() # Oculta la ventana principal de tkinter
        messagebox.showerror("Error al conectarse a la API", f"Revisa tu coneccion a internet \nCodigo de error: {e}") # Muestra una ventana de alerta con el mensaje de error
        sys.exit()

def guardarDatos():
    try:
        voltaje = int(voltajeInput.get())
    except:
        messagebox.showerror('Error', 'Sólo se permiten números en Voltaje.')
    
    fecha = datoFechaInput.get()
    hora = datoHoraInput.get()
    minutos = datoMinutoInput.get()
    now = datetime.now()
    temperatura = datoTempInput.get()
    
    
    if (fecha ==""):
        fecha = now.strftime("%d/%m/%Y")
    if (hora == ""):
        hora = now.hour
    if (minutos == ""):
        minutos = now.minute
    if (temperatura == ""):
        temperatura = obtenerTemperatura()
    
    cargarBase(voltaje, fecha, hora, minutos, temperatura)
    messagebox.showinfo("Registro guardado", "El registro se ha guardado con exito")
    limpiarInputs()
    
    
def cargarBase(voltaje ,fecha, hora, minutos, temperatura):
    conn = sqlite3.connect("mi_bd.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS datos (id INTEGER PRIMARY KEY AUTOINCREMENT, voltaje NUMERIC, fecha VARCHAR(10), hora VARCHAR(2), minutos VARCHAR(2), temperatura VARCHAR(2))''')
    cursor.execute("INSERT INTO datos (voltaje, fecha, hora, minutos, temperatura) VALUES (?,?,?,?,?)", (voltaje,fecha,hora,minutos,temperatura))
    conn.commit()
    conn.close()
    
def limpiarInputs():
    voltajeInput.delete(0, "end")
    datoFechaInput.delete(0, "end")
    datoHoraInput.delete(0, "end")
    datoMinutoInput.delete(0, "end")
    datoTempInput.delete(0, "end")

def ventanaKey():
    ventanaKey = tk.Toplevel(root)
    
    label = tk.Label(ventanaKey, text="Ingresar key")
    label.grid(row=0, column=0)

    ubicacion = tk.Label(ventanaKey, text="Ingresar ubicacion")
    ubicacion.grid(row=1, column=0)
    
    key = tk.Entry(ventanaKey)
    key.grid(row=0, column=1)
    
    ubicacionKey = tk.Entry(ventanaKey)
    ubicacionKey.grid(row=1, column=1)
    
    keySaveButton = tk.Button(ventanaKey, text="Guardar key", command=lambda: guardarKey(key.get(), ubicacionKey.get()), activebackground="lightblue", bg="cyan2")
    keySaveButton.grid(row=2, column=0)
    
def guardarKey(key, ubicacion):

    print(key)
    with open("key.txt", "w") as f:
        f.write(key)
    with open("ubicacion.txt", "w") as f:
        f.write(ubicacion)
    messagebox.showinfo("Archivo creado", "El archivo ha sido creado con exito")
    
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido

root = tk.Tk()
root.title("Cargar informacion en base")
icono = tk.PhotoImage(data=b64decode(icono_datos))
root.iconphoto(False, icono)

    
    
#Declaracon de labels
voltajeLabel = tk.Label(root, text="Voltaje = ")
datoFecha = tk.Label(root, text="Fecha DD/MM/AAAA = ")
datoHora = tk.Label(root, text="Hora = ")
datoMinuto = tk.Label(root, text="Minuto = ")
datoTemp = tk.Label(root, text="Temperatura en c° = ")
datoKey = tk.Label(root, text="Ingresar key = ")


#declaracion de inputs
voltajeInput = tk.Entry(root)
datoFechaInput = tk.Entry(root)
datoHoraInput = tk.Entry(root)
datoMinutoInput = tk.Entry(root)
datoTempInput = tk.Entry(root)
datoKeyInput = tk.Entry(root)
keyButton = tk.Button(root,text="Ingresar key", command = ventanaKey, activebackground="lightblue", bg="cyan2")
submitDatos = tk.Button(root,text="Guardar datos", command = guardarDatos, activebackground="lightblue", bg="cyan2")

#Posicionamiento en grilla
voltajeLabel.grid(row=0, column=0)
voltajeInput.grid(row=0, column=1)

datoFecha.grid(row=1, column=0)
datoFechaInput.grid(row=1, column=1)

datoHora.grid(row=2, column=0)
datoHoraInput.grid(row=2, column=1)

datoMinuto.grid(row=3, column=0)
datoMinutoInput.grid(row=3, column=1)

datoTemp.grid(row=4, column=0)
datoTempInput.grid(row=4, column=1)


submitDatos.grid(row=7, column=0)
keyButton.grid(row=7, column=1)
root.mainloop()