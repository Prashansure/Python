def calculate_emi(P=100000, R=10, T=12):
    R = R / (12 * 100)   # Convert annual rate to monthly
    emi = (P * R * (1 + R)**T) / ((1 + R)**T - 1)
    return emi

# Function call
emi_value = calculate_emi()
print("Monthly EMI:", round(emi_value, 2))