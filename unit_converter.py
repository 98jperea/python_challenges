def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def meters_to_kilometers(meters):
    return meters / 1000

if __name__ == "__main__":
    print("Celsius to Fahrenheit:", celsius_to_fahrenheit(25))
    print("Meters to Kilometers:", meters_to_kilometers(500))