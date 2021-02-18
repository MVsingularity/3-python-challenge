import json

with open('me-capitals.json', 'r') as f:
    data = json.load(f)

total = len(data["cards"])
score = 0

for i in data["cards"]:
    guess = input(i["q"] + ">")

    if guess.lower() == i["a"].lower():
            score +=1
            print(f"correct! Current score: {score}/{total}")

    else:
        print("incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")
