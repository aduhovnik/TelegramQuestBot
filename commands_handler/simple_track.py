from models.models import TlgMessage, TlgUser, TlgChat


class TrackMixin:
    def get_user_id(self, _user):
        if not _user:
            return None

        user = TlgUser.get_by_criteria(id=_user['id'])
        if not user:
            user_dict = {
                'id': _user['id'],
                'first_name': _user['first_name'],
                'second_name': _user['last_name'],
                'lang_code': _user['language_code'],
                'user_name': _user['username'],
                'is_bot': _user['is_bot']
            }
            user = TlgUser(**user_dict).save()
        return user.id

    def get_chat_id(self, _chat):
        if not _chat:
            return None

        chat = TlgChat.get_by_criteria(id=_chat['id'])
        if not chat:
            chat_dict = {
                'id': _chat['id'],
                'title': _chat['title'],
                'chat_type': _chat['type'],
                'first_name': _chat['first_name'],
                'second_name': _chat['last_name'],
                'user_name': _chat['username'],
                'invite_link': _chat['invite_link'],
                'is_all_members_admins': _chat['all_members_are_administrators'],
            }
            chat = TlgChat(**chat_dict).save()
        return chat.id

    def track_message(self, message):
        message_dict = {
            'id': message['message_id'],
            'from_user_id': self.get_user_id(message['from_user']),
            'date': message['date'],
            'chat_id': self.get_chat_id(message['chat']),
            'forward_from_id': self.get_user_id(message['forward_from']),
            'forward_from_chat_id': self.get_chat_id(message['forward_from_chat']),
            'reply_to_message_id': message['reply_to_message_id'],
            'forward_date': message['forward_date'],
            'text': message['text'],
        }
        _message = TlgMessage.get_by_criteria(id=message['message_id'])
        if _message is None:
            _message = TlgMessage(**message_dict).save()
        return _message.id
