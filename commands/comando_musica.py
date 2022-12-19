import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import pygame
import threading
import random

# Inicia o play as musicas
def init_musics(db):
    while True:
        musicas = {}
        tocando = ""
        numero = 0
        for doc in db.collection("Playlist").get():
            for i in sorted(doc.to_dict()):
                if i != "tocando":
                    try:
                        if i == "1":
                            tocando = doc.to_dict()[i]
                        else:
                            numero += 1
                            musicas[str(numero)] = doc.to_dict()[i]
                    except:
                        pass
                else:
                    if doc.to_dict()[i] == "":
                        db.collection("Playlist").document("tocando").update({"tocando": "Nada"})
                    else:
                        db.collection("Playlist").document("tocando").update({"tocando": tocando})
                        db.collection("Playlist").document("list").set(musicas)
        try:
            for fileName in os.listdir(r"./Musicas"):
                if fileName[0:2] == (
                    "0" + str(int(tocando)) if len(str(int(tocando))) == 1 else str(int(tocando))
                ):
                    play_music(fileName)
        except:
            music = random.choice(os.listdir(r"./Musicas"))
            db.collection("Playlist").document("tocando").update({"tocando": music[0:2]})
            play_music(music)

# Função que toca a musica
def play_music(musica):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(f'Musicas/{musica}')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(1000)



def comando_musica(enviado):
    # Init DB Firebase + Lista de comandos + Teste da Placa
    try:
        cred = credentials.Certificate("./serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
    except:
        pass
    db = firestore.client()
    # Retorna as músicas disponíveis para adicionar
    if enviado == "musicas":
        musicas = ""
        for fileName in os.listdir(r"./Musicas"):
            musicas += f'\n{fileName[0:2]}° ➤ *{fileName[5:-4]}*'
        return f"Como usar:\n*Add <N° da Música>*\n\nMúsicas: {musicas}"
    # Retorna a Playlist
    elif enviado == "playlist":
        musicas = ""
        tocando = ""
        for doc in db.collection("Playlist").get():
            for i in sorted(doc.to_dict()):
                if i != "tocando":
                    for fileName in os.listdir(r"./Musicas"):
                        if fileName[0:2] == (
                            "0" + str(int(doc.to_dict()[i]))
                            if len(str(int(doc.to_dict()[i]))) == 1
                            else str(int(doc.to_dict()[i]))
                        ):
                            musicas += f"\n{i}° ➤ *{fileName[5:-4]}*"
                else:
                    if doc.to_dict()[i] != "Nada":
                        for fileName in os.listdir(r"./Musicas"):
                            if fileName[0:2] == (
                                "0" + str(int(doc.to_dict()[i]))
                                if len(str(int(doc.to_dict()[i]))) == 1
                                else str(int(doc.to_dict()[i]))
                            ):
                                tocando = fileName[5:-4]
                    else:
                        tocando = "Nada"
        return f"Tocando agora:\n*{tocando}*\n\nPlaylist: {musicas}"
    # Retorna e Adiciona o numero da musica
    elif "add" in enviado:
        try:
            if 0 < int(enviado.replace("add", "")) <= 25:
                numero = 1
                for doc in db.collection("Playlist").get():
                    for i in doc.to_dict():
                        if i != "tocando":
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
        pygame.mixer.music.pause()
        return "Musica pulada."
    # Tocar a Playlist
    elif enviado == "play":
        for doc in db.collection("Playlist").get():
            for i in doc.to_dict():
                if doc.to_dict()[i] == "Nada":
                    threading.Thread(target= init_musics, args= [db]).start()
                    return "Tocando a Playlist."
        return "Playlist já está sendo tocada."
    # Parar tudo
    elif enviado == "cancel":
        db.collection("Playlist").document("tocando").update({"tocando": "Nada"})
        pygame.mixer.music.pause()
        return "Musicas canceladas."
