import arrow

from quest.quest import Quest
from quest.question import Question, QuestionUnit, AnswerUnit, HelpUnit

questions = [
    Question(
        QuestionUnit(type='text',
                     question="Столица Хорвати?",
                     correct_message="Верно",
                     wrong_message="Нет, пробуй еще!"),
        AnswerUnit(type='text', answer="Загреб"),
        HelpUnit(type='text', help="Пфф, думай!")
    ),
]

final_question = Question(
    question_unit=QuestionUnit(type='text', question="Квест пройден!"),
    answer_unit=AnswerUnit(type='text', answer="Квест пройден!"),
    help_unit=HelpUnit(type='text', help="Квест пройден!"),
    finished=True
)

info_str = "Телеграмм квест бот"

help_str = "Ты получишь подсказку только через пару попыток!"

start_datetime = arrow.get('2018-02-13T19:00:00.000-00:00')
waiting_message = 'Квест начнется через %s ч, %s мин! Ожидайте!'

quest = Quest(questions, info_str, help_str, final_question,
              start_datetime, waiting_message)
