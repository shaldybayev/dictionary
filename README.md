
# 🧠 Dictionary App / Языковой Тренажёр

Multilingual terminal app for memorizing vocabulary, self-testing, and tracking your learning progress.  
Многоязычное консольное приложение для запоминания слов, самопроверки и отслеживания прогресса.

---

## 🌍 Features / Возможности

- Interface in multiple languages (English, Русский, Français, Español)
- Language pair selection (English → Russian, French, etc.)
- Add new vocabulary manually
- Case-insensitive and multi-answer checking
- Exit quiz anytime with `q`, `Q`, `e`, or `E`
- Tracks frequent mistakes
- Saves data in JSON format

---

## 🚀 Getting Started / Установка

### English

```bash
git clone https://github.com/shaldybayev/dictionary.git
cd dictionary
python3 dictionary.py
```

### Русский

```bash
git clone https://github.com/shaldybayev/dictionary.git
cd dictionary
python3 dictionary.py
```

---

## 🧪 Usage / Как использовать

1. Choose interface language / Выберите язык интерфейса.
2. Choose language pair / Выберите языковую пару.
3. Main menu / Главное меню:
   - `1` — Add new word / Добавить слово
   - `2` — Start quiz / Начать тест
   - `3` — Show all words / Показать все слова
   - `4` — Show mistakes / Показать ошибки
   - `5` — Exit / Выход

During the quiz, type `q`, `Q`, `e`, or `E` to exit.  
Во время теста введите `q`, `Q`, `e` или `E`, чтобы выйти.

---

## 🗂 File Structure / Структура файлов

- `dictionary.py` — Main app / Главная программа
- `words_*.json` — Vocabulary for each language pair / Словари
- `mistakes.json` — Mistakes tracker / Отслеживание ошибок

---

## 💡 Example / Пример

```
Word: send
Your answer: отправить
✅ Correct!
```

---

## 🛠 Planned Features / В планах

- [ ] Audio for words / Озвучка слов
- [ ] Flashcards with pictures / Карточки с изображениями
- [ ] Web version (Flask or React) / Веб-версия
- [ ] GUI (Tkinter) / Графический интерфейс

---

## 👤 Author / Автор

Created with ❤️ for language learners.  
Создано с любовью к изучению языков.

GitHub: [https://github.com/shaldybayev](https://github.com/shaldybayev)  

