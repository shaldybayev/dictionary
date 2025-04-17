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

MIT License

Copyright (c) 2025 shaldybayev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
THE SOFTWARE.


