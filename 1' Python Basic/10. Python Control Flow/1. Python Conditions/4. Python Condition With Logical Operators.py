#Logical operators help us combine multiple conditions inside if statements.

'''
| Operator | Meaning                                    | Example                         |
| -------- | ------------------------------------------ | ------------------------------- |
| `and`    | True only if **both** conditions are true  | age > 18 **and** salary > 10000 |
| `or`     | True if **at least one** condition is true | age < 18 **or** student == True |
| `not`    | Reverses boolean value                     | not logged_in                   |

'''


#✅ Example 1: and
age = 25
has_id = True

if age >= 18 and has_id:
    print("✅ You can enter the club.")
else:
    print("❌ Entry denied.")


#✅ Example 2: or
is_student = False
has_discount_coupon = True

if is_student or has_discount_coupon:
    print("✅ You get a discount!")
else:
    print("❌ No discount available.")


#✅ Example 3: not
logged_in = False

if not logged_in:
    print("⚠ Please log in to continue.")

