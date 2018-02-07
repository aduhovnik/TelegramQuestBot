from quest.question import Question, QuestionUnit, AnswerUnit, HelpUnit

questions = [
    Question(
        question_unit=QuestionUnit(type='text',
                                   question="Столица Хорвати?",
                                   correct_message="Верно",
                                   wrong_message="Нет, пробуй еще!"),
        answer_unit=AnswerUnit(type='text', answer="Загреб"),
        help_unit=HelpUnit(type='text',
                           help="Пфф, думай!")
    ),
]

finish_question = Question(
    question_unit=QuestionUnit(type='text', question="Квест пройден!"),
    answer_unit=AnswerUnit(type='text', answer="Квест пройден!"),
    help_unit=HelpUnit(type='text', help="Квест пройден!"),
    finished=True
)

info_str = "Телеграмм квест бот"

help_str = "Ты получишь подсказку только через 5 попыток!"
