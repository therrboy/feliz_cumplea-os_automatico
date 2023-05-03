##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random as random

now = dt.datetime.now()
year = now.year
month = now.month
day_num = now.weekday()

my_email = "correodeprueba@hotmail.com"
password = "correodeprueba"

# Dia actual de la semana
day = now.day

# 1. Update the birthdays.csv

archivo_datetime = pd.read_csv("birthdays.csv")  # Lectura del archivo csv

nuevo_diccionario = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in archivo_datetime.iterrows()}  # Vamos a hacer un diccionario

data_today = (month, day)  # Datos del dia

if data_today in nuevo_diccionario:  # Si los datos del dia coinciden con el diccionario anterior
    birthday_person = nuevo_diccionario[data_today]  # Almacena en una variable la fecha de quien cumple años ese dia
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"  # Buscamos la ubicacion y elegimos al azar una de esas publicaciones, sin abrirlo
    with open(file_path) as datos_hoy:
        contenido = datos_hoy.read()  # Abrimos el archivo anteriormente buscado
        texto_reemplazado = contenido.replace("[NAME]", birthday_person["name"])  # Guardamos el texto reemplazado

    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:  # Podemos usar "with" para no usar close al final
        connection.starttls()  # Sirve para encriptar el mensaje
        connection.login(user=my_email, password=password)  # Login
        connection.sendmail(
            from_addr=my_email,
            to_addrs="correodeprueba@hotmail.com",
            msg=f"Subject:Probando\n\n{texto_reemplazado}"
        )
