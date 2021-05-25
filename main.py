from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Loads the correct questions and answers from BD data -> question_data to a list of objects called question_bank
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Instantiate a new object from QuizBrain class passing question_bank list
quiz_brain = QuizBrain(question_bank)

# While still has questions in BD call next_question method
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

# Print messages using the end_of_game_message method
quiz_brain.end_of_game_message()


