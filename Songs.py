from pygame import mixer
from random import choice
from time import sleep
from os import system
mixer.init()

# As músicas da playlist
m1 = './Musics/thunder.mp3'
m2 = './Musics/legends_never_die.mp3'
m3 = './Musics/hall_of_fame.mp3'
m4 = './Musics/industry_baby8d.mp3'
m5 = './Musics/believer.mp3'
m6 = './Musics/good_4_u.mp3'
m7 = './Musics/warriors.mp3'
m8 = './Musics/enemy.mp3'
m9 = './Musics/natural.mp3'
m10 = './Musics/sunflower100d.mp3'
m11 = './Musics/radioactive.mp3'
m12 = './Musics/memories.mp3'
m13 = './Musics/back_in_black.mp3'
m14 = '/Videos/Zelda/gerudo_valley.mp3'
m15 = '/Videos/Zelda/main_theme.mp3'
m16 = '/Videos/Zelda/song_of_storms.mp3'
m17 = '/Videos/Zelda/zelda_lullaby.mp3'
m18 = './Musics/whatever_it_takes.mp3'
m19 = './Musics/demons.mp3'
m20 = './Musics/por_supuesto.mp3'
m21 = './Musics/bones.mp3'
m22 = './Musics/stand_up.mp3'
m23 = './Musics/birds.mp3'
m24 = './Musics/follow_you.mp3'
m25 = './Musics/its_time.mp3'
m26 = './Musics/im_so_sorry.mp3'
m27 = './Musics/nothing_left_to_say.mp3'
m28 = './Musics/rise.mp3'

songs = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12,
m13, m18, m19, m20, m21, m22, m23, m24, m25, m26, m27, m28]

# Duração de cada música
dic = {
    m1: 183,
    m2: 235,
    m3: 202,
    m4: 212,
    m5: 204,
    m6: 179,
    m7: 171,
    m8: 176,
    m9: 191,
    m10: 155,
    m11: 189,
    m12: 189,
    m13: 253,
    m14: 272,
    m15: 263,
    m16: 198,
    m17: 195,
    m18: 199,
    m19: 183,
    m20: 187,
    m21: 175,
    m22: 224,
    m23: 223,
    m24: 177,
    m25: 242,
    m26: 395,
    m27: 230,
    m28: 210
    }

# Nome de cada música
nomes = {
    m1: 'Thunder - Imagine Dragons',
    m2: 'Legends Never Die - League of Legends, Against the Current',
    m3: 'Hall of Fame - The Script',
    m4: 'Industry Baby - Lil Nas X, Jack Harlow',
    m5: 'Believer - Imagine Dragons',
    m6: 'Good 4 U - Olivia Rodrigo',
    m7: 'Warriors - League of Legends, Imagine Dragons',
    m8: 'Enemy - Imagine Dragons, J.I.D',
    m9: 'Natural - Imagine Dragons',
    m10: 'Sunflower - Post Malone, Swae Lee',
    m11: 'Radioactive - Imagine Dragons',
    m12: 'Memories - Maroon 5',
    m13: 'Back In Black - AC/DC',
    m14: 'Gerudo Valley (The Legend of Zelda) - Koji Kondo',
    m15: 'The Legend of Zelda: Main Theme - Koji Kondo',
    m16: 'Song of Storms (The Legend of Zelda) - Koji Kondo',
    m17: "Zelda's Lullaby (The Legend of Zelda) - Koji Kondo",
    m18: 'Whatever It Takes - Imagine Dragons',
    m19: 'Demons - Imagine Dragons',
    m20: 'Por Supuesto - Marina Sena',
    m21: 'Bones - Imagine Dragons',
    m22: 'Stand Up - Cynthia Erivo',
    m23: 'Birds - Imagine Dragons',
    m24: 'Follow You - Imagine Dragons',
    m25: "It's Time - Imagine Dragons",
    m26: "I'm So Sorry - Imagine Dragons",
    m27: 'Nothing Left to Say - Imagine Dragons',
    m28: 'Rise - League of Legends, The Glitch Mob, Mako, The Word Alive'
    }

