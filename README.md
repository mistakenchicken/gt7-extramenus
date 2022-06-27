![image](https://user-images.githubusercontent.com/108235690/175868206-c31cdd18-0a09-4d4f-b311-07a8202acfa5.png)

# gt7-extramenus
Gran Turismo 7 v1.17 - Extra Menus AFK Exploit

Feel free to buy me a coffee https://www.buymeacoffee.com/mistakenchG

Inspired by: https://github.com/ByPrinciple/GT7-Scripts

IMPORTANT:

For Educational purposes only. I am not responsible for any damages such as getting banned, doing something unintended on your system, or any other unintended side effect. Use this at your own risk. This script only automates what any human would do, it does not exploit any code at all.

## WORK IN PROGRESS!
- This was quickly put together, there is barely any testing, so run it at your own risk. Feel free to modify the script to your liking.

## Features
- PoC that farms 4 star and engine swap tickets from GT7 v1.17 Extra Menus exploit.

## Instructions (Windows only)

- Install PS Remote Play and set up Remote Play with your console.
- Clone the repository
- Install python and `pyautogui`
- PS Remote Screen must be on your primary monitor. Make sure the center of the screen is directly on top of the PS Remote Play window. You want it to avoid capturing the terminal window.
- Make sure the first reward you get is the 4-star ticket. (The script starts there). If not, manually do the Rotary engine ticket before starting the script.
- Make sure the cursor is on the Cafe when you start the script.
- Run the script from an elevated command prompt. Otherwise, pyautogui will not capture the PS Remote Play screen.

```
python.exe .\gt7-extramenus.py
```
- Profit!

## Instructions for using image detection (EXPERIMENTAL)

- Install the necessary modules: `pyautogui`, `pillow`, `opencv-python`

If you would like to use image detection, simply run `gt7-extramenus-detection.py` instead.

Note: Images were tested using 1980p and 1440p screens but PS Remote Play image quality can yield unpredictable results.

Why would you use this? I can't tell you why. But it was good learning more about pyautogui for future exploits that may require image detection.

The original script `gt7-extramenus.py` was using image detection, but it was not as consistent, I believe the main culprit is that the image detection depends in screen resolutions. After trying to use 1080p and 1440p versions for each sample image, I decided it was not worth the effort, even when playing with different areas of the screen and different samples.

## Contributions

Thanks to:
- https://github.com/nelitow for attempting to improve on the image detection and for fixing typos.
