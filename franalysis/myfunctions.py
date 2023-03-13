from operator import itemgetter

abc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
chastota = ['о', 'е', 'а', 'и', 'н', 'т', 'с', 'р', 'в', 'л', 'к', 'м', 'д', 'п', 'у', 'я', 'ы', 'ь', 'г', 'з', 'б', 'ч', 'й', 'х']

def top_letter_detect(text: str):
    """
    Create a list of letters and amount of them from the most popular letter in the text to less popular.
    
    Argument must be str

    :param text: text
    :return: top of the letters and amount of them sorted by the popularity.
    """

    #convert str text to list object
    phrase = list(text.lower())

    #create variables for loop
    top = 0
    top_letter = {}

    #counting amounts of letters and appending list with pairs of letters and amounts of them
    for i in abc:
        if phrase.count(i) > top:
            top = phrase.count(i)
            top_letter[i] = phrase.count(i)
    
    #sort letter from the most popular to less
    top_letter = list(map(list, dict(sorted(top_letter.items(), key=itemgetter(1))).items()))

    return top_letter


def find_key(top_letter_list: list):
    """
    Finds key of crypted text by Cezars crypting
    
    Argument must be list

    :param top_letter_list: Sorted by popuarity list of letters
    :return: key of crypted text
    """
    key = 0
    x = -1
    while key == 0:
        key = abc.index(top_letter_list[x][0]) - abc.index(chastota[x*(-1) - 1])
        x -= 1
    print('Ключ:', key)

    return key


def encrypt(key: int, text: str):
    """
    Encrypt Cezars text with key

    key must be int
    text must be str

    :param key: key of crypted text
    :param text: crypted text
    :return: encrypted text
    """

    phrase = list(text.lower())
    rez = []
    for i in range(len(phrase)):
        if phrase[i] in abc:
            y = abc.index(phrase[i]) - key
            if y > 32:
                y -= 33
            rez += abc[y]
        else:
            rez += phrase[i]
    
    return ''.join(rez)
