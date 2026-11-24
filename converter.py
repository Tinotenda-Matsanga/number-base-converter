def to_binary(decimal_number):
    return bin(decimal_number)[2:]

def to_hexadecimal(decimal_number):
    return hex(decimal_number)[2:].upper()

def to_octal(decimal_number):
    return oct(decimal_number)[2:] 

def to_bcd(decimal_number):
    bcd_nibbles = []
    for digit in str(decimal_number):
        four_bit = bin(int(digit))[2:].zfill(4)
        bcd_nibbles.append(four_bit)
    return ''.join(bcd_nibbles)

def main():
  while True:
    user_input = input(
        "\nEnter a decimal number (or 'q' to quit): "
    ).strip()

    if user_input.lower() == "q":
      break

    if not user_input.isdigit():
      print("Please enter a valid positive number.")
      continue

    decimal_number = int(user_input)
    print(f"Binary: {to_binary(decimal_number)}")
    print(f"Hexadecimal: {to_hexadecimal(decimal_number)}")
    print(f"Octal: {to_octal(decimal_number)}")
    print(f"BCD: {to_bcd(decimal_number)}")


if __name__ == "__main__":
  main()

