import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def comando_musica(enviado):
    #Init DB Firebase + Lista de comandos + Teste da Placa
    try:
        cred = credentials.Certificate("./serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
    except:
        pass
    db = firestore.client()
    # Retorna as músicas disponíveis para adicionar
    if enviado == 'som':
        return
    # Retorna a Playlist    
    elif enviado == 'playlist':
        musicas = ''
        for doc in db.collection('Playlist').get(): 
            for i in sorted(doc.to_dict()): musicas += f'\n➤ *{doc.to_dict()[i]}*'
        return f'Playlist: {musicas}'
    # Retorna e Adiciona o numero da musica
    elif 'add' in enviado:
        if 0 < int(enviado.replace('add', '')) <= 25:
            numero = 1
            for doc in db.collection('Playlist').get(): 
                for i in doc.to_dict(): numero+=1
            db.collection('Playlist').document('list').update({str(numero):enviado.replace('add', '')})
            return f"Música {str(int(enviado.replace('add', '')))} adicionada."
        else:
            return f"Música {str(int(enviado.replace('add', '')))} não existe."
    # Pula a musica
    elif enviado == 'skip':
        return
    