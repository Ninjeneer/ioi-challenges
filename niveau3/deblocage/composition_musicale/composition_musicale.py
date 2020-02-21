notes = input()

index = 0
while index < len(notes) - 1:
    if notes[index] == notes[index + 1]:
        notes = notes[0:index] + notes[index + 2:]
        index = 0
    else:
        index += 1

print(notes)
