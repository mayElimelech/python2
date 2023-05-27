import winsound

freqs = {
    "la": 220,
    "si": 247,
    "do": 261,
    "re": 293,
    "mi": 329,
    "fa": 349,
    "sol": 392,
}

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

# Split the notes by hyphen
note_list = notes.split("-")

# Iterate over the notes and play each one
for note in note_list:
    note_info = note.split(",")
    frequency = freqs[note_info[0]]
    duration = int(note_info[1])
    winsound.Beep(frequency, duration)


numbers = iter(list(range(1, 102)))

for i in numbers:
    print(i)
    for j in range(2):
        try:
            next(numbers)
        except StopIteration:
            break


import itertools
money_type = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
count= 0
for i in range(5, 20):
    hundred = set(itertools.combinations(money_type, i))
    for item in hundred:
        if sum(item) == 100:
            print(item)
            count += 1
print("these are the number of ways " + str(count) )

class MusicNotes:
    def __init__(self):
        self.notes = {
            "la": [55, 110, 220, 440, 880],
            "si": [61.74, 123.48, 246.96, 493.92, 987.84],
            "do": [65.41, 130.82, 261.64, 523.28, 1046.56],
            "re": [73.42, 146.84, 293.68, 587.36, 1174.72],
            "mi": [82.41, 164.82, 329.64, 659.28, 1318.56],
            "fa": [87.31, 174.62, 349.24, 698.48, 1396.96],
            "sol": [98, 196, 392, 784, 1568]
        }
        self.octave = 0
        self.note_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.octave >= len(self.notes["la"]):
            raise StopIteration
        frequency = self.notes[list(self.notes.keys())[self.note_index]][self.octave]
        self.note_index = (self.note_index + 1) % len(self.notes)
        if self.note_index == 0:
            self.octave += 1
        return frequency

# Usage
iter1 = iter(MusicNotes())
for freq in iter1:
    print(freq)


class IDIterator:
    def __init__(self, id_):
        self.id_ = id_

    def __iter__(self):
        return self

    def __next__(self):
        if self.id_ >= 999999999:
            raise StopIteration
        self.id_ += 1
        while not check_id_valid(self.id_):
            self.id_ += 1
        return self.id_


def check_id_valid(id_number):
    digits = [int(digit) for digit in str(id_number)]
    multiplied_digits = [digit * (2 if index % 2 != 0 else 1) for index, digit in enumerate(digits)]
    summed_digits = [digit if digit <= 9 else digit - 9 for digit in multiplied_digits]
    total_sum = sum(summed_digits)
    return total_sum % 10 == 0



def main():
    print(check_id_valid(123456782))
    id_number = int(input("Enter ID: "))

    generator_type = input("Generator or Iterator? (gen/it)? ")

    if generator_type == "it":
            iterator = IDIterator(id_number)
            id_numbers = [next(iterator) for j in range(10)]
    elif generator_type == "gen":
            id_numbers = [id for id in id_generator(id_number, 10)]
    else:
            print("Invalid input")

    for id in id_numbers:
            print(id)



def id_generator(id_number, count):
    while count > 0 and id_number < 999999999:
        id_number += 1
        while not check_id_valid(id_number):
            id_number += 1
        yield id_number
        count -= 1


if __name__ == "__main__":
    main()
