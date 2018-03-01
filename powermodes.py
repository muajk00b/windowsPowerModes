import subprocess

powerModes = {"1" : "powercfg -SETACTIVE SCHEME_BALANCED", "2" : "powercfg -SETACTIVE SCHEME_MAX", "3" : "powercfg -SETACTIVE SCHEME_MIN"}

while True:
    choice = input("1 - Balance\n2 - Power Saver\n3 - High Performance \n")
    if choice.isalpha():
        print("Please enter a number!")
        continue
    else:
        if choice == "1":
            subprocess.call(powerModes["1"])
            print("Set power mode to 'Balanced'.")
            break
        elif choice == "2":
            subprocess.call(powerModes["2"])
            print("Set power mode to 'Power Saver'.")
            break
        elif choice == "3":
            subprocess.call(powerModes["3"])
            print("Set power mode to 'High Performance'.")
            break
        else:
            print("Choose a Mode")
