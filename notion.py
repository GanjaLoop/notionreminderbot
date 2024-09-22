import logging
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
from database import Note, session

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ваш токен от BotFather
TOKEN = 'YOUR_TOKEN'

# Определение состояния для ConversationHandler
NEW_NOTE = 1

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Привет! Я ваш личный помощник.\n'
        'Используйте /newnote для создания заметки.\n'
        'Используйте /listnotes для просмотра всех заметок.'
    )

def new_note_start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Пожалуйста, введите текст новой заметки.')
    return NEW_NOTE

def save_new_note(update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id
    text = update.message.text
    new_note = Note(user_id=user_id, text=text)
    session.add(new_note)
    session.commit()
    update.message.reply_text(f'Заметка сохранена: {text}')
    return ConversationHandler.END

def list_notes(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    notes = session.query(Note).filter_by(user_id=user_id).all()
    if notes:
        message = "Ваши заметки:\n"
        for note in notes:
            message += f"{note.id}. {note.text}\n"
    else:
        message = "У вас нет сохранённых заметок."
    update.message.reply_text(message)

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Действие отменено.')
    return ConversationHandler.END

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Обработчик команды /start
    dispatcher.add_handler(CommandHandler('start', start))

    # Обработчик команды /listnotes
    dispatcher.add_handler(CommandHandler('listnotes', list_notes))

    # Обработчик ConversationHandler для создания новой заметки
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('newnote', new_note_start)],
        states={
            NEW_NOTE: [MessageHandler(Filters.text & ~Filters.command, save_new_note)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()