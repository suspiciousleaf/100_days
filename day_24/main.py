# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("day_24/Input/Letters/starting_letter.txt", "r") as infile:
    letter_raw = infile.read()


with open("day_24/Input/Names/invited_names.txt", "r") as infile:
    names = infile.read().splitlines()

for name in names:
    new_letter = letter_raw.replace("[name]", name)
    with open(f"day_24/Output/ReadyToSend/letter_for_{name}.txt", "w") as outfile:
        outfile.write(new_letter)
