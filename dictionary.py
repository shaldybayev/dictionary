import json
import os
import random

# Интерфейсные переводы
interface_translations = {
    "en": {
        "choose_language": "Choose your interface language:",
        "welcome": "Welcome to the Dictionary Trainer!",
        "choose_pair": "Choose a language pair for translation (e.g., en-ru):",
        "menu": "\nMenu:\n1. Add word\n2. Edit word\n3. Delete word\n4. Show words\n5. Start quiz\n6. Exit",
        "prompt": "> ",
        "enter_english": "Enter English word:",
        "enter_translation": "Enter translation(s), comma-separated:",
        "word_added": "Word added!",
        "word_exists": "Word already exists. Do you want to edit it? (y/n): ",
        "word_not_found": "Word not found.",
        "word_updated": "Word updated!",
        "word_deleted": "Word deleted!",
        "quiz_intro": "Starting quiz. Type 'q' or 'e' to exit.",
        "correct": "Correct!",
        "incorrect": "Incorrect! Correct answers: ",
        "final_score": "Final score:",
        "no_words": "No words available yet.",
        "choose_action": "Choose an action:",
        "goodbye": "Goodbye!"
    },
    "ru": {
        "choose_language": "Выберите язык интерфейса:",
        "welcome": "Добро пожаловать в Тренажёр словаря!",
        "choose_pair": "Выберите языковую пару (например, en-ru):",
        "menu": "\nМеню:\n1. Добавить слово\n2. Изменить слово\n3. Удалить слово\n4. Показать слова\n5. Начать викторину\n6. Выход",
        "prompt": "> ",
        "enter_english": "Введите английское слово:",
        "enter_translation": "Введите перевод(ы) через запятую:",
        "word_added": "Слово добавлено!",
        "word_exists": "Слово уже существует. Хотите изменить? (y/n): ",
        "word_not_found": "Слово не найдено.",
        "word_updated": "Слово обновлено!",
        "word_deleted": "Слово удалено!",
        "quiz_intro": "Начинаем викторину. Введите 'q' или 'e' для выхода.",
        "correct": "Правильно!",
        "incorrect": "Неправильно! Правильные ответы: ",
        "final_score": "Финальный счёт:",
        "no_words": "Пока нет добавленных слов.",
        "choose_action": "Выберите действие:",
        "goodbye": "До свидания!"
    }
    # Можно добавить другие языки здесь
}

language_choices = {
    "1": "en",
    "2": "ru",
    "3": "fr",
    "4": "es",
    "5": "kk",
    "6": "zh",
    "7": "ko",
    "8": "ja"
}

def t(key, lang):
    return interface_translations.get(lang, interface_translations["en"]).get(key, key)

def load_words(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_words(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    print("1. English\n2. Русский\n3. Français\n4. Español\n5. Қазақша\n6. 中文\n7. 한국어\n8. 日本語")
    lang_choice = input("Choose your interface language (1-8): ")
    lang = language_choices.get(lang_choice, "en")
    print(f"\n{t('welcome', lang)}")

    pair = input(f"{t('choose_pair', lang)} ").strip()
    filename = f"words_{pair}.json"
    words = load_words(filename)

    while True:
        print(t("menu", lang))
        choice = input(t("prompt", lang))

        if choice == "1":
            word = input(t("enter_english", lang)).strip().lower()
            if word in words:
                overwrite = input(t("word_exists", lang)).strip().lower()
                if overwrite != 'y':
                    continue
            translation = input(t("enter_translation", lang)).strip().lower()
            words[word] = translation
            save_words(filename, words)
            print(t("word_added", lang))

        elif choice == "2":
            word = input(t("enter_english", lang)).strip().lower()
            if word in words:
                translation = input(t("enter_translation", lang)).strip().lower()
                words[word] = translation
                save_words(filename, words)
                print(t("word_updated", lang))
            else:
                print(t("word_not_found", lang))

        elif choice == "3":
            word = input(t("enter_english", lang)).strip().lower()
            if word in words:
                del words[word]
                save_words(filename, words)
                print(t("word_deleted", lang))
            else:
                print(t("word_not_found", lang))

        elif choice == "4":
            if not words:
                print(t("no_words", lang))
            else:
                for word, translation in words.items():
                    print(f"{word} → {translation}")

        elif choice == "5":
            if not words:
                print(t("no_words", lang))
                continue

            print(t("quiz_intro", lang))
            score = 0
            total = 0
            quiz_words = list(words.items())
            random.shuffle(quiz_words)

            for word, translations in quiz_words:
                answer = input(f"{word} → ").strip().lower()
                if answer in ['q', 'e']:
                    break
                correct_answers = [x.strip().lower() for x in translations.split(',')]
                total += 1
                if answer in correct_answers:
                    print(t("correct", lang))
                    score += 1
                else:
                    print(f"{t('incorrect', lang)} {', '.join(correct_answers)}")

            print(f"{t('final_score', lang)} {score}/{total}")

        elif choice == "6":
            print(t("goodbye", lang))
            break

        else:
            print(t("choose_action", lang))

if __name__ == "__main__":
    main()

