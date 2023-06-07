from quiz_questions import Question

question_prompts = [
"what color are apples? \n a) red/green\n b) purple\n c) orange\n\n",
"what color are bananas? \n a) red/green\n b) purple\n c) yellow\n\n",
"what color are strawberries? \n a) red\n b) purple\n c) orange\n\na"

]

question = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(question)

