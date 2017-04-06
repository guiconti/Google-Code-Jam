import collections
import functools32
#import functools
import sympy.ntheory.factor_

class Jamcoin():
    def __init__(self, is_valid, divisors):
        self.is_valid = is_valid
        self.divisors = divisors

def coin_jam(filename):
    txt_file = open(filename, 'r')
    txt_file_result = open('C-large-practice-result.txt', 'w')
    test_cases_amount = int(txt_file.readline().rstrip('\n'))
    jamcoin_info = txt_file.readline().rstrip('\n').split()
    jamcoin_size = int(jamcoin_info[0])
    jamcoin_amount = int(jamcoin_info[1])

    global minValue
    minValue = int(('1' + '0'*(jamcoin_size-2) + '1'),2) - 2

    for x in range(1, test_cases_amount + 1):
        txt_file_result.write('Case #' + str(test_cases_amount) + ':')

        for y in range(1, 2):
            txt_file_result.write('\n' + generate_jamcoin(jamcoin_size, jamcoin_amount))

    txt_file_result.close
    txt_file.close

def generate_jamcoin(coin_size, amount):

    answer = ''
    generated_amount = 0

    for i in range(2 ** (coin_size - 1) + 1, 2 ** coin_size, 2):

        jamcoin = "{:b}".format(i)
        valid_coin = validate_jamcoin(jamcoin)

        if valid_coin.is_valid:

            answer += jamcoin + '  ' + ' '.join(str(divisor) for divisor in valid_coin.divisors) + '\n'
            generated_amount += 1
            print (generated_amount)

            if generated_amount >= amount:
                return answer

def validate_jamcoin(jamcoin):

    validation_jamcoin = Jamcoin(False, [])

    if not (jamcoin.startswith("1") and jamcoin.endswith("1")):
        return validation_jamcoin

    for base in range(2, 11):

        divisor = find_nontrivial_divisor(int(jamcoin, base))
        if divisor is None:
            return validation_jamcoin
        
        validation_jamcoin.divisors.append(divisor)

    validation_jamcoin.is_valid = True

    return validation_jamcoin

@functools32.lru_cache()
def find_nontrivial_divisor(n):

    return sympy.ntheory.factor_.pollard_pm1(n, retries=5)

coin_jam('C-large-practice.txt')