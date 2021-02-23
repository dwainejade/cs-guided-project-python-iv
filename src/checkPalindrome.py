def csCheckPalindrome(input_str):
    length = len(input_str)
    reverse = length - 1
    for letter in range(round(length/2)):
        if (not input_str[letter] == input_str[reverse]):
            return False
        reverse -= 1
    return True
pal = 'annatu'
print(csCheckPalindrome(pal))