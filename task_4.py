from googletrans import Translator

def open_file():
	try:
		with open('my_text_4.txt', 'r', encoding='utf-8') as eng_file:
			translator = Translator()
			str_eng_file = eng_file.read()
			ru_file = translator.translate(str_eng_file, dest='ru')
			ru_file_text = ru_file.text
		with open('ru_text_4.txt', 'w+', encoding='utf-8') as ru:
			print(ru_file_text, file=ru)
			return ru.read()

	except:
		print('Error!')

print(open_file())