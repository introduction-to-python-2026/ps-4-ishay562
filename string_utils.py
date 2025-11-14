def split_before_each_uppercases(formula):
    split_formula = []
    start = 0
    
    # Handle empty string case
    if not formula:
        return []

    # Loop through the string starting from the second character logically
    # 'end' here represents the current character index
    for end in range(len(formula)):
        # Check for uppercase letters from the second character onwards
        if end > 0 and formula[end].isupper():
            # When an uppercase letter is found, append the substring
            # from 'start' to 'end' to the list
            split_formula.append(formula[start:end])
            # Update 'start' to the current 'end' position
            start = end

    # After the loop, append the last part of the string (from 'start' to the end)
    split_formula.append(formula[start:len(formula)])
    
    return split_formula

def split_at_first_digit(formula):
    digit_location = 0
    for i, char in enumerate(formula):
        if i == 0 and char.isdigit(): # handle cases like '40' (prefix will be empty) or '4H' (prefix will be empty) or '4' (prefix will be empty)
            digit_location = i
            break
        if char.isdigit():
            digit_location = i
            break
        digit_location = i + 1 # if no digit is found, digit_location will be len(formula)

    if digit_location == len(formula): # No digit found
        return formula, 1
    else:
        prefix = formula[:digit_location]
        numeric_part = int(formula[digit_location:])
        return prefix, numeric_part
