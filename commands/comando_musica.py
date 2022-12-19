import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os


def comando_musica(enviado):
    # Init DB Firebase + Lista de comandos + Teste da Placa
    try:
        cred = credentials.Certificate("./serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
    except:
        pass
    db = firestore.client()
    # Retorna as músicas disponíveis para adicionar
    if enviado == "som":
        return
    # Retorna a Playlist
    elif enviado == "playlist":
        musicas = ""
        for doc in db.collection("Playlist").get():
            for i in sorted(doc.to_dict()):
                for fileName in os.listdir(r"./Musicas"):
                    if fileName[0:2] == (
                        "0" + str(int(doc.to_dict()[i]))
                        if len(str(int(doc.to_dict()[i]))) == 1
                        else str(int(doc.to_dict()[i]))
                    ):
                        musicas += f"\n➤ *{fileName[5:-4]}*"
        return f"Playlist: {musicas}"
    # Retorna e Adiciona o numero da musica
    elif "add" in enviado:
        try:
            if 0 < int(enviado.replace("add", "")) <= 25:
                numero = 1
                for doc in db.collection("Playlist").get():
                    for i in doc.to_dict():
                        numero += 1
                db.collection("Playlist").document("list").update(
                    {str(numero): enviado.replace("add", "")}
                )
                for fileName in os.listdir(r"./Musicas"):
                    if fileName[0:2] == (
                        "0" + str(int(enviado.replace("add", "")))
                        if len(str(int(enviado.replace("add", "")))) == 1
                        else str(int(enviado.replace("add", "")))
                    ):
                        return f"Música *{fileName[5:-4]}* adicionada."
            else:
                return f"Música *{str(int(enviado.replace('add', '')))}* não existe."
        except:
            return "Erro no comando."
    # Pula a musica
    elif enviado == "skip":
        return
