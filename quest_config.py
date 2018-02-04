from quest.question import Question, QuestionUnit, AnswerUnit, HelpUnit

questions = [
    Question(
        question_unit=QuestionUnit(type='text',
                                   question="10+10",
                                   correct_message="Nice! Let's go to the next question.",
                                   wrong_message="Oh, common, try again!"),
        answer_unit=AnswerUnit(type='text', answer="20"),
        help_unit=HelpUnit(type='text',
                           help="Oh, common, this is so easy.")
    ),
]

finish_question = Question(
    question_unit=QuestionUnit(type='text', question="That's all! See you later"),
    answer_unit=AnswerUnit(type='text', answer="That's all! See you later"),
    help_unit=HelpUnit(type='text', help="That's all! See you later"),
    finished=True
)

info_str = "This is quest bot"

help_str = "You can get help only after 5 unsuccessful tries."
