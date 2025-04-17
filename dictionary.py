import json
import random
import os

FILENAME = "words.json"

def load_words():
    if not os.path.exists(FILENAME):
        return {}

    with open(FILENAME, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    converted = {}
    for word, translations in raw_data.items():
        if isinstance(translations, list):
            converted[word] = translations
        else:
            converted[word] = [translations]
    
    return converted

def save_words(words):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(words, f, indent=4, ensure_ascii=False)

def add_word(words):
    en = input("English word: ").strip()
    ru_input = input("Translation(s) (comma-separated): ").strip().lower()
    ru_list = [t.strip() for t in ru_input.split(',')]
    words[en] = ru_list
    save_words(words)
    print("✓ Word added!")

def quiz(words):
    if not words:
        print("No words to quiz yet.")
        return
    items = list(words.items())
    random.shuffle(items)
    score = 0
    for en, ru_list in items:
        ans = input(f"Translate '{en}': ").strip().lower()
        if ans in [t.lower() for t in ru_list]:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Incorrect. Possible answers: {', '.join(ru_list)}")
    print(f"\nYour score: {score}/{len(words)}")

def view_edit(words):
    if not words:
        print("No words added yet.")
        return
    
    print("\nYour word list:\n")
    for i, (en, ru_list) in enumerate(words.items(), 1):
        print(f"{i}. {en} → {', '.join(ru_list)}")

    print("\nType the number of the word to delete, or press Enter to return.")
    choice = input("Delete which word?: ").strip()
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(words):
            key_to_delete = list(words.keys())[idx]
            confirm = input(f"Delete '{key_to_delete}'? (y/n): ").strip().lower()
            if confirm == 'y':
                del words[key_to_delete]
                save_words(words)
                print("✓ Word deleted.")
        else:
            print("Invalid number.")
    elif choice:
        print("Invalid input.")
    else:
        print("Returning to menu...")

def main():
    words = load_words()
    while True:
        print("\n1. Add word\n2. Quiz\n3. View/edit words\n4. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            add_word(words)
        elif choice == "2":
            quiz(words)
        elif choice == "3":
            view_edit(words)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

