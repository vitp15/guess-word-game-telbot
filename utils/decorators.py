def group(bot):
    def decorator(func):
        def wrapper(message):
            chat_type = message.chat.type
            if chat_type == 'group' or chat_type == 'supergroup':
                func(message)
            else:
                bot.reply_to(message, 'This command can only be used in groups, use /help for details about this bot')
        return wrapper
    return decorator
