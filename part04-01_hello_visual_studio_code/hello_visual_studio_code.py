# Write your solution here
while True:
    editor = input("Editor:")
    bad_editor = "word, notepad"
    right = "Visual Studio Code"
    
    if editor.lower() == "visual studio code":
        print("an excellent choice!")
        break
    elif editor.lower() in bad_editor:
        print("awful")
    else:
        print("not good")