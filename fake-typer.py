import keyboard

file = [open("connections-essay.txt","r").read(),0]

def keyPress(event):
    if event.name != "backspace":
        keyboard.press_and_release(file[0][file[1]])
        file[1] += 1 if file[1] < len(file[0]) else 0
    else:
        file[1] -= 1 if file[1] > 0 else 0

keyboard.on_press(keyPress)
keyboard.wait("esc")
