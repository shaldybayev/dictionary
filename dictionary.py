# dictionary.py

import json
import random
import os

SUPPORTED_LANGUAGES = {
    "en": "English",
    "ru": "Русский",
    "fr": "Français",
    "es": "Español",
    "kk": "Қазақша",
    "zh": "中文",
    "ko": "한국어",
    "ja": "日本語"
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_interface_language():
    print("Select your interface language / Выберите язык интерфейса:")
    for code, name in SUPPORTED_LANGUAGES.items():
        print(f"{code}: {name}")
    while True:
        lang = input("Language code: ").strip().lower()
        if lang in SUPPORTED_LANGUAGES:
            return lang
        else:
            print("Unsupported language code. Try again.")

def load_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_words(words, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=4)

def normalize(text):
    return text.lower().strip()

def quiz(words, lang):
    correct = 0
    total = 0
    mistakes = {}
    unused_words = list(words.items())
    random.shuffle(unused_words)

    interface = translations[lang]

    while unused_words:
        eng, translations_list = unused_words.pop()
        total += 1
        print(f"{interface['translate']}: {eng}")
        answer = input("-> ").strip()

        if answer.lower() in ('q', 'quit', 'e', 'exit'):
            break

        answer_normalized = normalize(answer)
        valid_answers = [normalize(t) for t in translations_list]

        if answer_normalized in valid_answers:
            print(interface['correct'])
            correct += 1
        else:
            print(interface['wrong'])
            print(f"{interface['correct_answers']}: {', '.join(translations_list)}")
            mistakes[eng] = translations_list
        print()

    print(interface['results'])
    print(f"{interface['score']}: {correct}/{total}")
    if mistakes:
        print(interface['mistakes'] + ":")
        for word, correct_list in mistakes.items():
            print(f"{word}: {', '.join(correct_list)}")

    input(interface['press_enter'])

def add_word(words, lang):
    interface = translations[lang]
    eng = input(interface['enter_english']).strip()
    translation = input(interface['enter_translation']).strip()
    if eng in words:
        words[eng].extend([t.strip() for t in translation.split(',') if t.strip() not in words[eng]])
    else:
        words[eng] = [t.strip() for t in translation.split(',') if t.strip()]
    print(interface['word_added'])

def edit_word(words, lang):
    interface = translations[lang]
    eng = input(interface['edit_prompt']).strip()
    if eng in words:
        print(f"{interface['current_translations']}: {', '.join(words[eng])}")
        new_translations = input(interface['new_translations']).strip()
        words[eng] = [t.strip() for t in new_translations.split(',') if t.strip()]
        print(interface['word_updated'])
    else:
        print(interface['word_not_found'])

def main():
    lang = get_interface_language()
    interface = translations[lang]
    filename = 'words.json'
    words = load_words(filename)

    while True:
        clear()
        print("=== Dictionary Trainer ===")
        print("1.", interface['start_quiz'])
        print("2.", interface['add_word'])
        print("3.", interface['edit_word'])
        print("4.", interface['exit'])
        choice = input("-> ").strip()

        if choice == '1':
            quiz(words, lang)
        elif choice == '2':
            add_word(words, lang)
            save_words(words, filename)
        elif choice == '3':
            edit_word(words, lang)
            save_words(words, filename)
        elif choice == '4':
            break
        else:
            print(interface['invalid_option'])
            input("Press Enter...")

translations = {
    "en": {
        "translate": "Translate the word",
        "correct": "✅ Correct!",
        "wrong": "❌ Incorrect.",
        "correct_answers": "Correct answers",
        "results": "Quiz Results",
        "score": "Score",
        "mistakes": "Your mistakes",
        "press_enter": "Press Enter to continue...",
        "enter_english": "Enter the English word:",
        "enter_translation": "Enter translations (comma-separated):",
        "word_added": "Word added!",
        "edit_prompt": "Enter the English word you want to edit:",
        "current_translations": "Current translations",
        "new_translations": "Enter new translations (comma-separated):",
        "word_updated": "Word updated!",
        "word_not_found": "Word not found.",
        "start_quiz": "Start Quiz",
        "add_word": "Add a New Word",
        "edit_word": "Edit an Existing Word",
        "exit": "Exit",
        "invalid_option": "Invalid option. Try again."
    },
    "ru": {
        "translate": "Переведите слово",
        "correct": "✅ Верно!",
        "wrong": "❌ Неверно.",
        "correct_answers": "Правильные ответы",
        "results": "Результаты викторины",
        "score": "Счет",
        "mistakes": "Ваши ошибки",
        "press_enter": "Нажмите Enter, чтобы продолжить...",
        "enter_english": "Введите слово на английском:",
        "enter_translation": "Введите переводы (через запятую):",
        "word_added": "Слово добавлено!",
        "edit_prompt": "Введите слово на английском для редактирования:",
        "current_translations": "Текущие переводы",
        "new_translations": "Введите новые переводы (через запятую):",
        "word_updated": "Слово обновлено!",
        "word_not_found": "Слово не найдено.",
        "start_quiz": "Начать викторину",
        "add_word": "Добавить новое слово",
        "edit_word": "Редактировать слово",
        "exit": "Выход",
        "invalid_option": "Неверный вариант. Попробуйте снова."
    },
    "fr": {
        "translate": "Traduisez le mot",
        "correct": "✅ Correct !",
        "wrong": "❌ Incorrect.",
        "correct_answers": "Réponses correctes",
        "results": "Résultats du quiz",
        "score": "Score",
        "mistakes": "Vos erreurs",
        "press_enter": "Appuyez sur Entrée pour continuer...",
        "enter_english": "Entrez le mot anglais:",
        "enter_translation": "Entrez les traductions (séparées par des virgules):",
        "word_added": "Mot ajouté !",
        "edit_prompt": "Entrez le mot anglais à modifier:",
        "current_translations": "Traductions actuelles",
        "new_translations": "Entrez les nouvelles traductions (séparées par des virgules):",
        "word_updated": "Mot mis à jour !",
        "word_not_found": "Mot non trouvé.",
        "start_quiz": "Commencer le quiz",
        "add_word": "Ajouter un nouveau mot",
        "edit_word": "Modifier un mot existant",
        "exit": "Quitter",
        "invalid_option": "Option invalide. Réessayez."
    }
    # Можно добавить и другие языки по аналогии
}

if __name__ == "__main__":
    main()

