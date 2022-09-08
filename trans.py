from googletrans import Translator
import speech_recognition as sr
import pyttsx3


translator = Translator()


#test_1 = input('Enter text to translate: ')
#language_1 = input('Enter Language: ')

language = {
     'afrikaans'   : 'af',   'albanian'    : 'sq',  'amharic'     : 'am',   'arabic'      : 'ar',   'armenian'    : 'hy', 
  'azerbaijani' : 'az',   'basque' : 'eu',   'belarusian'  : 'be',  'bengali'     : 'bn',   'bosnian'     : 'bs', 
  'bulgarian'   : 'bg',  'catalan' : 'ca',  'cebuano'   : 'ceb',  'chichewa'  : 'ny', 'chinese (simplified)'   :'zh-cn',
   'chinese (traditional)'  :'zh-tw', 'corsican':'co', 'croatian'        :'hr',  'czech'  :'cs',
   'danish':'da', 'dutch'  :'nl', 'english' :'en',  'esperanto'       :'eo', 'estonian'        :'et',
   'filipino' :'tl', 'finnish':'fi', 'french' :'fr', 'frisian':'fy','galician':'gl', 'georgian' :'ka',
   'german'  :'de', 'greek'  :'el','gujarati' :'gu','haitian creole'  :'ht','hausa' :'ha',
    'hawaiian':'haw','hebrew':'iw','hebrew':'he','hindi':'hi','hmong':'hmn','hungarian':'hu', 
   'icelandic':'is', 'igbo':'ig','indonesian':'id','irish':'ga','italian':'it','japanese':'ja',
   'javanese':'jw','kannada':'kn','kazakh' :'kk','khmer':'km','korean':'ko','kurdish (kurmanji)' :'ku',
   'kyrgyz' :'ky', 'lao':'lo','latin' :'la','latvian':'lv','lithuanian':'lt','luxembourgish':'lb',
   'macedonian':'mk', 'malagasy':'mg','malay':'ms','malayalam' :'ml','maltese':'mt','maori':'mi',
   'marathi':'mr', 'mongolian'  :'mn','myanmar (burmese)' :'my','nepali':'ne','norwegian':'no',
   'odia':'or', 'pashto' :'ps','persian' :'fa','polish':'pl','portuguese':'pt','punjabi':'pa',
   'romanian':'ro','russian':'ru','samoan':'sm','scots gaelic':'gd','serbian':'sr','sesotho':'st', 
   'shona':'sn','sindhi':'sd','sinhala':'si', 'slovak':'sk','slovenian':'sl','somali':'so','spanish':'es',
   'sundanese':'su', 'swahili':'sw','swedish':'sv','tajik':'tg','tamil':'ta','telugu':'te','thai':'th',
   'turkish':'tr','ukrainian':'uk','urdu':'ur','uyghur':'ug','uzbek':'uz','vietnamese':'vi',
   'welsh':'cy','xhosa':'xh','yiddish':'yi','yoruba':'yo','zulu':'zu'
}

choice = input("Enter 'V' for  voice or 'T' for Text : ")

if choice.upper() == 'T':
    test_1 = input('Enter text to translate: ')
    language_1 = input('Enter Language: ')

    destin = (language[language_1.lower() ])

    out = translator.translate(test_1, dest=destin)

    print('Translated text is : '+ out.text) 
else:

    language_1 = input('Enter Language to transalte to : ')
    print('Speak Phrase to Translate')
    

    # Initialize the recognizer
    r = sr.Recognizer()
    while(1):
            
        
        # exceptions at the runtime
        try:
            
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                speech = r.recognize_google(audio2)
                speech = speech.lower()

                print("Did you say "+speech)
                #SpeakText(speech)
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occured")
    
    test_1 =  speech

    destin = (language[language_1.lower() ])

    out = translator.translate(test_1, dest=destin)

    print('Translated text is: '+ out.text) 
