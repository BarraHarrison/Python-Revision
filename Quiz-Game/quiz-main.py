questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in the Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: ",
    "What is the capital of France?: ",
    "What is the smallest prime number?: ",
    "Who wrote 'To Kill a Mockingbird'?: ",
    "What is the chemical symbol for water?: ",
    "What is the largest mammal on Earth?: ",
    "What is the square root of 144?: ",
    "Which ocean is the largest?: ",
    "Who painted the Mona Lisa?: ",
    "What is the speed of light in a vacuum?: ",
    "Which country is known as the Land of the Rising Sun?: ",
    "What is the currency of Japan?: ",
    "Who is known as the father of computers?: ",
    "Which planet is known as the Red Planet?: ",
    "What is the chemical symbol for gold?: ",
    "How many continents are there?: ",
    "What is the largest desert in the world?: ",
    "What is the main ingredient in guacamole?: ",
    "Who discovered penicillin?: ",
    "What is the powerhouse of the cell?: ",
    "What is the freezing point of water in Celsius?: ",
    "Which is the longest river in the world?: ",
    "What is the capital of Italy?: ",
    "What is the heaviest naturally occurring element?: ",
    "Who wrote 'Pride and Prejudice'?: ",
    "Which gas do plants absorb for photosynthesis?: "
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
    ("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"),
    ("A. 0", "B. 1", "C. 2", "D. 3"),
    ("A. Harper Lee", "B. J.K. Rowling", "C. Jane Austen", "D. Mark Twain"),
    ("A. HO", "B. O2", "C. H2O", "D. OH"),
    ("A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Orca"),
    ("A. 12", "B. 14", "C. 16", "D. 10"),
    ("A. Atlantic", "B. Pacific", "C. Indian", "D. Arctic"),
    ("A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Claude Monet"),
    ("A. 3x10^7 m/s", "B. 3x10^8 m/s", "C. 3x10^9 m/s", "D. 3x10^10 m/s"),
    ("A. China", "B. Japan", "C. India", "D. Korea"),
    ("A. Dollar", "B. Yen", "C. Euro", "D. Pound"),
    ("A. Alan Turing", "B. Charles Babbage", "C. Ada Lovelace", "D. George Boole"),
    ("A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"),
    ("A. Au", "B. Ag", "C. Gd", "D. Fe"),
    ("A. 5", "B. 6", "C. 7", "D. 8"),
    ("A. Sahara", "B. Arctic", "C. Gobi", "D. Kalahari"),
    ("A. Tomato", "B. Avocado", "C. Potato", "D. Onion"),
    ("A. Marie Curie", "B. Alexander Fleming", "C. Louis Pasteur", "D. Robert Koch"),
    ("A. Nucleus", "B. Ribosome", "C. Mitochondria", "D. Cytoplasm"),
    ("A. 100", "B. 0", "C. -100", "D. -273"),
    ("A. Nile", "B. Amazon", "C. Yangtze", "D. Ganges"),
    ("A. Venice", "B. Rome", "C. Milan", "D. Florence"),
    ("A. Uranium", "B. Plutonium", "C. Lead", "D. Osmium"),
    ("A. Emily Bronte", "B. Harper Lee", "C. Jane Austen", "D. George Eliot"),
    ("A. Oxygen", "B. Carbon-Dioxide", "C. Nitrogen", "D. Methane")
)

answers = (
    "C", "D", "A", "A", "B",  # First 5 questions
    "C", "C", "A", "C", "B",  # Next 5
    "A", "B", "B", "B", "B",  # Next 5
    "B", "B", "B", "A", "B",  # Next 5
    "A", "B", "B", "C", "A",  # Next 5
    "B", "A", "C", "C", "B"   # Last 5
)

guesses = []
score = 0
question_number = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_number]} is the correct answer.")
    question_number += 1

print("--------------------")
print("------RESULTS-------")
print("--------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

# Calculating the number of correct answers
total_questions = len(questions)
incorrect = total_questions - score

print(f"\nYou got {score} out of {total_questions} questions correct!")
print(f"You got {incorrect} question(s) wrong.")

# Calculate and display the percentage
percentage = (score / total_questions) * 100
print(f"Your score: {percentage:.2f}%")
