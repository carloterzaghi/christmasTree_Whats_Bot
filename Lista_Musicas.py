import pygame

playlist = list()
tocando = []

def musicIndex(title) -> int:
    musics = {
        "1" : 1,
    }
    try:
        index = musics[title]
        return index
    except Exception as e:
        return -1

def addMusic(title):
    if title < 27:
        playlist.append(title)
        return mensagem_retorno(title)
    else:
        return 'Música não encontrada'

def skip():
    pygame.mixer.music.stop()
    return playPlaylistMusics()

def listView():
    listReturn = '*A seguencia na Playlist são:*\n'
    # tocando_agora = tocando[0]
    # print(tocando_agora)
    # if tocando_agora == 1 or tocando_agora == 0:
    #         listReturn = listReturn + '\nAll I Want for Christmas Is You --> Tocando agora'
    # elif tocando_agora == 2:
    #         listReturn = listReturn +'\nFrank Sinatra - Jingle Bells --> Tocando agora'
    # elif tocando_agora == 3:
    #         listReturn = listReturn +'\nSpidey Bells --> Tocando agora'
    # elif tocando_agora == 4:
    #         listReturn = listReturn +'\nJingle Bell Rock --> Tocando agora'
    # elif tocando_agora == 5:
    #         listReturn = listReturn +'\nDean Martin - Let it Snow! --> Tocando agora'
    # elif tocando_agora == 6:
    #         listReturn = listReturn +'\nIts Beginning To Look A Lot Like Christmas --> Tocando agora'
    # elif tocando_agora == 7:
    #         listReturn = listReturn + '\nWhat A Wonderfull World --> Tocando agora'
    # elif tocando_agora == 8:
    #         listReturn = listReturn + '\nWestlife - I Have A Dream --> Tocando agora'
    # elif tocando_agora == 9:
    #         listReturn = listReturn + '\nModern Talking - Its Christmas --> Tocando agora'
    # elif tocando_agora == 10:
    #         listReturn = listReturn + '\nWhitney Houston - The Firs Nöel --> Tocando agora'
    # elif tocando_agora == 11:
    #         listReturn = listReturn + '\nBoney M. - Jingle Bells --> Tocando agora'
    # elif tocando_agora == 12:
    #         listReturn = listReturn + '\nJimmy Boyd - I Saw Mommy Kissing Santa Claus --> Tocando agora'
    # elif tocando_agora == 13:
    #         listReturn = listReturn + '\nAndy Williams - Its The Most Wonderful Of The Year --> Tocando agora'
    # elif tocando_agora == 14:
    #         listReturn = listReturn + '\nArt Garfunkel - O Come All Ye Faithful --> Tocando agora'
    # elif tocando_agora == 15:
    #         listReturn = listReturn + '\nJohn Denver - Rudolph The Red Nosed Reindeer --> Tocando agora'
    # elif tocando_agora == 16:
    #         listReturn = listReturn + '\nMary Chapin Carpenter - Bells Are Ringing --> Tocando agora'
    # elif tocando_agora == 17:
    #         listReturn = listReturn + '\nWham! - Last Christmas --> Tocando agora'
    # elif tocando_agora == 18:
    #         listReturn = listReturn + '\nR. Kelly - Christmas I will Be Steppin --> Tocando agora'
    # elif tocando_agora == 19:
    #         listReturn = listReturn + '\nBackstreet Boys - Christmas Time --> Tocando agora'
    # elif tocando_agora == 20:
    #         listReturn = listReturn + '\nChris Brown - This Christmas --> Tocando agora'
    # elif tocando_agora == 21:
    #         listReturn = listReturn + '\nNew Kids On The Block - Merry, Merry Christmas --> Tocando agora'
    # elif tocando_agora == 22:
    #         listReturn = listReturn + '\nWillie Nelson - Frosty The Snowman --> Tocando agora'
    # elif tocando_agora == 23:
    #         listReturn = listReturn + '\nLet It Snow! Let It Snow! Let It Snow! - Frank Sinatra With The B. Swanson Quartet --> Tocando agora'
    # elif tocando_agora == 24:
    #         listReturn = listReturn + '\nJohnny Cash - Little Drummer Boy --> Tocando agora'
    # elif tocando_agora == 25:
    #         listReturn = listReturn + '\nPatti Page - We Wish You A Merry Christmas --> Tocando agora'
    # elif tocando_agora == 26:
    #         listReturn = listReturn + '\nThe Malufs - Conquistador Barato --> Tocando agora'    
    # else:
    #         pass
    for numero in playlist:
        if numero == 1 or numero == 0:
            listReturn = listReturn + '\nAll I Want for Christmas Is You'
        elif numero == 2:
            listReturn = listReturn +'\nFrank Sinatra - Jingle Bells'
        elif numero == 3:
            listReturn = listReturn +'\nSpidey Bells'
        elif numero == 4:
            listReturn = listReturn +'\nJingle Bell Rock'
        elif numero == 5:
            listReturn = listReturn +'\nDean Martin - Let it Snow!'
        elif numero == 6:
            listReturn = listReturn +'\nIts Beginning To Look A Lot Like Christmas'
        elif numero == 7:
            listReturn = listReturn + '\nWhat A Wonderfull World'
        elif numero == 8:
            listReturn = listReturn + '\nWestlife - I Have A Dream'
        elif numero == 9:
            listReturn = listReturn + '\nModern Talking - Its Christmas'
        elif numero == 10:
            listReturn = listReturn + '\nWhitney Houston - The Firs Nöel'
        elif numero == 11:
            listReturn = listReturn + '\nBoney M. - Jingle Bells'
        elif numero == 12:
            listReturn = listReturn + '\nJimmy Boyd - I Saw Mommy Kissing Santa Claus'
        elif numero == 13:
            listReturn = listReturn + '\nAndy Williams - Its The Most Wonderful Of The Year'
        elif numero == 14:
            listReturn = listReturn + '\nArt Garfunkel - O Come All Ye Faithful'
        elif numero == 15:
            listReturn = listReturn + '\nJohn Denver - Rudolph The Red Nosed Reindeer'
        elif numero == 16:
            listReturn = listReturn + '\nMary Chapin Carpenter - Bells Are Ringing'
        elif numero == 17:
            listReturn = listReturn + '\nWham! - Last Christmas'
        elif numero == 18:
            listReturn = listReturn + '\nR. Kelly - Christmas I will Be Steppin'
        elif numero == 19:
            listReturn = listReturn + '\nBackstreet Boys - Christmas Time'
        elif numero == 20:
            listReturn = listReturn + '\nChris Brown - This Christmas'
        elif numero == 21:
            listReturn = listReturn + '\nNew Kids On The Block - Merry, Merry Christmas'
        elif numero == 22:
            listReturn = listReturn + '\nWillie Nelson - Frosty The Snowman'
        elif numero == 23:
            listReturn = listReturn + '\nLet It Snow! Let It Snow! Let It Snow! - Frank Sinatra With The B. Swanson Quartet'
        elif numero == 24:
            listReturn = listReturn + '\nJohnny Cash - Little Drummer Boy'
        elif numero == 25:
            listReturn = listReturn + '\nPatti Page - We Wish You A Merry Christmas'
        elif numero == 26:
            listReturn = listReturn + '\nThe Malufs - Conquistador Barato'    
        else:
            return 'Música não encontrada'
    print(playlist)
    return listReturn 

