from twilio.twiml.messaging_response import MessagingResponse
import serial


def comando_ligar_Placa(enviado):
    try:
        serialInst = serial.Serial()
        serialInst.baudrate = 9600
        serialInst.port = "COM4"
        serialInst.open()

        if enviado in ["ligar", "desligar"]:
            serialInst.write(("O" if enviado == "ligar" else "L").encode("utf-8"))
            p = serialInst.readline()
            return [f"LED {enviado.capitalize()[0:-1]}do.", True]
        else:
            return ["", False]
    # Não conseguiu conectar com a placa
    except:
        if enviado in ["ligar", "desligar"]:
            return ["Placa Desconectada", True]
        else:
            return ["", False]
