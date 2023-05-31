from win32gui import GetWindowText, GetForegroundWindow
from keyboard import is_pressed
from time import sleep


def check_exit() -> bool:
    try:
        if is_pressed("q"):
            return False
    except:
        print("Couldn't get keyboard input")
    return True


def mainloop():
    while check_exit():
        sleep(0.1)
        print(GetWindowText(GetForegroundWindow()))


def main():
    mainloop()


if __name__ == "__main__":
    main()
