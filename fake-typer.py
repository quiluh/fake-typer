import keyboard

file = open("connections-essay.txt","r").read().split()
index = 0

def keyPress(event):
    if event.name != "backspace":
        print(file[index])
        index += 1 if index < len(file) else 0
    else:
        index -= 1 if index > 0 else 0
keyboard.on_press(keyPress)
keyboard.wait("esc")