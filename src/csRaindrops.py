def csRaindrops(number):
    # check if nunber is factorial of largest to smallest.
    answer = ''
    if (number % 3 == 0):
        answer = answer + "Pling"

    if (number % 5 == 0):
        answer = answer + "Plang"

    if (number % 7 == 0):
        answer = answer + "Plong"
    else: answer = number
    # return answer
    return answer

number = 7

print(csRaindrops(number))