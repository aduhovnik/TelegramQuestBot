import arrow
from sqlalchemy import desc

from models.db_settings import db_session
from models.models import QuestionsProgres

TRIES_BEFORE_HELP = 5


class Quest:
    def __init__(self, _questions, info_str, help_str, final_question,
                 start_datetime, waiting_message):
        self.questions = _questions
        self.info_str = info_str
        self.default_help = help_str
        self.start_datetime = start_datetime
        self.waiting_message = waiting_message

        self.finish_question = final_question

    def try_guess(self, chat_id, answer):
        _question = self._get_current_question(chat_id)
        question = self._get_question_by_number(_question.question_number)
        ret, message = question.check_ans(answer)
        if ret:
            _question.update(passed=True, tries=_question.tries + 1)
            QuestionsProgres(question_number=_question.question_number + 1, passed=False,
                             tries=0, chat_id=chat_id).save()
        else:
            _question.update(tries=_question.tries + 1)
        return message

    def get_help(self, chat_id):
        _question = self._get_current_question(chat_id)
        if _question.tries < TRIES_BEFORE_HELP:
            help = self.default_help
        else:
            question = self._get_question_by_number(_question.question_number)
            help = question.get_help()
        return help

    def start_new_game(self, chat_id):
        for q in db_session.query(QuestionsProgres).filter(QuestionsProgres.chat_id == chat_id):
            db_session.delete(q)
        db_session.commit()

    def get_info(self):
        return self.info_str

    def get_question(self, chat_id):
        _question = self._get_current_question(chat_id)
        question = self._get_question_by_number(_question.question_number)
        return question.get_question()

    def _get_question_by_number(self, question_number):
        if question_number >= len(self.questions):
            return self.finish_question
        else:
            return self.questions[question_number]

    def _get_current_question(self, chat_id):
        question = db_session.query(QuestionsProgres) \
            .filter(QuestionsProgres.chat_id == chat_id) \
            .order_by(desc(QuestionsProgres.question_number)).first()
        if not question:
            question = QuestionsProgres(question_number=0, passed=False, tries=0, chat_id=chat_id).save()
        return question

    def _get_waiting_message(self, timedelta):
        secs = timedelta.total_seconds()
        hours = int(secs // 3600)
        secs -= hours * 3600
        minutes = int(secs // 60)
        return self.waiting_message % (hours, minutes)

    def is_started(self):
        _now = arrow.utcnow()
        if _now < self.start_datetime:
            message = self._get_waiting_message(self.start_datetime - _now)
            return False, message
        return True, ''