def playPlaylistMusics():
    for numero in playlist:
        playlist.remove(numero)
        if numero == 1 or numero == 0:
            pygame.mixer.music.load('Musicas/1.mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            
        elif numero == 2:
            pygame.mixer.music.load('Musicas/Frank Sinatra - Jingle Bells.mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            
        elif numero == 3:
            pygame.mixer.music.load('Musicas/Spidey Bells - A VERY SPIDEY CHRISTMAS (online-audio-converter.com).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Spidey Bells'
        elif numero == 4:
            pygame.mixer.music.load('Musicas/Glee Cast - Jingle Bell Rock (Official Yule Log) (online-audio-converter.com).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Jingle Bell Rock'
        elif numero == 5:
            pygame.mixer.music.load('Musicas/Dean Martin - Let it Snow!.mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Dean Martin - Let it Snow!'
        elif numero == 6:
            pygame.mixer.music.load('Musicas/Its Beginning To Look A Lot Like Christmas.mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Its Beginning To Look A Lot Like Christmas'
        elif numero == 7:
            pygame.mixer.music.load('Musicas/01 - What A Wonderfull World (John Leggend).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando What A Wonderfull World'
        elif numero == 8:
            pygame.mixer.music.load('Musicas/02 - I Have A Dream (Westlife).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Westlife - I Have A Dream'
        elif numero == 9:
            pygame.mixer.music.load('Musicas/03 - Its Christmas (Modern Talking).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Modern Talking - Its Christmas'
        elif numero == 10:
            pygame.mixer.music.load('Musicas/04 - The Firs Nöel (Whitney Houston).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Whitney Houston - The Firs Nöel'
        elif numero == 11:
            pygame.mixer.music.load('Musicas/05 - Jingle Bells (Boney M.).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Boney M. - Jingle Bells'
        elif numero == 12:
            pygame.mixer.music.load('Musicas/06 - I Saw Mommy Kissing Santa Claus (Jimmy Boyd).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Jimmy Boyd - I Saw Mommy Kissing Santa Claus'
        elif numero == 13:
            pygame.mixer.music.load('Musicas/07 - Its The Most Wonderful Of The Year (Andy Williams).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Andy Williams - Its The Most Wonderful Of The Year'
        elif numero == 14:
            pygame.mixer.music.load('Musicas/08 - O Come All Ye Faithful (Art Garfunkel).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Art Garfunkel - O Come All Ye Faithful'
        elif numero == 15:
            pygame.mixer.music.load('Musicas/09 - Rudolph The Red Nosed Reindeer (John Denver).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando John Denver - Rudolph The Red Nosed Reindeer'
        elif numero == 16:
            pygame.mixer.music.load('Musicas/10 - Bells Are Ringing (Mary Chapin Carpenter).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Mary Chapin Carpenter - Bells Are Ringing'
        elif numero == 17:
            pygame.mixer.music.load('Musicas/11 - Last Christmas (Wham!).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Wham! - Last Christmas'
        elif numero == 18:
            pygame.mixer.music.load('Musicas/12 - Christmas Ill Be Steppin (R. Kelly).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando R. Kelly - Christmas I will Be Steppin'
        elif numero == 19:
            pygame.mixer.music.load('Musicas/13 - Christmas Time (Backstreet Boys).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Backstreet Boys - Christmas Time'
        elif numero == 20:
            pygame.mixer.music.load('Musicas/14 - This Christmas (Chris Brown).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Chris Brown - This Christmas'
        elif numero == 21:
            pygame.mixer.music.load('Musicas/15 - Merry, Merry Christmas (New Kids On The Block).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando New Kids On The Block - Merry, Merry Christmas'
        elif numero == 22:
            pygame.mixer.music.load('Musicas/16 - Frosty The Snowman (Willie Nelson).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Willie Nelson - Frosty The Snowman'
        elif numero == 23:
            pygame.mixer.music.load('Musicas/17 - Let It Snow! Let It Snow! Let It Snow! (Frank Sinatra With The B. Swanson Quartet).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Let It Snow! Let It Snow! Let It Snow! - Frank Sinatra With The B. Swanson Quartet'
        elif numero == 24:
            pygame.mixer.music.load('Musicas/18 - Little Drummer Boy (Johnny Cash).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Johnny Cash - Little Drummer Boy'
        elif numero == 25:
            pygame.mixer.music.load('Musicas/19 - We Wish You A Merry Christmas (Patti Page).mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando Patti Page - We Wish You A Merry Christmas'
        elif numero == 26:
            pygame.mixer.music.load('Musicas/Conquistador Barato.mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            return 'Tocando The Malufs - Conquistador Barato'    
        else:
            return 'Música não encontrada'

def mensagem_retorno(numero):
    if numero == 1 or numero == 0:
        return 'Adicionado All I Want for Christmas Is You'
    elif numero == 2:
            return 'Adicionado Frank Sinatra - Jingle Bells'
    elif numero == 3:
            return 'Adicionado Spidey Bells'
    elif numero == 4:
            return 'Adicionado Jingle Bell Rock'
    elif numero == 5:
            return 'Adicionado Dean Martin - Let it Snow!'
    elif numero == 6:
            return 'Adicionado Its Beginning To Look A Lot Like Christmas'
    elif numero == 7:
            return 'Adicionado What A Wonderfull World'
    elif numero == 8:
            return 'Adicionado Westlife - I Have A Dream'
    elif numero == 9:
            return 'Adicionado Modern Talking - Its Christmas'
    elif numero == 10:
            return 'Adicionado Whitney Houston - The Firs Nöel'
    elif numero == 11:
            return 'Adicionado Boney M. - Jingle Bells'
    elif numero == 12:
            return 'Adicionado Jimmy Boyd - I Saw Mommy Kissing Santa Claus'
    elif numero == 13:
            return 'Adicionado Andy Williams - Its The Most Wonderful Of The Year'
    elif numero == 14:
            return 'Adicionado Art Garfunkel - O Come All Ye Faithful'
    elif numero == 15:
            return 'Adicionado John Denver - Rudolph The Red Nosed Reindeer'
    elif numero == 16:
            return 'Adicionado Mary Chapin Carpenter - Bells Are Ringing'
    elif numero == 17:
            return 'Adicionado Wham! - Last Christmas'
    elif numero == 18:
            return 'Adicionado R. Kelly - Christmas I will Be Steppin'
    elif numero == 19:
            return 'Adicionado Backstreet Boys - Christmas Time'
    elif numero == 20:
            return 'Adicionado Chris Brown - This Christmas'
    elif numero == 21:
            return 'Adicionado New Kids On The Block - Merry, Merry Christmas'
    elif numero == 22:
            return 'Adicionado Willie Nelson - Frosty The Snowman'
    elif numero == 23:
            return 'Adicionado Let It Snow! Let It Snow! Let It Snow! - Frank Sinatra With The B. Swanson Quartet'
    elif numero == 24:
            return 'Adicionado Johnny Cash - Little Drummer Boy'
    elif numero == 25:
            return 'Adicionado Patti Page - We Wish You A Merry Christmas'
    elif numero == 26:
            return 'Adicionado The Malufs - Conquistador Barato'    
    else:
            return 'Música não encontrada'

    # def playlistTeste():
    #     return str(playlist)

    # def tocar_playlist(x):
    #     playlist.append(x)
    #     try: 
    #         tocando_musica()
    #     return None

    # def tocando_musica():  
    #     return tocar_musica(int(playing.pop()))

            
    #     #if len(playlist) == 1:
    #         #return tocar_musica(int(playlist[0]))
    #     #elif len(playlist) > 1:
    #         #return 'já vai'
        

    # def tocar_musica(numero):
        # if numero == 1 or numero == 0:
        #     pygame.mixer.music.load('Musicas/videoplayback (online-audio-converter.com).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando All I Want for Christmas Is You'
        # elif numero == 2:
        #     pygame.mixer.music.load('Musicas/Frank Sinatra - Jingle Bells.mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Frank Sinatra - Jingle Bells'
        # elif numero == 3:
        #     pygame.mixer.music.load('Musicas/Spidey Bells - A VERY SPIDEY CHRISTMAS (online-audio-converter.com).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Spidey Bells'
        # elif numero == 4:
        #     pygame.mixer.music.load('Musicas/Glee Cast - Jingle Bell Rock (Official Yule Log) (online-audio-converter.com).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Jingle Bell Rock'
        # elif numero == 5:
        #     pygame.mixer.music.load('Musicas/Dean Martin - Let it Snow!.mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Dean Martin - Let it Snow!'
        # elif numero == 6:
        #     pygame.mixer.music.load('Musicas/Its Beginning To Look A Lot Like Christmas.mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Its Beginning To Look A Lot Like Christmas'
        # elif numero == 7:
        #     pygame.mixer.music.load('Musicas/01 - What A Wonderfull World (John Leggend).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando What A Wonderfull World'
        # elif numero == 8:
        #     pygame.mixer.music.load('Musicas/02 - I Have A Dream (Westlife).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Westlife - I Have A Dream'
        # elif numero == 9:
        #     pygame.mixer.music.load('Musicas/03 - Its Christmas (Modern Talking).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Modern Talking - Its Christmas'
        # elif numero == 10:
        #     pygame.mixer.music.load('Musicas/04 - The Firs Nöel (Whitney Houston).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Whitney Houston - The Firs Nöel'
        # elif numero == 11:
        #     pygame.mixer.music.load('Musicas/05 - Jingle Bells (Boney M.).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Boney M. - Jingle Bells'
        # elif numero == 12:
        #     pygame.mixer.music.load('Musicas/06 - I Saw Mommy Kissing Santa Claus (Jimmy Boyd).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Jimmy Boyd - I Saw Mommy Kissing Santa Claus'
        # elif numero == 13:
        #     pygame.mixer.music.load('Musicas/07 - Its The Most Wonderful Of The Year (Andy Williams).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Andy Williams - Its The Most Wonderful Of The Year'
        # elif numero == 14:
        #     pygame.mixer.music.load('Musicas/08 - O Come All Ye Faithful (Art Garfunkel).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Art Garfunkel - O Come All Ye Faithful'
        # elif numero == 15:
        #     pygame.mixer.music.load('Musicas/09 - Rudolph The Red Nosed Reindeer (John Denver).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando John Denver - Rudolph The Red Nosed Reindeer'
        # elif numero == 16:
        #     pygame.mixer.music.load('Musicas/10 - Bells Are Ringing (Mary Chapin Carpenter).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Mary Chapin Carpenter - Bells Are Ringing'
        # elif numero == 17:
        #     pygame.mixer.music.load('Musicas/11 - Last Christmas (Wham!).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Wham! - Last Christmas'
        # elif numero == 18:
        #     pygame.mixer.music.load('Musicas/12 - Christmas Ill Be Steppin (R. Kelly).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando R. Kelly - Christmas I will Be Steppin'
        # elif numero == 19:
        #     pygame.mixer.music.load('Musicas/13 - Christmas Time (Backstreet Boys).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Backstreet Boys - Christmas Time'
        # elif numero == 20:
        #     pygame.mixer.music.load('Musicas/14 - This Christmas (Chris Brown).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Chris Brown - This Christmas'
        # elif numero == 21:
        #     pygame.mixer.music.load('Musicas/15 - Merry, Merry Christmas (New Kids On The Block).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando New Kids On The Block - Merry, Merry Christmas'
        # elif numero == 22:
        #     pygame.mixer.music.load('Musicas/16 - Frosty The Snowman (Willie Nelson).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Willie Nelson - Frosty The Snowman'
        # elif numero == 23:
        #     pygame.mixer.music.load('Musicas/17 - Let It Snow! Let It Snow! Let It Snow! (Frank Sinatra With The B. Swanson Quartet).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Let It Snow! Let It Snow! Let It Snow! - Frank Sinatra With The B. Swanson Quartet'
        # elif numero == 24:
        #     pygame.mixer.music.load('Musicas/18 - Little Drummer Boy (Johnny Cash).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Johnny Cash - Little Drummer Boy'
        # elif numero == 25:
        #     pygame.mixer.music.load('Musicas/19 - We Wish You A Merry Christmas (Patti Page).mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando Patti Page - We Wish You A Merry Christmas'
        # elif numero == 26:
        #     pygame.mixer.music.load('Musicas/Conquistador Barato.mp3')
        #     pygame.mixer.music.play()
        #     pygame.event.wait()
        #     return 'Tocando The Malufs - Conquistador Barato'    
        # else:
        #     return 'Música não encontrada'

