from commands_handler.simple_track import TrackMixin


class Commands_Handler(TrackMixin):
    def __init__(self, update, bot, quest):
        self.bot = bot
        self.quest = quest
        self.update = update

        self.commands_handler = {
            '/info': self._quest_info,
            '/question': self._quest_get_question,
            '/guess': self._quest_guess,
            '/start_new': self._quest_restart,
            '/help': self._quest_help,
            '/q': self._quest_guess
        }

    def process_update(self, update):
        self.track_message(update.message)
        command, args = self._get_command(update)

        if self._quest_check_start():
            self.process_command(command, args)

    def process_command(self, command, args):
        self.commands_handler.get(command, self._quest_guess)(args + [command])

    def _get_command(self, update):
        try:
            args = update.message['text'].split(' ')
        except:
            args = ['']
        command, args = args[0], args[1:]
        return command, args

    def _quest_info(self, args):
        info = self.quest.get_info()
        self.bot.sendMessage(chat_id=self.update.message.chat_id, text=info)

    def _quest_get_question(self, args):
        chat_id = self.update.effective_chat['id']
        ret = self.quest.get_question(chat_id)
        self.bot.sendMessage(chat_id=self.update.message.chat_id, text=ret)

    def _quest_restart(self, args):
        chat_id = self.update.effective_chat['id']
        self.quest.start_new_game(chat_id)

    def _quest_help(self, args):
        chat_id = self.update.effective_chat['id']
        ret = self.quest.get_help(chat_id)
        self.bot.sendMessage(chat_id=self.update.message.chat_id, text=ret)

    def _quest_guess(self, args):
        answer = args[0] if args else None
        chat_id = self.update.effective_chat['id']
        ret = self.quest.try_guess(chat_id, answer)
        self.bot.sendMessage(chat_id=self.update.message.chat_id, text=ret)

    def _default_handler(self, args):
        self.bot.sendMessage(chat_id=self.update.message.chat_id, text='< 3')

    def _quest_check_start(self):
        ret, message = self.quest.is_started()
        if not ret:
            self.bot.sendMessage(chat_id=self.update.message.chat_id, text=message)
        return ret
