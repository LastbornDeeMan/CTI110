# CTI 110
# P4HW2 - Gross Pay
# 10/29/23
# Davisc
# Initialize variables
overtime_total = 0
regular_pay_total = 0
gross_pay_total = 0
num_employees = 0
# Start loop to get employee information
while True:
  # Get employee name
  employee_name = input("Enter employee name (or 'Done' to terminate): ")
  if employee_name == 'Done':
    break

  # Get pay rate and hours worked
  pay_rate = float(input("Enter employee pay rate: "))
  hours_worked = float(input("Enter employee hours worked: "))
  # Calculate overpay and regular pay
  if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
  else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate
  # Calculate gross pay
  gross_pay = regular_pay + overtime_pay
  # Update totals
  overtime_total += overtime_pay
  regular_pay_total += regular_pay
  gross_pay_total += gross_pay
  num_employees += 1
# Display results
print("Overtime total:", overtime_total)
print("Regular pay total:", regular_pay_total)
print("Gross pay total:", gross_pay_total)
print("Number of employees:", num_employees)