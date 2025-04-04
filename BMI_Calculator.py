class BMICalculator:
    '''Class to handle BMI Calculation and categorization.'''

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        return self.weight / (self.weight ** 2)

    def determine_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal Weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    def display_result(self):
        #Calculating the bmi, determining the category and displaying the result
        bmi = self.calculate_bmi()

        category = self.determine_bmi_category(bmi)

        #Displaying the result
        print(f"BMI: {bmi:.1f}")
        print(f"Category: {category}")

weight = float(input("Enter weight (in kilogram): "))
height = float(input("Enter height (in meters): "))

bmi_calculator = BMICalculator(weight, height)


bmi_calculator.display_result()