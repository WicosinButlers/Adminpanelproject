import time
import tkinter as tk
import sys
import subprocess

# Flag to check if admin permissions are granted
admin_granted = False

def open_user_videos():
    try:
        # Path to the user's Videos folder
        folder_path = r"C:\Users\lando\Videos"
        # Open the folder using Windows Explorer
        subprocess.run(["explorer", folder_path], check=True)
        print("User videos opened successfully.")
    except Exception as e:
        print(f"Error opening Videos: {e}")

def open_obs():
    try:
        # Path to the OBS folder
        obs_path = r"C:\Program Files\obs-studio\bin\64bit"
        # Open the folder using Windows Explorer
        subprocess.run(["explorer", obs_path], check=True)
        print("OBS opened successfully.")
    except Exception as e:
        print(f"Error opening OBS: {e}")

def open_epic_games():
    try:
        # Path to the Epic Games Launcher
        epic_games_path = r"C:\Program Files\Epic Games\Launcher\Portal\Binaries\Win64\EpicGamesLauncher.exe"
        # Open the Epic Games Launcher
        subprocess.run([epic_games_path], check=True)
        print("Epic Games Launcher opened successfully.")
    except Exception as e:
        print(f"Error opening Epic Games Launcher: {e}")

def open_admin_window():
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Admin Panel")
    window.geometry("400x200")

    # Label to show admin message
    label = tk.Label(window, text="YOUR ADMIN, YOU HAVE POWER!", font=("Arial", 16))
    label.pack(pady=20)

    # Text box for user input
    entry = tk.Entry(window, font=("Arial", 14))
    entry.pack(pady=10)

    # Function to handle submission of input
    def check_input(event=None):
        user_input = entry.get()
        if "jjkneecap" in user_input:
            open_user_videos()
        elif "sudorec" in user_input:
            open_obs()
        elif "sudoEP" in user_input:
            open_epic_games()
        else:
            print("No valid command input.")
        window.destroy()  # Close the window after processing the input

    # Bind the "Enter" key to check the input
    entry.bind("<Return>", check_input)

    # Start the Tkinter loop
    window.mainloop()

def quick_admin_access():
    word = input("What's the useful word? ").strip().lower()
    if word == "cimis2-10":
     TFA = input("2FA intorduced what is the 2FA?")
    if TFA == "#)!^$()": print("Admin quick portal launched..")
    open_admin_window()
  

def main():
    global admin_granted
    
    # Check for quick admin access
    Faster_way = input("FW? y/n ").strip().lower()
    if Faster_way == "y":
        quick_admin_access()
        return

    Are_you_fast = input("Are you fast? ").strip().lower()

    if Are_you_fast in ["yes", "yea", "yep"]:
        print("I'm the fastest")
        time.sleep(0.5)
        print("No, I am!")
        time.sleep(0.5)
        print("How so?")
        time.sleep(0.5)
        print("Because... I don't know.")
        time.sleep(0.5)
        print("How about a race?")
        time.sleep(0.5)
        print("Okay, fine. Meet me at 3:45 on the track.")
        time.sleep(0.5)
        print("Okay.")
    elif Are_you_fast in ["no", "not really", "not rlly"]:
        print("Just train and you'll get faster, that's what I did. It's awesome!")
    else:
        print("Try some different words.")

    # Check for admin
    if Are_you_fast == "admincmd":
        print("Admin input recognized")
        Pass_word = input("What's the password? ").strip().lower()
        if Pass_word in ["cypr3a-10", "adminportal--"]:
            print("ADMIN PERMS ACTIVATED")
            admin_granted = True  # Set flag to True since admin permissions are granted
            open_admin_window()  # Open the admin window
        else:
            print("ADMIN PERMS DENIED!")
            Attempted_access = input("Why did you try and access Admin commands without the correct pass? ").strip().lower()

            if Attempted_access in ["im a hacker", "idk"]:
                print("OK")
            elif Attempted_access == "future":
                lo_cation = input("addy? ").strip().lower()
                if lo_cation == "cyp-hou":
                    print("ADMIN PERMS GRANTED!")
                    admin_granted = True  # Admin permissions granted if location is correct
                    open_admin_window()  # Open the admin window
                else:
                    print("Try some different words.")
            else:
                print("Try some different words.")

    # Only exit if admin permissions are not granted
    if not admin_granted:
        time.sleep(5)
        sys.exit()  # Exit the program if no admin permissions are granted

if __name__ == "__main__":
    main()
