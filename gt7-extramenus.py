import time
import pyautogui


def press(key: str) -> None:
    """Press a key.
    Using vanilla `pyautogui.press()` will not register the keystroke
    because GT requires you hold a keypress for a small duration."""

    with pyautogui.hold(key):
        time.sleep(0.2)
    time.sleep(0.3)


def hold(key: str, duration: float) -> None:
    """Hold a key for some duration."""

    with pyautogui.hold(key):
        time.sleep(duration)


def focus_window():
    """Focus the window by clicking on the center of the primary screen."""
    # Click center of screen to focus remote play window.
    # You can reposition and resize remote play window, just
    # make sure you update where you click. I don't know how to
    # use pyautogui in headless mode.

    width, height = pyautogui.size()
    center = width / 2, height / 2
    pyautogui.moveTo(center)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)


def start_exploit(section):
    print(" [-] Entering Cafe.")
    press("enter")
    time.sleep(3)
    press("left")
    press("enter")
    press("down")
    press("right")
    press("enter")
    press("up")

    if section == "ROTARY":
        press("right")
        press("right")

        # Inside Rotary Engine

    press("enter")
    press("enter")
    time.sleep(3)
    press("escape")
    press("escape")
    press("escape")
    time.sleep(4)

    # Back to map to open ticket
    press("right")
    press("enter")
    time.sleep(4)
    press("right")
    press("right")
    press("right")
    press("enter")
    press("enter")
    press("enter")
    print(" [-] Opening ticket.")
    time.sleep(16)

    # Accepting any kind of ticket, avoids using image detection
    press("enter")
    time.sleep(10)
    press("enter")
    time.sleep(4)
    press("enter")
    press("enter")

    print(" [-] Accepting ticket.")
    press("enter")  # accept ticket

    # Back out of tickets
    print(" [-] Going back to map.")
    press("escape")
    press("escape")
    time.sleep(3)
    press("left")  # Place cursor on Menu to start over


if __name__ == "__main__":
    cycles = 0
    focus_window()
    while True:
        start_exploit("")
        start_exploit("ROTARY")
        cycles += 1
        print(" [+] Cycles completed: " + str(cycles))
