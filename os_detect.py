import platform

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

def detect_win_ver():
    return platform.release()

if __name__ == "__main__":
    # example
    os = detect_sys(platform.system())
    print(f"Current OS: {os}")
    if os == "Windows":
        win_ver = detect_win_ver()
        print(f"Current Version: Windows {win_ver}")