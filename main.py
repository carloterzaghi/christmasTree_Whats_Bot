from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from commands.comando_placa import comando_ligar_Placa
from commands.comando_musica import comando_musica
import firebase_admin
from firebase_admin import credentials

global lista_playlist
lista_playlist = []

app = Flask(__name__)
  
@app.route("/")
def index():
    return "Hello, world!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    #Lista Playlist + Lista de comandos + Teste da Placa
    lista_comandos = ['ligar','desligar','som', 'playlist', 'add','skip']
    placa_teste = False

    #Mensagens Whats
    resp = MessagingResponse()
    enviado = request.form.get('Body')
    enviado = enviado.casefold()
    msg = resp.message()

    #Comando Placa
    if comando_ligar_Placa(enviado)[1]:
        msg.body(comando_ligar_Placa(enviado)[0])
        placa_teste = comando_ligar_Placa(enviado)[1]
    
    #Se o Try ou Except acontecer
    if placa_teste == True:
        placa_teste = False
    
    #Comandos/Help
    elif enviado in ['comandos','help']:
        commands = ''
        for i in lista_comandos: commands+= f'\n➤ *{i.capitalize()}*'
        msg.body('Os comandos são:'+ commands)
    
    #Comandos de Som
    elif enviado.split()[0] in lista_comandos:
        print(lista_playlist)
        if type(comando_musica(enviado,lista_playlist)) == list:
            lista_playlist = comando_musica(enviado,lista_playlist)[1]
            print(lista_playlist)
            msg.body(comando_musica(enviado,lista_playlist)[0])
        else:
            msg.body(comando_musica(enviado,lista_playlist))
    else:
        msg.body(f'Não entendi o que você disse.')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)