age = 34
#txt = "My name is John, I am " + age            # It will give typeerror

#F-strings
fTxt = f"My name is John, I am {age}"
print(fTxt)

#Placeholders and Modifiers
price = 30
priceTxt = f"The price is {price} dollars"
print(priceTxt)

modifierPriceTxt = f"The price is {price:.2f} dollars"
print(modifierPriceTxt)


#Math operations in placeholder
mathOperationTxt = f"The price is {20*40} dollars"
print(mathOperationTxt)
