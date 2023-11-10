import random

def replace_char(string, index, replacement):
    string_list = list(string)
    string_list[index] = replacement
    new_string = ''.join(string_list)
    return new_string

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

def main():
    r_word = random_word()
    #print(r_word)
    guess = '*' * len(r_word)
    #print(guess)
    tries = 10
    while True:
        user_word = input("Welke letters zijn er in het woord?: ")
        point = True
        if len(user_word) != 1:
            print("Voer slechts één letter in.")
            continue

        for i in range(len(r_word)):
            if r_word[i] == user_word:
                guess = guess[:i] + user_word + guess[i + 1:]
                point = False
        print(f'{guess}\nJe hebt nog {tries} pogingen over.\n------------------------')

        if tries == 0:
            print("Verloren")
            break

        if point:
            tries -= 1

        if '*' not in guess:
            print("Gewonnen")
            break


main()
