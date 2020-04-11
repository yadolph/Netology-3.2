import requests


API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(source_file, dest_file, from_lang, to_lang='ru'):

    text_raw = []

    with open(source_file, 'r', encoding='utf-8') as file:
        for line in file:
            text_raw.append(line.strip())

    text_for_translation = '|'.join(text_raw)

    params = {
        'key': API_KEY,
        'text': text_for_translation,
        'lang': f'{from_lang}-{to_lang}'
    }

    response = requests.get(URL, params=params)
    translated_text_json = response.json()

    translated_text = translated_text_json['text'][0].split('|')

    with open(dest_file, 'w') as file:
        for line in translated_text:
            file.write(line + '\n')

translate_it('DE.txt', 'DE_RU.txt', 'de')
translate_it('FR.txt', 'FR_RU.txt', 'fr')
translate_it('ES.txt', 'ES_RU.txt', 'es')
