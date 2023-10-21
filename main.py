from googletrans import Translator

translator=Translator()

translated=translator.translate("Hello World, This is a test, I would like to be a bird",
                                src='en',
                                dest='es')

print(translated.text)