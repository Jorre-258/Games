import random

def rules():
    print("Welkom bij Galgje!")
    print("Het doel van het spel is om het woord te raden door letters te raden.")
    print("Je hebt een beperkt aantal pogingen voordat de 'galg' compleet is.")
    print("Als je alle letters van het woord raadt voordat de 'galg' compleet is, win je het spel.")
    print("Als de 'galg' compleet is voordat je het woord raadt, verlies je het spel.")
    print("Hier zijn de regels:")
    print("1. Het spel selecteert willekeurig een woord uit een lijst.")
    print("2. Je kunt letters raden door ze in te voeren.")
    print("3. Als de letter in het woord voorkomt, wordt deze onthuld. Als de letter meerdere keren voorkomt, worden alle voorkomens onthuld.")
    print("4. Als de letter niet in het woord voorkomt, verlies je een poging.")
    print("5. Je kunt geen letters raden die je al eerder hebt geraden.")
    print("Veel succes en veel plezier met Galgje")

def random_word():
    words = [
        'rood', 'blauw', 'groen', 'geel', 'oranje', 'paars', 'roze', 'wit', 'zwart', 'grijs',
        'hond', 'kat', 'vogel', 'vis', 'paard', 'konijn', 'leeuw', 'tijger', 'olifant', 'giraffe', 'aap', 'beer', 'koe',
        'schaap', 'geit', 'kip', 'eend', 'slang', 'schildpad', 'krokodil',
        'appel', 'banaan', 'peer', 'sinaasappel', 'aardbei', 'druif', 'ananas', 'wortel', 'tomaat', 'aardappel',
        'brood', 'kaas', 'melk', 'boter', 'ei', 'vlees', 'vis', 'rijst', 'pasta', 'pizza',
        'dokter', 'leraar', 'ingenieur', 'muzikant', 'schilder', 'schrijver', 'kok', 'politieagent', 'brandweerman',
        'verpleegster',
        'auto', 'fiets', 'trein', 'bus', 'vliegtuig', 'boot', 'motor', 'vrachtwagen', 'helikopter', 'scooter',
        'appel', 'banaan', 'sinaasappel', 'peer', 'druif', 'aardbei', 'framboos', 'meloen', 'kiwi', 'perzik',
        'shirt', 'broek', 'jurk', 'trui', 'jas', 'sokken', 'schoenen', 'hoed', 'handschoenen', 'riem',
        'hoofd', 'oog', 'neus', 'mond', 'oor', 'hand', 'been', 'voet', 'hart', 'rug'
    ]
    random_word = random.choice(words)
    return random_word

def correct_word():
    pass

def ask_word():
    word = input()
    return word

def wrong_word():
    pass

def main():
    r_word = random_word()
    print(r_word)
    print('*' * len(r_word))
    while True:
        user_word = input("Welke letters zijn er in het woord?:")
        for letter, index in enumerate(user_word):
            if letter in r_word:
                print(letter, index)





main()