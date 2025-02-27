import random
import re

class ElizaChatbot:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name', 'Eliza')
        self.user_name = kwargs.get('user_name', 'User')
        self.responses = kwargs.get('responses', self.default_responses())
        self.keywords = kwargs.get('keywords', self.default_keywords())

    def default_responses(self):
        return {
            'greeting': ['Hallo! Wie kann ich dir helfen?', 'Hi, wie geht es dir?'],
            'goodbye': ['Auf Wiedersehen!', 'Tschüss, bis bald!'],
            'question': ['Interessante Frage, erzähl mir mehr!', 'Warum fragst du das?'],
            'default': ['Erzähl mir mehr...', 'Ich verstehe. Kannst du das näher erläutern?']
        }

    def default_keywords(self):
        return {
            'greeting': ['hallo', 'hi', 'hey', 'guten tag'],
            'goodbye': ['tschüss', 'auf wiedersehen', 'bye'],
            'question': ['warum', 'wie', 'was', 'wo', 'wann'],
        }

    def match_pattern(self, user_input, *args, **kwargs):
        user_input = user_input.lower()

        # Innere Funktion für Keyword-Suche
        def find_matching_keyword(user_input, keywords):
            return any(keyword in user_input for keyword in keywords)

        # Suchen nach Schlüsselwörtern
        for key, keywords in self.keywords.items():
            if find_matching_keyword(user_input, keywords):
                return self.generate_response(key)

        # Rückfallantwort, wenn kein Muster erkannt wird
        return self.responses['default']

    def generate_response(self, key):
        # Innere Funktion zur Auswahl einer zufälligen Antwort
        def random_choice(responses):
            return random.choice(responses)
        
        if key in self.responses:
            return random_choice(self.responses[key])
        return self.responses['default']

    def process_input(self, *args, **kwargs):
        """Verarbeitet die Benutzereingabe und gibt eine Antwort zurück."""
        user_input = args[0]
        
        # Innere Funktion zur Beendigung des Chats
        def should_exit(user_input):
            return 'exit' in user_input.lower()
        
        if should_exit(user_input):
            return self.responses['goodbye'][0]
        return self.match_pattern(user_input, *args, **kwargs)

    def chat(self):
        print(f"Willkommen bei {self.name}!\nTippe 'exit' zum Beenden.")
        while True:
            user_input = input(f"{self.user_name}: ")
            response = self.process_input(user_input)
            print(f"{self.name}: {response}")
            if 'exit' in user_input.lower():
                break

# Beispiel für Chatbot mit benutzerdefinierten Parametern
chatbot = ElizaChatbot(
    name='ELIZA', 
    user_name='Luna',
    responses={
        'greeting': ['Hallo, Luna! Wie kann ich dir helfen?', 'Hi Luna, was ist los?'],
        'goodbye': ['Auf Wiedersehen, Luna!', 'Tschüss, bis bald Luna!'],
        'question': ['Das ist eine interessante Frage. Kannst du mehr dazu sagen?', 'Was denkst du darüber?'],
        'default': ['Erzähl mir mehr darüber...', 'Ich höre dir zu, bitte fahre fort.']
    },
    keywords={
        'greeting': ['hallo', 'hi', 'hey', 'guten tag'],
        'goodbye': ['tschüss', 'auf wiedersehen', 'bye'],
        'question': ['warum', 'wie', 'was', 'wo', 'wann'],
    }
)

chatbot.chat()
