def exclusive_to_include(amount, VAT_percentage):
    return amount * VAT_percentage


excl_VAT = float(input("What is the amount excluding VAT? "))
VAT_percentage = float(input("What is the percentage of VAT? "))

incl_VAT = exclusive_to_include(excl_VAT, VAT_percentage)

print(f"The amount you have to pay including VAT is: {incl_VAT}")
