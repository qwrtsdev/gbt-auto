import time
import sys
import pyautogui
import pygetwindow as gw

MESSAGE = ["!work", "!dep all"]
INTERVAL = 60
REPEAT_COUNT = 0
WINDOW_TITLE = "Discord"
TYPING_DELAY = 0.01

def find_discord_window():
    all_windows = gw.getAllWindows()
    
    for w in all_windows:
        if WINDOW_TITLE.lower() in w.title.lower():
            return w
    return None


def focus_and_send(window):
    try:
        window.activate()
        time.sleep(0.5)
    except Exception:
        pass

    win_left   = window.left
    win_top    = window.top
    win_width  = window.width
    win_height = window.height

    click_x = win_left + win_width // 2
    click_y = win_top + int(win_height * 0.93)   # ~93% down = message input

    pyautogui.click(click_x, click_y)
    time.sleep(0.3)

    pyautogui.typewrite(MESSAGE, interval=TYPING_DELAY)
    time.sleep(0.1)
    pyautogui.press("enter")
    print(f"  [sent] {MESSAGE}")

def main():
    pyautogui.FAILSAFE = True

    print("Gapbo Town - Auto Work")
    print("==================")
    print(f"  Message  : {MESSAGE!r}")
    print(f"  Interval : {INTERVAL}s")
    print(f"  Repeats  : {'forever' if REPEAT_COUNT == 0 else REPEAT_COUNT}")
    print(f"  Failsafe : move mouse to top-left corner to stop\n")

    sent = 0
    while True:
        window = find_discord_window()
        if window is None:
            print(f"[!] No window matching '{WINDOW_TITLE}' found. Retrying in {INTERVAL}s…")
        else:
            print(f"[+] Found: '{window.title}'")
            focus_and_send(window)
            sent += 1

        if REPEAT_COUNT > 0 and sent >= REPEAT_COUNT:
            print(f"\n[done] Sent {sent} message(s). Exiting.")
            break

        print(f"    Waiting {INTERVAL}s… (Ctrl-C or top-left mouse to stop)\n")
        try:
            time.sleep(INTERVAL)
        except KeyboardInterrupt:
            print("\n[stopped] Keyboard interrupt.")
            sys.exit(0)


if __name__ == "__main__":
    main()