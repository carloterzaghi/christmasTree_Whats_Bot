def comando_musica(enviado,lista_playlist):
    if enviado == 'som':
        return
    elif enviado == 'playlist':
        musicas = ''
        for i in lista_playlist: musicas += f'\n- {i}'
        return f'Playlist: {musicas}'
    elif 'add' in enviado:
        lista_playlist.append(int(enviado.replace('add', '')))
        return [f"Música {str(int(enviado.replace('add', '')))} adicionada.", lista_playlist]
    elif enviado == 'skip':
        return
    