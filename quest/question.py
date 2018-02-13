DEFAULT_CORRECT_MESSAGE = "It's correct"
DEFAULT_WRONG_MESSAGE = "It's wrong"

DEFAULT_HELP_MESSAGE = "Never give up!"

TEXT_TYPE = 'text'
ONE_FROM_LIST_TYPE = 'one_from_list'


class Question:
    def __init__(self, question_unit, answer_unit, help_unit, finished=False):
        self.question = question_unit
        self.answer = answer_unit
        self.help = help_unit
        self.finished = finished

    def get_question(self):
        return self.question.get_question()

    def check_ans(self, answer):
        ret = self.answer.check_ans(answer)
        message = self.question.correct_message if ret \
            else self.question.wrong_message
        return ret, message

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

    def get_question(self):
        if self.type == TEXT_TYPE:
            return self.q_string
        else:
            raise ValueError


class AnswerUnit:
    def __init__(self, type, **kwargs):
        self.type = type
        self.ans_string = None
        self.ans_set = ()
        if type == TEXT_TYPE:
            self.ans_string = kwargs['answer']
        elif type == ONE_FROM_LIST_TYPE:
            self.ans_set = list(map(str.lower, kwargs['answers']))
        else:
            raise ValueError

    def check_ans(self, answer):
        if self.type == 'text':
            if self.ans_string.lower() == answer.lower():
                return True
            else:
                return False

        elif self.type == ONE_FROM_LIST_TYPE:
            if answer.lower() in self.ans_set:
                return True
            else:
                return False

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
