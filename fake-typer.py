import keyboard

file = open("connections-essay.txt","r",encoding="utf-8").read()
currentProgress = []

def keyPress(event):
    global currentProgress
    if event.name != "backspace" and len(currentProgress) + 1 < len(file):
        keyboard.press_and_release("backspace")
        letter = file[len(currentProgress)]
        keyboard.press_and_release(letter)
        currentProgress.append(letter)
    else:
        if len(currentProgress) > 0:
            currentProgress = currentProgress[:-1]

keyboard.on_press(keyPress)
keyboard.wait("esc")

