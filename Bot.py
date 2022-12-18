from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from Lista_Musicas import addMusic, playPlaylistMusics, listView, skip
import pygame
import string
from random import randrange
import time

pygame.init()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Mensagem enviada
    msg = request.form.get('Body')
    msg = msg.casefold()
    print(msg)
    # Mensagem a ser enviada pelo bot
    resp = MessagingResponse()

    if msg == 'oi' or msg == 'Oi':
        resp.message('Oi!') 
    
    elif msg == 'Comandos' or msg == 'comandos':
        resp.message('Os comandos do Bot são: Gatos e Som')

    elif msg == 'gatos' or msg == 'Gatos':
        resp.message().media('https://cataas.com/cat')

    elif msg == 'som' or msg == 'Som':
        resp.message('*REGRAS*\n\n*Para tocar a música coloque Play*\n\n*Para adicionar uma música coloque:*\n\n*Tocar (Número da Música)*\n\n*Caso queira pular a música digite Skip*\n\n*Caso queira parar a música digite Parar*\n\n*Caso queira tocar uma musica aleatória digite Tocar Random*\n\n *Para ver a playlist coloque Playlist*\n\n*Lista de Músicas:*\n\n1. All I Want for Christmas Is You\n2. Frank Sinatra - Jingle Bells\n3. Spidey Bells\n4. Jingle Bell Rock\n5. Dean Martin - Let it Snow!\n6. Its Beginning To Look A Lot Like Christmas\n7. What A Wonderfull World\n8. Westlife - I Have A Dream\n9. Modern Talking - Its Christmas\n10. Whitney Houston - The Firs Nöel\n11. Boney M. - Jingle Bells\n12. Jimmy Boyd - I Saw Mommy Kissing Santa Claus\n13. Andy Williams - Its The Most Wonderful Of The Year\n14. Art Garfunkel - O Come All Ye Faithful\n15. John Denver - Rudolph The Red Nosed Reindeer\n16. Mary Chapin Carpenter - Bells Are Ringing\n17. Wham! - Last Christmas\n18. R. Kelly - Christmas I will Be Steppin\n19. Backstreet Boys - Christmas Time\n20. Chris Brown - This Christmas\n21. New Kids On The Block - Merry, Merry Christmas\n22. Willie Nelson - Frosty The Snowman\n23. Let It Snow! Let It Snow! Let It Snow! - Frank Sinatra With The B. Swanson Quartet\n24. Johnny Cash - Little Drummer Boy\n25. Patti Page - We Wish You A Merry Christmas\n26. The Malufs - Conquistador Barato')
    
    elif msg == 'Tocar' or msg == 'tocar':
        resp.message('*Para usar este comando:*\n*Tocar (Número da Música)*')
    
    elif msg == 'tocar random':
        aleatorio = randrange(27)     
        resp.message(addMusic(int(aleatorio)))
    
    elif msg == 'parar':
        pygame.mixer.music.stop()
    
    elif msg == 'playlist':
        resp.message(listView())
    
    elif msg == 'skip':
        resp.message(skip())

    elif msg == 'play':
        playPlaylistMusics()
        
    else:
        lista = [] 
        musica = ''
        for x in msg:
            if lista == ['t','o','c','a','r']:
                musica = musica+x
            if x in string.ascii_lowercase:
                lista.append(x)
        if lista == ['t','o','c','a','r']:
            resp.message(addMusic(int(musica))) #Começo
            #tocar_musica(int(musica))
            #resp.message(tocar_musica(int(musica)))
        else:
            resp.message('Sua mensagem foi: ' + msg)
    print(resp)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
