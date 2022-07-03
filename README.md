![image](https://user-images.githubusercontent.com/108235690/175868206-c31cdd18-0a09-4d4f-b311-07a8202acfa5.png)

# gt7-extramenus
Gran Turismo 7 v1.17 - Extra Menus AFK Exploit
By: mistakenchicken
Follow me at: https://twitter.com/ChickenMistaken

Feel free to buy me a coffee https://www.buymeacoffee.com/mistakenchG

Inspired by: https://github.com/ByPrinciple/GT7-Scripts

IMPORTANT:

For Educational purposes only. I am not responsible for any damages such as getting banned, doing something unintended on your system, or any other unintended side effect. Use this at your own risk. This script only automates what any human would do, it does not exploit any code at all.

## WORK IN PROGRESS!
- This was quickly put together, there is barely any testing, so run it at your own risk. Feel free to modify the script to your liking.

## Features
- PoC that farms 4 star and engine swap tickets from GT7 v1.17 Extra Menus exploit.

## Instructions (Tested on Windows and Mac)

1. Install PS Remote Play and set up Remote Play with your console. Visit https://remoteplay.dl.playstation.net/remoteplay/lang/en/index.html
2. Clone the repository or download `gt7-extramenus.py` for PS5 version and `gt7-extramenus-ps4.py` for PS4
3. Install python: https://www.python.org/downloads/

**Make sure you check "Add to PATH"**

![image](https://user-images.githubusercontent.com/108235690/176962043-f3226980-1cd2-4a7e-84c0-6cfac3a47f1e.png)

4. Install python module `pyautogui`
```
pyton -m pip install pyautogui
```
5. PS Remote Screen must be on your primary monitor.
6. Make sure the first reward you get is the 4-star ticket. (The script starts there). If not, manually do the Rotary engine ticket before starting the script.
7. Make sure the cursor is on the Cafe when you start the script.
8. Run the script from an elevated command prompt. Otherwise, pyautogui will not capture the PS Remote Play screen.

### PS5
```
python .\gt7-extramenus.py
```

### PS4 ⚠️ EXPERIMENTAL (WIP)
```
python .\gt7-extramenus-ps4.py
```

**Please read!**

When the script starts, if you don't supply the `--auto` flag, it will give you 5 seconds to manually switch to the PS Remote Play window. 

If you are using `--auto`. Make sure the PS Remote Play window is right under the center of your primary screen. You want it to avoid capturing the terminal window.

9. Profit!

## Troubleshooting

**Q: My script seems to miss button presses or falls of randomly**

A: If your PS Remote Play connection is poor try passing a `--delay` value **(Default is 0.2s)**, this may improve button press timings

## Instructions for using image detection (EXPERIMENTAL)

- Install the necessary modules: `pyautogui`, `pillow`, `opencv-python`

If you would like to use image detection, simply run `gt7-extramenus-detection.py` instead.

Note: Images were tested using 1980p and 1440p screens but PS Remote Play image quality can yield unpredictable results.

Why would you use this? I can't tell you why. But it was good learning more about pyautogui for future exploits that may require image detection.

The original script `gt7-extramenus.py` was using image detection, but it was not as consistent, I believe the main culprit is that the image detection depends in screen resolutions. After trying to use 1080p and 1440p versions for each sample image, I decided it was not worth the effort, even when playing with different areas of the screen and different samples.

## Contributions and Acknowledgements

Thanks to:
- https://github.com/nelitow for attempting to improve on the image detection and for fixing typos.
- https://reddit.com/U/Whmeh0 on /r/granturismo for determining the timings for gt7-extramenus-ps4.py
- https://github.com/dehydratedH2O for optimizing the timings (~20s faster) on rotary ticket roulette screen
- The /r/granturismo subreddit community for feedback.
