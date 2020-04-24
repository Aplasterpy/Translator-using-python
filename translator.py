from googletrans import Translator
trans = Translator()
t = trans.translate('bom dia')
print(f'source : {t.src}')          # source language
print(f'destination : {t.dest}')    #destination language.. its default is in english
print(f'{t.origin} -> {t.text}')

#list supported languages

from googletrans import LANGUAGES
for lang in LANGUAGES:
    print(f'{lang} - {LANGUAGES[lang]}')

# list possible mistake and translations

pm = t.extra_data['possible-mistakes']
pt  = t.extra_data['possible-Translation']

print(f'possible mistakes: {pm}')
print(f'possible Translation: {pt}')
 