def is_vaild_brackets(expression : str) -> bool:
    stack = []
    brackets = {')':'(', '}':'{', ']':'[' }

    for letter in expression:
        if letter in brackets.values():
            stack.append(letter)
        if letter == brackets.keys():
            if not stack or stack.pop() != brackets[letter]:
                return False
    return not stack


print(is_vaild_brackets("{}"))
print(is_vaild_brackets("(]"))
print(is_vaild_brackets("{)"))