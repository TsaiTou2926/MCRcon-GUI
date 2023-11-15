import platform
import sys

def detect_sys(sys):
    if sys == "Linux":
        os = "Linux"
    elif sys == "Windows":
        os = "Windows"
    elif sys == "Darwin":
        os = "MacOS"
    else:
        os = "unknown"
    return os

def is_win11():
    return sys.getwindowsversion().build >= 22000

if __name__ == "__main__":
    # example
    os = detect_sys(platform.system())
    print(f"Current OS: {os}")
    if os == "Windows":
        win_ver = is_win11()
        print(f"Windows 11: {win_ver}")
        print(type(win_ver))