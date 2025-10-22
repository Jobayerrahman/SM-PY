'''
Nested if (if inside if)
- Used when we need to check one condition inside another.
'''

age = 25
salary = 40000

if age >= 18:
    if salary >= 30000:
        print("✅ Loan approved")
    else:
        print("❌ Loan denied: Low salary")
else:
    print("❌ Loan denied: Underage")
