weight = int(input("Welcome to the BMI calculator\nEnter your weight in kg\n"))
height = float(input("Enter your height in meters\n"))

bmi = weight/(height**2)

print(f"Your BMI is {int(bmi)} and height is {height} and weight is {weight}")
