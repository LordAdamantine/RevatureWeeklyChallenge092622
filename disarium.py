import math

def main():
    print("Checking for Disariusm: ")
    while True: # Allows for checking multiple numbers while only running the program once.
        total = 0
        i = 1
        entry = input()
        if "q" in entry:    # Quit condition to close program.
            break
        for letter in str(entry):   # Easy way to cycle through all of the digits one by one.
            total += int(letter)**i
            i += 1  # Since the index starts at 1 and goes up each position, incrementing i makes it easy.

        if total == int(entry): # These outputs can be changed to output whatever is necessary, allowing this module to easily slot in to another program.
            print(f"{entry} is a disariusm number.")
        else:
            print(f"{entry} is not a disariusm number.")

if __name__ == "__main__":
    main()