# 🧠 dictionary

Простое приложение для изучения английских слов. Работает в терминале. Позволяет добавлять слова, проходить викторину, просматривать и редактировать словарь.

A simple terminal-based vocabulary trainer for learning English. Allows adding words, taking quizzes, and editing your word list.

---

## 🚀 Возможности / Features

- Добавление слов и переводов (возможно несколько переводов через запятую).
- Прохождение викторины на основе сохранённых слов.
- Подсчёт результатов теста.
- Просмотр и удаление слов.
- Сохраняет данные в `words.json`.

Add words and multiple translations.  
Take a quiz to test your memory.  
View your word list and delete entries.  
All data saved in `words.json`.

---

## 📦 Установка / Installation

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/shaldybayev/dictionary.git
   cd dictionary
   ```

2. Запустите:
   ```bash
   python dictionary.py
   ```

---

## 🧪 Пример использования / Example usage

```
1. Add word
2. Quiz
3. View/edit words
4. Exit
Choice: 1
English word: send
Translation(s) (comma-separated): отправлять, посылать
✓ Word added!
```

---

## 🗂 Структура / Structure

- `dictionary.py` — основной код.
- `words.json` — словарь, автоматически создаётся и обновляется.

---

## 🛠 Требования / Requirements

- Python 3.6+

---

## 🌍 Планы / Plans

- Интерфейс на разных языках (English, Русский, Français, Español и др.)
- Анализ ошибок и сложных слов
- Поддержка обратного режима (перевод → слово)
- Возможность импорта/экспорта

---

## 📄 Лицензия / License

MIT

