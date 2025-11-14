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
  for i in range(0, len(formula) - 1):
      if formula[i].isdigit() and i == 0:
        return formula
      elif formula[i].isdigit():
                return (formula[:i], (formula[i:]))
