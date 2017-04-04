def revenge_of_the_pancakes(filename):
    txt_file = open(filename, 'r')
    txt_file_result = open('B-large-practice-result.txt', 'w')
    test_cases_amount = int(txt_file.readline())

    for x in range(1, test_cases_amount + 1):
        actual_state = txt_file.readline().rstrip('\n')
        txt_file_result.write('Case #' + str(x) + ': ' + str(solve(actual_state, 0)) + '\n')
        #print ('Case #' + str(x) + ': ' + str(solve('+-+', 0)) + '\n')

    txt_file_result.close
    txt_file.close

def flip(state):
    state.reverse()
    state = ''.join(state).replace('+', '%temp%').replace('-', '+').replace('%temp%', '-')
    return state

def solve(state, flip_amount):

    if state.count('-') == 0:
        return flip_amount
    if state.count('+') == 0:
        return flip_amount + 1

    find_char = '-' if state[0] == '+' else '+'

    index = state.index(find_char)

    state = ''.join(flip(list(state[0:index]))) + state[index:len(state)]

    return solve(state, flip_amount + 1)

revenge_of_the_pancakes('B-large-practice.txt')