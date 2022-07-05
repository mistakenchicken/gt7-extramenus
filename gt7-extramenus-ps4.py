import time
import argparse
import pyautogui

DEFAULT_DELAY = 0.2
STARTUP_DELAY = 5


def parse_args():
    """Parse arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--delay",
        type=float,
        required=False,
        nargs="?",
        const=DEFAULT_DELAY,
        default=DEFAULT_DELAY,
        help="default = 0.2 - Value must be >= 0.2",
    )
    parser.add_argument(
        "--auto",
        action="store_true",
        help="automatically captures window on primary monitor",
    )
    args = parser.parse_args()
    if args.delay < DEFAULT_DELAY:
        print("--delay values below 0.2 may break the script. Try another value")
        exit()
    return args


def press(key: str) -> None:
    """Press a key.
    Using vanilla `pyautogui.press()` will not register the keystroke
    because GT requires you hold a keypress for a small duration."""
    delay = parse_args().delay

    with pyautogui.hold(key):
        time.sleep(0.2)
    time.sleep(delay)  # delay after any press


def hold(key: str, duration: float) -> None:
    """Hold a key for some duration."""

    with pyautogui.hold(key):
        time.sleep(duration)


def sleep(seconds: float):
    delay = parse_args().delay
    time.sleep(seconds - delay + DEFAULT_DELAY)


def focus_window(auto):
    """Focus the window by clicking on the center of the primary screen."""
    # Click center of screen to focus remote play window.
    # You can reposition and resize remote play window, just
    # make sure you update where you click. I don't know how to
    # use pyautogui in headless mode.

    if auto:
        print("Using auto mode")
        width, height = pyautogui.size()
        center = width / 2, height / 2
        pyautogui.moveTo(center)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
    else:
        print(
            "Using startup delay of "
            + str(STARTUP_DELAY)
            + " seconds. Switch to PS Remote Play window now"
        )
        time.sleep(STARTUP_DELAY)


def start_exploit(section):
    """Begin a cycle"""

    print(" [-] Entering Cafe.")
    press("enter")
    sleep(6)
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
    sleep(1)  # Exploiting
    press("escape")
    press("escape")
    press("escape")
    sleep(8)

    # Back to map to open ticket
    press("right")
    press("enter")
    sleep(10)
    press("right")
    press("right")
    press("right")
    press("enter")
    press("enter")
    press("enter")
    print(" [-] Opening ticket.")
    sleep(18)

    # Accepting any kind of ticket, avoids using image detection
    print(" [-] Accepting ticket.")
    press("enter")

    # skip superfluous times for rotary tickets
    if section != "ROTARY":
        sleep(16)
        press("enter")
        sleep(6)
        press("enter")
        press("enter")
        press("enter")  # accept ticket

    # Back out of tickets
    print(" [-] Going back to map.")
    press("escape")
    press("escape")
    sleep(8)
    press("left")  # Place cursor on Menu to start over


if __name__ == "__main__":
    inputs = parse_args()
    print("*** gt7-extramenus-ps4.py ***")
    print("Using input delay of: " + str(inputs.delay) + " seconds")
    cycles = 0
    focus_window(inputs.auto)
    while True:
        start_exploit("")
        start_exploit("ROTARY")
        cycles += 1
        print(" [+] Cycles completed: " + str(cycles))
