from quest.question import Question, QuestionUnit, AnswerUnit, HelpUnit

questions = [
    Question(
        question_unit=QuestionUnit(type='text',
                                   question="Столица Хорвати?",
                                   correct_message="Ой ты моя умничка)) Угадала!",
                                   wrong_message="Нет, пробуй еще!"),
        answer_unit=AnswerUnit(type='text', answer="Загреб"),
        help_unit=HelpUnit(type='text',
                           help="Пфф, думай!")
    ),
    Question(
        question_unit=QuestionUnit(type='text',
                                   question="Что бросают тогда, когда это необходимо, и поднимают тогда, \
                                             когда это уже не нужно?",
                                   correct_message="Ой ты моя умничка)) Угадала!",
                                   wrong_message="Нет, не сдавайся!"),
        answer_unit=AnswerUnit(type='text', answer="Якорь"),
        help_unit=HelpUnit(type='text',
                           help="Морская тематика")
    ),
    Question(
        question_unit=QuestionUnit(type='text',
                                   question="Фамилия главной героини из фильма 'Три билборда на границе Эббинга'?",
                                   correct_message="Ой ты моя умничка)) Угадала!",
                                   wrong_message="Пробуй еще, может обратиться к подсказкам?"),
        answer_unit=AnswerUnit(type='text', answer="Хейс"),
        help_unit=HelpUnit(type='text',
                           help="Сложно, согласен. Имя дочери было Анжела, Анжела ..йс")
    ),
    Question(
        question_unit=QuestionUnit(type='text',
                                   question="Сколько дней в 2020 году?",
                                   correct_message="Ой ты моя умничка)) Угадала!",
                                   wrong_message="Легкий вопрос ведь))"),
        answer_unit=AnswerUnit(type='text', answer="366"),
        help_unit=HelpUnit(type='text',
                           help="Високосный)")
    ),

    Question(
        question_unit=QuestionUnit(type='text',
                                   question="Сколько кг весит михал?",
                                   correct_message="Ой ты моя умничка)) Угадала!",
                                   wrong_message="Нет, гадай)"),
        answer_unit=AnswerUnit(type='text', answer="90"),
        help_unit=HelpUnit(type='text',
                           help="Меньше 100, но больше 80")
    ),
]

finish_question = Question(
    question_unit=QuestionUnit(type='text', question="Все, ты прошла квест! Поздравляю, жди 14 февраля!"),
    answer_unit=AnswerUnit(type='text', answer="Все, ты прошла квест! Поздравляю, жди 14 февраля!"),
    help_unit=HelpUnit(type='text', help="Все, ты прошла квест! Поздравляю, жди 14 февраля!"),
    finished=True
)

info_str = "Это демо квестового бота для моей Лизы)"

help_str = "Ты получишь подсказку только через 5 попыток)"
