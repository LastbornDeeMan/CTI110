# CTI 110
# P5T1 - Functions
# Davisc
# 10/24/23

def main():
  print("Hello world!")
  burger = 4.999000001
  print_money(burger)
  print_money(12)
  print_money(0.3)
  print_money(6.9)
  print_money(4.2)
# main() ends

# other functions go here
def print_money(amount):
  print("$", format(amount, ".2f"), sep="")


# Now, start the program
main()