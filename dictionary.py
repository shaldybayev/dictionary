import json
import os
import random

interface_languages = ["English", "Русский", "Français", "Español"]
translation_pairs = [
    ("English", "Russian"),
    ("English", "French"),
    ("English", "Spanish"),
    ("English", "Kazakh"),
    ("English", "Chinese"),
    ("English", "Korean"),
    ("English", "Japanese")
]

translations = {
    "select_interface_language": {
        "English": "Select interface language:",
        "Русский": "Выберите язык интерфейса:",
        "Français": "Choisissez la langue d’interface :",
        "Español": "Elige el idioma de la interfaz:"
    },
    "select_translation_pair": {
        "English": "Choose language pair for quiz:",
        "Русский": "Выберите языковую пару для тренировки:",
        "Français": "Choisissez une paire de langues pour l’entraînement :",
        "Español": "Elige un par de idiomas para entrenar:"
    },
    "menu": {
        "English": "\n1. Add word\n2. Start quiz\n3. Show words\n4. Show mistakes\n5. Exit",
        "Русский": "\n1. Добавить слово\n2. Начать тест\n3. Показать слова\n4. Показать ошибки\n5. Выход",
        "Français": "\n1. Ajouter un mot\n2. Démarrer le quiz\n3. Afficher les mots\n4. Afficher les erreurs\n5. Quitter",
        "Español": "\n1. Agregar palabra\n2. Comenzar prueba\n3. Mostrar palabras\n4. Mostrar errores\n5. Salir"
    },
    "choice": {
        "English": "Enter your choice: ",
        "Русский": "Введите ваш выбор: ",
        "Français": "Votre choix : ",
        "Español": "Tu elección: "
    },
    "enter_word": {
        "English": "Enter English word: ",
        "Русский": "Введите английское слово: ",
        "Français": "Entrez le mot anglais : ",
        "Español": "Ingresa la palabra en inglés: "
    },
    "enter_translation": {
        "English": "Enter translation: ",
        "Русский": "Введите перевод: ",
        "Français": "Entrez la traduction : ",
        "Español": "Ingresa la traducción: "
    },
    "correct": {
        "English": "Correct!",
        "Русский": "Верно!",
        "Français": "Correct !",
        "Español": "¡Correcto!"
    },
    "wrong": {
        "English": "Wrong. Correct answer(s):",
        "Русский": "Неверно. Правильный ответ(ы):",
        "Français": "Faux. Bonne(s) réponse(s) :",
        "Español": "Incorrecto. Respuesta(s) correcta(s):"
    },
    "exit_quiz": {
        "English": "Type Q or E to quit",
        "Русский": "Введите Q или E, чтобы выйти",
        "Français": "Tapez Q ou E pour quitter",
        "Español": "Escribe Q o E para salir"
    }
}

def get_translation(key, lang):
    return translations.get(key, {}).get(lang, key)

def load_words(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_words(words, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

def quiz(words, interface_lang, mistakes_file):
    keys = list(words.keys())
    if not keys:
        print("No words added yet.")
        return

    print(get_translation("exit_quiz", interface_lang))
    while True:
        word = random.choice(keys)
        correct_answers = [t.strip().lower() for t in words[word]]

        user_input = input(f"{word}: ").strip().lower()
        if user_input in ('q', 'quit', 'e', 'exit'):
            break

        if user_input in correct_answers:
            print(get_translation("correct", interface_lang))
        else:
            print(get_translation("wrong", interface_lang), ", ".join(words[word]))
            record_mistake(mistakes_file, word, user_input)

def record_mistake(filename, word, wrong_answer):
    mistakes = load_words(filename)
    if word not in mistakes:
        mistakes[word] = []
    mistakes[word].append(wrong_answer)
    save_words(mistakes, filename)

def show_words(words):
    for word, translations in words.items():
        print(f"{word} — {', '.join(translations)}")

def show_mistakes(filename):
    mistakes = load_words(filename)
    for word, wrongs in mistakes.items():
        freq = {}
        for answer in wrongs:
            freq[answer] = freq.get(answer, 0) + 1
        sorted_freq = sorted(freq.items(), key=lambda x: -x[1])
        print(f"\n{word}:")
        for ans, count in sorted_freq:
            print(f"  {ans} — {count}x")

def main():
    print("=== Language Quiz App ===")
    for i, lang in enumerate(interface_languages, 1):
        print(f"{i}. {lang}")
    interface_choice = int(input("> ")) - 1
    interface_lang = interface_languages[interface_choice]

    print(get_translation("select_translation_pair", interface_lang))
    for i, (from_lang, to_lang) in enumerate(translation_pairs, 1):
        print(f"{i}. {from_lang} -> {to_lang}")
    pair_choice = int(input("> ")) - 1
    lang_pair = translation_pairs[pair_choice]
    filename = f"words_{lang_pair[0]}_{lang_pair[1]}.json"
    mistakes_file = "mistakes.json"
    words = load_words(filename)

    while True:
        print(get_translation("menu", interface_lang))
        choice = input(get_translation("choice", interface_lang)).strip()

        if choice == '1':
            eng = input(get_translation("enter_word", interface_lang)).strip()
            translation = input(get_translation("enter_translation", interface_lang)).strip()
            if eng in words:
                words[eng].append(translation)
            else:
                words[eng] = [translation]
            save_words(words, filename)
        elif choice == '2':
            quiz(words, interface_lang, mistakes_file)
        elif choice == '3':
            show_words(words)
        elif choice == '4':
            show_mistakes(mistakes_file)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

