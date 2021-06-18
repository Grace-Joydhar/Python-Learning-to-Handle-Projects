# A BMI Calculator
Name_1 = 'Karim'
Height_m1 = 2
Weight_kg1 = 90

Name_2 = 'Karim Sister'
Height_m2 = 1.8
Weight_kg2 = 70

Name_3 = 'Karim Brother'
Height_m3 = 2.5
Weight_kg3 = 160

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m / 2)
    print('BMI:', bmi)
    if bmi > 25:
        return name + 'is not overweight'
    else:
        return name + 'is overweight'

result1 = bmi_calculator(Name_1, Height_m1, Weight_kg1)
result2 = bmi_calculator(Name_2, Height_m2, Weight_kg2)
result3 = bmi_calculator(Name_3, Height_m3, Weight_kg3)

print(result1)
print(result2)
print(result3)