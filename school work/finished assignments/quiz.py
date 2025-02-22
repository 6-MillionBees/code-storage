# Arden Boettcher
# 1/29/25
# Quiz Game

def get_int(text: str):
  while True:
    try:
      answer = int(input(text))
    except ValueError:
      continue
    else:
      break
  return answer


score = 0
questions = [
  {
    "question": "How many people got stuck inside Cannonball Loop in Action park?",
    "answer": 1
  },
  {
    "question": """What is Michel Lotito's favorite thing to drink while eating?
1: Olive Oil
2: Water
3: Mineral Oil
4: Orange Juice""",
    "answer": 3
  },
  {
    "question": "What year did Team Fortress 2 come out?",
    "answer": 2007
  },
  {
    "question": "What does the fox say?",
    "answer": "placeholder"
  },
  {
    "question": "What year was Tetris made?",
    "answer": 1984
  },
  {
    "question": "Did you like this quiz?\n1: Yes!!!\n2: no (I'm evil and mean)",
    "answer": 1
  }
]


for q in questions:
  print(q["question"])

  if q["question"] == "What does the fox say?":
    input("A: ")
    print("\nidk either\n")
    score += 1
    continue

  answer = get_int("A: ")


  if answer == q["answer"]:
    print("\nCorrect!\n")
    score += 1

  else:
    print("\nnuh uh\n")

if score == len(questions):
  print("Perfect Score!!")

elif score <= len(questions):
  print("F")

print(f"You got {score}/{len(questions)}")
