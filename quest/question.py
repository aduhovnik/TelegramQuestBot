class Question:
    def __init__(self, question_unit, answer_unit, help_unit, finished=False):
        self.question = question_unit
        self.answer = answer_unit
        self.help = help_unit
        self.finished = finished

    def get_question(self):
        return self.question.q_string

    def check_ans(self, answer):
        if self.answer.ans_string == answer:
            return True, "It's correct"
        else:
            return False, "It's wrong"


class QuestionUnit:
    def __init__(self, type, **kwargs):
        self.type = type
        self.q_string = None
        if type == 'text':
            self.q_string = kwargs['question']
        else:
            raise ValueError


class AnswerUnit:
    def __init__(self, type, **kwargs):
        self.type = type
        self.ans_string = None
        if type == 'text':
            self.ans_string = kwargs['answer']
        else:
            raise ValueError


class HelpUnit:
    def __init__(self, type, **kwargs):
        self.type = type
        self.help_string = None
        if type == 'text':
            self.help_string = kwargs['help']
        else:
            raise ValueError
