DEFAULT_CORRECT_MESSAGE = "It's correct"
DEFAULT_WRONG_MESSAGE = "It's wrong"

DEFAULT_HELP_MESSAGE = "Never give up!"

TEXT_TYPE = 'text'


class Question:
    def __init__(self, question_unit, answer_unit, help_unit, finished=False):
        self.question = question_unit
        self.answer = answer_unit
        self.help = help_unit
        self.finished = finished

    def get_question(self):
        if self.question.type == TEXT_TYPE:
            return self.question.q_string
        else:
            raise ValueError

    def check_ans(self, answer):
        if self.answer.ans_string == answer:
            return True, self.question.correct_message
        else:
            return False, self.question.wrong_message

    def get_help(self):
        return self.help.help_string


class QuestionUnit:
    def __init__(self, type, **kwargs):
        self.type = type
        self.correct_message = kwargs.get('correct_message', DEFAULT_CORRECT_MESSAGE)
        self.wrong_message = kwargs.get('wrong_message', DEFAULT_WRONG_MESSAGE)
        self.q_string = None
        if type == TEXT_TYPE:
            self.q_string = kwargs['question']
        else:
            raise ValueError


class AnswerUnit:
    def __init__(self, type, **kwargs):
        self.type = type
        self.ans_string = None
        if type == TEXT_TYPE:
            self.ans_string = kwargs['answer']
        else:
            raise ValueError


class HelpUnit:
    def __init__(self, type, **kwargs):
        self.type = type
        self.help_string = None
        if type == TEXT_TYPE:
            self.help_string = kwargs.get('help', DEFAULT_HELP_MESSAGE)
        else:
            raise ValueError
