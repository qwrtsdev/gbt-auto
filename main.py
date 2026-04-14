import time
import sys
import pyautogui
import pygetwindow as gw

MESSAGES = [
    ("!work",    20),
    ("!dep all", 70),
]
WINDOW_TITLE  = "Discord"
TYPING_DELAY  = 0.01

def find_discord_window():
    for w in gw.getAllWindows():
        if WINDOW_TITLE.lower() in w.title.lower():
            return w
    return None

def click_message_box(window):
    try:
        window.activate()
        time.sleep(0.5)
    except Exception:
        pass

    click_x = window.left + window.width // 2
    click_y = window.top + int(window.height * 0.93)
    pyautogui.click(click_x, click_y)
    time.sleep(0.3)

def send_message(text):
    pyautogui.typewrite(text, interval=TYPING_DELAY)
    time.sleep(0.1)
    pyautogui.press("enter")

def main():
    pyautogui.FAILSAFE = True

    print("Gapbo Town - Auto Work & Deposit")
    print("==================================")

    loop = 0
    while True:
        loop += 1
        print(f"ทำงานไปแล้ว : {loop} ครั้ง")

        window = find_discord_window()
        if window is None:
            print(f"ไม่พบหน้าต่าง Discord")
            time.sleep(10)
            continue

        for msg, wait in MESSAGES:
            click_message_box(window)
            send_message(msg)
            try:
                time.sleep(wait)
            except KeyboardInterrupt:
                sys.exit(0)

if __name__ == "__main__":
    main()