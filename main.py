import pandas

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# Looping through dictionaries:
for key, value in student_dict.items():
    # Access key and value
    print(key)
    print(value)
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    print(row.student)
    print(row.score)
    pass

# Loop through rows of a data frame
for index, row in student_data_frame.iterrows():
    if row.student == "Angela":
        print(f"test row.score: {row.score}")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv(
    "/Users/mei/projects/python_practice_nato_alphabet/nato_phonetic_alphabet.csv"
)
print(data)
print(data.to_dict())


# use dictionary comprehension to get it to be the format we want
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def check_word_input():
    try:
        boolean = True

        word = input("Enter a word?").upper()
        if not word.isalpha():
            raise ValueError("Please enter alphabet word")

    except ValueError as e:
        print(e)
        check_word_input()
    else:
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)


check_word_input()
