# Ask the user for a starting number.
# Count down to 0.
# Print a message when the countdown finishes.

num = int(input("Please enter a number to initiate countdown: "))
countdown = num
print(f"Countdown: {countdown}")

while countdown != 0:
    countdown = countdown - 1
    print(f"Countdown: {countdown}")

print("\nLiftoff!!")