# Nomes para pesquisa de cada música
search = {
    m1: 'Thunder',
    m2: 'Legends Never Die',
    m3: 'Hall Of Fame',
    m4: 'Industry Baby',
    m5: 'Believer',
    m6: 'Good 4 U',
    m7: 'Warriors',
    m8: 'Enemy',
    m9: 'Natural',
    m10: 'Sunflower',
    m11: 'Radioactive',
    m12: 'Memories',
    m13: 'Back In Black',
    m14: 'Gerudo Valley',
    m15: 'Zelda Main Theme',
    m16: 'Song Of Storms',
    m17: "Zelda's Lullaby",
    m18: 'Whatever It Takes',
    m19: 'Demons',
    m20: 'Por Supuesto',
    m21: 'Bones',
    m22: 'Stand Up',
    m23: 'Birds',
    m24: 'Follow You',
    m25: "It's Time",
    m26: "I'm So Sorry",
    m27: 'Nothing Left To Say',
    m28: 'Rise'
}

system('cls')
print('Que modo você deseja?')
diga = input('Automático (A), Manual (M) ou Música Específica (E): ').upper().strip()
system('cls')

if diga == 'A':
    while len(songs) > 0:
        c = choice(songs) # Escolha da música
        mixer.music.load(c) # Carregamento da música
        mixer.music.play() # Reprodução da música
        print('='*26)
        print(f'SpotPython :) - {len(songs)} músicas')
        print('='*26)
        print(f'Tocando {nomes[c]}...')
        sleep(dic[c])
        sleep(3)
        songs.pop(songs.index(c)) # Eliminação da música escolhida
        system('cls') # Limpeza do terminal ao final da música

elif diga == 'M':
    while len(songs) > 0:
        ch = choice(songs)
        mixer.music.load(ch)
        mixer.music.play()
        print('='*26)
        print(f'SpotPython :) - {len(songs)} músicas')
        print('='*26)
        print(f'Tocando {nomes[ch]}...')
        
        contrl = 0
        while contrl == 0:

            if len(songs) == 1:
                decide = input('Pause (P), Restart (A) or Stop (S): ').upper().strip()

                if decide == 'P':
                    mixer.music.pause()
                    decide2 = input('Resume (R), Restart (A) or Stop (S): ').upper().strip()

                    if decide2 == 'R':
                        mixer.music.unpause()
                    
                    elif decide2 == 'A':
                        mixer.music.stop()
                        mixer.music.load(ch)
                        mixer.music.load()

                    elif decide2 == 'S':
                        mixer.music.stop()
                        songs.clear()
                        contrl = contrl + 1
                
                elif decide == 'A':
                    mixer.music.stop()
                    mixer.music.load(ch)
                    mixer.music.play()

                elif decide == 'S':
                    mixer.music.stop()
                    songs.clear()
                    contrl = contrl + 1

            else:
                decide3 = input('Pause (P), Restart (A), Stop (S) or Next Song (N): ').upper().strip()
                if decide3 == 'P':
                    mixer.music.pause()
                    decide4 = input('Resume (R), Restart (A), Stop (S) or Next Song (N): ').upper().strip()

                    if decide4 == 'R':
                        mixer.music.unpause()
                    
                    elif decide4 == 'A':
                        mixer.music.stop()
                        mixer.music.load(ch)
                        mixer.music.play()

                    elif decide4 == 'S':
                        mixer.music.stop()
                        songs.clear()
                        contrl = contrl + 1

                    elif decide4 == 'N':
                        mixer.music.stop()
                        contrl = contrl + 1
                        songs.pop(songs.index(ch))
                        system('cls')
                
                elif decide3 == 'A':
                    mixer.music.stop()
                    mixer.music.load(ch)
                    mixer.music.play()

                elif decide3 == 'S':
                    mixer.music.stop()
                    songs.clear()
                    contrl = contrl + 1
                
                elif decide3 == 'N':
                    mixer.music.stop()
                    contrl = contrl + 1
                    songs.pop(songs.index(ch))
                    system('cls')

elif diga == 'E':
    print('Ok! Estas são suas opções:')
    print('-='*10)
    for valor in search.values():
        print(f'* {valor}')
    print('-='*10)
    music = input('Qual música você gostaria de ouvir?: ').title().strip()
    for chave in search.keys():
        if music == search[chave]:
            system('cls')
            print('='*13)
            print('SpotPython :)')
            print('='*13)
            print(f'Tocando {nomes[chave]}...')
            mixer.music.load(chave)
            mixer.music.play()
            sleep(dic[chave])
