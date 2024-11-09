def main():
    # Prompt the user for mass in kilograms
    mass = int(input("Enter mass in kilograms: "))

    # Define the speed of light
    speed_of_light = 300000000  # in meters per second

    # Calculate energy using E = mc^2
    energy = mass * (speed_of_light ** 2)

    # Output the energy in Joules
    print(energy)


# Call the main function
if __name__ == "__main__":
    main()