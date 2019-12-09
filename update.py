import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import smtplib
from email.mime.text import MIMEText
from mail import*
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
import serial
from Pyserial import*

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds =  ServiceAccountCredentials.from_json_keyfile_name("nome da API do google", scope)

client = gspread.authorize(creds)

sheet_1 = client.open("formulario").sheet1
sheet_2 = client.open("AACD").sheet1
sheet_3 = client.open("Cofres").sheet1

def update():
    col_ID_FORM = sheet_1.col_values(2)
    col_ID_AACD = sheet_2.col_values(1)
    try:
        index = col_ID_AACD.index(col_ID_FORM[1])
        sheet_3.insert_row(sheet_2.row_values(index+1),1)
        
        iden = sheet_2.row_values(index+1)[0]
        adress = sheet_2.row_values(index+1)[1]

        mensagem(iden, adress)
        led_on()
        
        sheet_2.delete_row(index+1)
        sheet_1.delete_row(2)
        print('ok')
        
    except Exception:
        if col_ID_FORM[1] == "":
            print('Nada existe!')
        elif col_ID_FORM != "":
            sheet_1.delete_row(2)
            print('Linha apagada!')
        
CONTINUAR = True 
while CONTINUAR:
    try:
        update()
    except Exception:
        print('Sem notificação')