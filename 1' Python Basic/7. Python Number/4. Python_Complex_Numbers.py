# Complex numbers in Python have a real part and an imaginary part.
# The imaginary part is denoted by 'j' (like in electrical engineering or math).

x = 3 + 5j    # complex number with real part 3 and imaginary part 5
y = 5j        # purely imaginary number
z = -5j       # negative imaginary number

print(type(x))  # <class 'complex'>
print(type(y))  # <class 'complex'>
print(type(z))  # <class 'complex'>


# ---------------------- Real-Life Example ----------------------


# Example: Representing AC electrical signals
voltage = 230 + 5j     # 230V real part, 5V imaginary (phase)
current = 10 - 2j      # 10A real, 2A imaginary
power = voltage * current

print("Voltage:", voltage, "Current:", current, "Power:", power)
