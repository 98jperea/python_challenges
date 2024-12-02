import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time left: {seconds} seconds", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    secs = int(input("Enter time in seconds: "))
    countdown_timer(secs)