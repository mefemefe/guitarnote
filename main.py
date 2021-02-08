#Take a string and a fret number and return the note.
def what_note(string, fret):
    scale = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
    while fret >= 12:
        fret -= 12
    result = scale.index(string.upper()) + fret
    while result >= 12:
        result -= 12
    return scale[result]

print("Enter the letter representing the string (A,A#,B,C,C#,D,D#,E,F,F#,G,G#)")
st = input("String:")
print("Enter the fret number")
try:
    fr = int(input("Fret:"))
except:
    print("That's not a number")
    quit()

print("\n"+what_note(st,fr))