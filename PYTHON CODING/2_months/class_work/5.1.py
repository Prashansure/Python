class ElectricityBill:
    def __init__(self, previous_reading, current_reading):

        if current_reading < previous_reading:
            raise ValueError("Invalid meter reading")

        self.previous = previous_reading
        self.current = current_reading
        self.units = current_reading - previous_reading

    def calculate_energy_charge(self):
        units = self.units
        charge = 0

        if units <= 100:
            charge = units * 1.5

        elif units <= 300:
            charge = 100 * 1.5 + (units - 100) * 2.5

        elif units <= 500:
            charge = 100 * 1.5 + 200 * 2.5 + (units - 300) * 4

        else:
            charge = 100 * 1.5 + 200 * 2.5 + 200 * 4 + (units - 500) * 6

        return charge

    def calculate_total_bill(self):
        energy_charge = self.calculate_energy_charge()
        fixed_charge = 50
        tax = energy_charge * 0.05

        total_bill = energy_charge + fixed_charge + tax
        return total_bill


# -------- MAIN PROGRAM --------

previous = int(input("Enter previous meter reading: "))
current = int(input("Enter current meter reading: "))

bill = ElectricityBill(previous, current)

print("Units Consumed:", bill.units)
print("Total Bill Amount: Rs.", bill.calculate_total_bill())