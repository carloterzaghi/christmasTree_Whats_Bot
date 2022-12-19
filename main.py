from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from commands.comando_placa import comando_ligar_Placa
from commands.comando_musica import comando_musica

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world!"


@app.route("/sms", methods=["POST"])
def sms_reply():
    # Lista de comandos + Teste da Placa
    lista_comandos = [
        "ligar",
        "desligar",
        "musicas",
        "playlist",
        "add",
        "skip",
        "play",
        "cancel",
    ]
    placa_teste = False

    # Mensagens Whats
    resp = MessagingResponse()
    enviado = request.form.get("Body")
    enviado = enviado.casefold()
    msg = resp.message()

    # Comando Placa
    if comando_ligar_Placa(enviado)[1]:
        msg.body(comando_ligar_Placa(enviado)[0])
        placa_teste = comando_ligar_Placa(enviado)[1]

    # Se o Try ou Except acontecer
    if placa_teste == True:
        placa_teste = False

    # Comandos/Help
    elif enviado in ["comandos", "help"]:
        commands = ""
        for i in lista_comandos:
            commands += f"\n➤ *{i.capitalize()}*"
        msg.body("Os comandos são:" + commands)

    # Comandos de Som
    elif enviado.split()[0] in lista_comandos:
        msg.body(comando_musica(enviado))
    else:
        msg.body(f"Não entendi o que você disse.")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
