from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# write a loop to iterate over the question_data. Create a Question object 
# for each item in the question_data. Append each Question object to the question_bank 

#class Question:
#
 #   def __init__(self,q_text,q_answer):
  #      self.text=q_text
   #     self.answer=q_answer


question_bank=[]

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text, question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question() 
    
    


#print(question_bank)    
#quiz.next_question()




question_bank=[]
for questions in question_data:
    question_text=question["text"] 
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer) 
    question_bank.append(new_question) 





    