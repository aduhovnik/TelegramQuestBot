from commands_handler.simple_track import TrackMixin


class Commands_Handler(TrackMixin):
    def __init__(self, update, bot):
        self.bot = bot
        self.commands_handler = {
        }

        self.update = update

    def process_update(self, update):
        command, args = self._get_command(update)
        self.process_command(command, args)
        self.track_message(update.message)

    def process_command(self, command, args):
        chat_id = self.update.effective_chat['id']
        bot_id = self.bot.id

        self.commands_handler.get(command, self.default_handler)()

    def default_handler(self):
        self.bot.sendMessage(chat_id=self.update.message.chat_id, text='< 3')

    def _get_command(self, update):
        try:
            args = update.message['text'].split(' ')
        except:
            args = ['']
        command, args = args[0], args[1:]
        return command, args
