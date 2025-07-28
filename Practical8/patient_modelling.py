class Patients:
    def __init__(self, name, age, height_m, weight_kg):
        self.name = name
        self.age = age
        self.height = height_m
        self.weight = weight_kg
    
    def bmi_category(self):
        bmi = self.weight / (self.height ** 2)
        if bmi < 18.5:
            return f"{self.name} is underweight (BMI={bmi:.2f})"
        elif bmi > 25:
            return f"{self.name} is overweight (BMI={bmi:.2f})"
        else:
            return f"{self.name} is healthy weight (BMI={bmi:.2f})"

p1 = Patients("Alice", 30, 1.65, 50)
print(p1.bmi_category())
# ➜ Alice is underweight (BMI=18.37)
