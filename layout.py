import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import os


# Layout do Tkinter
def layout():
    # Função que pega os dados do DB Firebase
    def get_db_data():
        while True:
            musicas = ""
            for doc in db.collection("Playlist").get():
                if doc.to_dict() == {}:
                    fila.set(musicas)
                for i in sorted(doc.to_dict()):
                    if i != "tocando":
                        for fileName in os.listdir(r"./Musicas"):
                            if fileName[0:2] == (
                                "0" + str(int(doc.to_dict()[i]))
                                if len(str(int(doc.to_dict()[i]))) == 1
                                else str(int(doc.to_dict()[i]))
                            ):
                                musicas += f"\n{i}° ➤ {fileName[5:-4]}"
                        fila.set(musicas)
                    else:
                        try:
                            for fileName in os.listdir(r"./Musicas"):
                                if fileName[0:2] == (
                                    "0" + str(int(doc.to_dict()[i]))
                                    if len(str(int(doc.to_dict()[i]))) == 1
                                    else str(int(doc.to_dict()[i]))
                                ):
                                    tocando.set(fileName[5:-4])
                        except:
                            tocando.set("Nada")

    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    master = Tk()

    # Variáveis
    tocando = StringVar()
    fila = StringVar()

    # Pegar informações da tela
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    # Nome da Aplicação + Tamanho dela
    master.title("Playlist Bot")
    master.geometry(
        (
            str(int(900 * (screen_width / 1200)))
            + "x"
            + str(int(900 * (screen_height / 1000)))
        )
    )
    master.resizable(width=1, height=1)

    # Coloca a imagem
    img = Image.open("Layout_Musica.png")
    img_resized = img.resize(
        (int(900 * (screen_width / 1200)), int(900 * (screen_height / 1000))),
        Image.ANTIALIAS,
    )
    img_final = ImageTk.PhotoImage(img_resized)
    lab_img = Label(master, image=img_final)
    lab_img.pack()

    # Colocando as variáveis no Tkinter + setar valores iniciais
    texto_tocando = Label(master, textvariable=tocando, font=("jost", 24), bg="white")
    texto_tocando.place(
        width=int((screen_width * 3.66) * (303 / screen_width)),
        height=int((screen_height * 0.40) * (155 / screen_height)),
        x=screen_width / 12.16,
        y=screen_height / 13.5,
    )

    texto_fila = Label(master, textvariable=fila, font=("jost", 22), bg="white")
    texto_fila.place(
        width=int((screen_width * 3.96) * (303 / screen_width)),
        height=int((screen_height * 4.10) * (155 / screen_height)),
        x=screen_width / 16.16,
        y=screen_height / 4.7,
    )

    # Variaveis set/Start
    tocando.set("Nada")
    fila.set("")

    master.resizable(0, 0)

    threading.Thread(target=get_db_data).start()

    master.mainloop()
