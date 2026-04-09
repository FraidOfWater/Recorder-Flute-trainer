import random
notes = "C5 C#5 D5 D#5 E5 F5 F#5 G5 G#5 A5 A#5 B5 C6 C#6 D6 D#6 E6 F6 F#6 G6 G#6 A6 A#6 B6 C7 C#7 D7"
notes = notes.split(" ")

# E, F, G, A are the same with just the bottom hole partially held!
octaves_pairs = [("C5", "C6", "C7"), ("C#5", "C#6", "C#7"), ("D5", "D6", "D7"), ("D#5", "D#6"), ("E5", "E6"), ("F5", "F6"), ("F#5", "F#6"), ("G5", "G6"), ("G#5", "G#6"), ("A5", "A6"), ("A#5", "A#6"), ("B5", "B6")]
mode = None
while True:
    mode = input("Choose mode (number):\n1. First octave\n2. All notes\n3. Octave pairs\n4. All in order\n")
    if mode in ("1", "2", "3", "4"):
        break

notes = notes[:12] if mode == "1" else notes
i = 0
while True:
    if mode == "3":
        choice = list(random.choice(octaves_pairs))
        random.shuffle(choice)
        print(choice)
        input(" ")
    elif mode == "4":
        if i > len(notes)-1:
            i = 0 # looping back
        print(notes[i])
        i += 1
        input(" ")
    else:
        print(random.choice(notes))
        input(" ")
