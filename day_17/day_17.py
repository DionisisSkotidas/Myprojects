class Question:

    def __init__(self, question, answer):
        self.text = question
        self.answer = answer


class QuizBrain:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            self.quiz_completed()
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f" Q. {self.question_number + 1} : {current_question.text} (True or False) : ").lower()
        self.check_answer(user_answer, current_question.answer)
        print()
        self.question_number += 1

    def check_answer(self, given_answer, correct_answer):
        if given_answer.lower() == correct_answer.lower():
            self.score += 1
            print('Correct')
        else:
            print(f'Sorry bro the correct answer was {correct_answer}')
        print(f'Your current score is {self.score}/{self.question_number + 1}')

    def quiz_completed(self):
        print("You've completed the quiz")
        print(f"Your score was {self.score}/{len(self.question_list)}")


question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
             " you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can  kill a small dog.", "answer": "True"}
]

question_bank = []
for dictionary in question_data:
    question_text = dictionary['text']
    question_ans = dictionary['answer']
    question_bank.append(Question(question_text, question_ans))

px = QuizBrain(question_bank)
while px.still_has_question():
    px.next_question()