def counting_sheep(filename):
    txt_file = open(filename, 'r')
    txt_file_result = open('A-small-practice-result.txt', 'w')
    testCasesAmount = int(txt_file.readline())

    for x in range(1, testCasesAmount + 1):
        actualNumber = int(txt_file.readline().rstrip('\n'))
        result = solve_number(actualNumber, actualNumber, []) if actualNumber > 0 else 'INSOMNIA'

        txt_file_result.write('Case #' + str(x) + ': ' + str(result) + '\n')

    txt_file_result.close()
    txt_file.close()

def solve_number(actualNumber, sum, countedNumbers):

    for number in str(actualNumber):
        if number not in countedNumbers:
            countedNumbers.append(number)
            if (len(countedNumbers) == 10):
                return actualNumber
                
    return solve_number(actualNumber + sum, sum, countedNumbers)


counting_sheep('A-small-practice.txt')