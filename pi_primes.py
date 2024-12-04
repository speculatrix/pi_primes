#!/usr/bin/python3
''' searches for prime numbers which are int(pi * 10^N)
    no optimisation has been done, and bugs are likely
'''

from mpmath import mp       # see https://mpmath.org/
from primePy import primes  # pip3 install primePy

MAX_DEC_PLACES = 50

##########################################################################################
def main():
    ''' main function '''


    stop_count = MAX_DEC_PLACES     # stops runaway process
    mp.dps = MAX_DEC_PLACES         # limit decimal places

    # initial value of pi
    pi_mult = mp.pi(dps=MAX_DEC_PLACES)

    offset = 0              # how many times shifted left

    pi_dec_part = 1         # ensure loop runs at least once
    while stop_count > 0 and pi_dec_part > 0:
        pi_int = int(pi_mult)
        shifted_is_prime = primes.check(pi_int)
        if shifted_is_prime:
            print(f'{offset} {pi_int} is prime')
        else:
            print(f'{offset} {pi_int} is not prime')

        # shift left
        offset += + 1
        pi_mult *= 10

        # need to stop when there's no more decimal part
        pi_dec_part = mp.fmod(pi_mult,1)
        #print(f'dec_part {pi_dec_part}')

        stop_count -= 1

##########################################################################################

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
