class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0  

    def next_question(self):
        if self.still_has_questions():
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"{current_question.text} (True/False): ")
            self.check_answer(user_answer, current_question.answer.lower(),
                              current_question)
        else:
          print("Thank you for taking the quiz! Your final score is:", self.score)


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer, current_question):
        if user_answer.lower() == current_question.answer.lower():
            print("You got it right!")
            self.score += 1  

        else:
            print("Sorry, that's wrong.")

        self.next_question()  # Move to the next question
