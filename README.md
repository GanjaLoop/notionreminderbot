RUS

# Телеграм-бот для заметок (Beta)

Внимание: бот находится на ранней стадии разработки. Функциональность может быть ограничена и содержать ошибки.

## Описание

Это простой телеграм-бот для создания и просмотра заметок. Бот позволяет пользователям создавать новые заметки и просматривать список всех своих заметок непосредственно в мессенджере Telegram.

## Основные функции

- Создание новой заметки: используйте команду /newnote, чтобы добавить новую заметку.
- Просмотр всех заметок: команда /listnotes выводит список всех ваших заметок.

## Инструкция по запуску

1. Клонируйте репозиторий:

   
   git clone https://github.com/ваш_логин/telegram-notetaking-bot.git
   

2. Перейдите в директорию проекта:

   
   cd telegram-notetaking-bot
   

3. Установите необходимые зависимости:

   
   pip install -r requirements.txt
   

4. Создайте файл config.py:

   Скопируйте config.example.py и переименуйте его в config.py. Внутри файла замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего телеграм-бота.

5. Запустите бота:

   
   python notion.py
   

6. Используйте бота в Telegram:

   - Найдите вашего бота по имени в приложении Telegram.
   - Отправьте команду /start для начала работы.

## Требования

- Python 3.x
- Библиотеки из requirements.txt

---

ENG

# Telegram Notetaking Bot (Beta)

Note: This bot is in early development. Functionality may be limited and may contain bugs.

## Description

This is a simple Telegram bot for creating and viewing notes. The bot allows users to create new notes and view a list of all their notes directly within the Telegram messenger.

## Main Features

- Create a new note: Use the /newnote command to add a new note.
- View all notes: The /listnotes command displays all your notes.

## How to Run

1. Clone the repository:

   
   git clone https://github.com/your_username/telegram-notetaking-bot.git
   

2. Navigate to the project directory:

   
   cd telegram-notetaking-bot
   

3. Install the required dependencies:

   
   pip install -r requirements.txt
   

4. Create a config.py file:

   Copy config.example.py and rename it to config.py. Inside the file, replace 'YOUR_TELEGRAM_BOT_TOKEN' with your Telegram bot token.

5. Run the bot:

   
   python notion.py
   

6. Use the bot in Telegram:

   - Find your bot by its username in the Telegram app.
   - Send the /start command to begin.

## Requirements

- Python 3.x
- Libraries listed in requirements.txt
