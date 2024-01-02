weight = int(input("Please enter weight in kg : "))
height = float(input("Please enter height in kg : "))
BMI = weight / height**2
BMI = round(BMI,2)
print(f"BMI = {BMI}")
if BMI < 16.0 :
    print("underweight(Severe weight)")
elif (BMI >= 16.0 and BMI <= 16.9):
    print("underweight(Moderate weight)")
elif (BMI >= 17.0 and BMI <= 18.4):
    print("underweight(Mild weight)")
elif (BMI >= 18.5 and BMI <= 24.9):
    print("Normal Range")
elif (BMI >= 25.0 and BMI <= 29.9):
    print("overweight(Pre-obese)")
elif (BMI >= 30.0 and BMI <= 34.9):
    print("obese class 1")
elif (BMI >= 35.0 and BMI <= 39.9):
    print("obese class 2")
elif (BMI >= 40):
    print("obese class 3")
