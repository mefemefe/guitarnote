#Take a string and a fret number and return the note.
def what_note(string, fret):
    scale = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
    return scale[(scale.index(string.upper())+fret)%len(scale)]

print("Enter the letter representing the string (A,A#,B,C,C#,D,D#,E,F,F#,G,G#)")
st = input("String:")
print("Enter the fret number")
try:
    fr = int(input("Fret:"))
except:
    print("That's not a number")
    quit()

print("\n"+what_note(st,fr))