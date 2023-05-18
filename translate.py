from googletrans import Translator


def tarjima(text1):
    malumot = ""
    tarjimon = Translator()
    lang1 = tarjimon.detect(text1)

    if lang1.lang == 'en':
        tarjima2 = tarjimon.translate(text1, dest='uz').text
        return tarjima2
    elif lang1.lang == 'uz':
        tarjima2 = tarjimon.translate(text1, dest='en').text
        return tarjima2
    else:
        malumot += "Menga ingliz yoki o'zbekcha so'z kiting"
        return malumot


# print(tarjima('hello world'))
