#!/usr/bin/python
##################################################################
#
# Purpose:
#   Calculate mortgage payment
# Author: Chunhui Han, Ph.D.
# 
##################################################################

import sys, os, commands, datetime, time, csv

def calc():
    print '**************************************'
    print '**                                  **'
    print '** Welcome to Mortgage Calculation  **'
    print '**                                  **'
    print '** Author: Chunhui Han, Ph.D.       **'
    print '**                                  **'
    print '** All rights reserved.             **'
    print '**                                  **'
    print '** Last update time: 10/21/2007     **'
    print '**                                  **'
    print '**************************************'
    print ''
    print 'To use this program, you need to enter the following parameters:'
    print '1. P: The principal amount.'
    print '2. Y: The number of years to pay down your mortgage.'
    print '3. I: Yearly interest rate.'
    try:
        P = int(raw_input('P = (in 000\'s)'))
        nyear = int(raw_input('N = '))
        interest = float(raw_input('I = (%)')) / 100.
    except:
        print 'Erorr interpreting the data. Program will exit.'
        sys.exit(1)
    if P > 10**5 or P < 1 or nyear < 1 or nyear > 100 or interest < 0 or interest > 1:
        print 'Invalid data. Program will exit.'
        sys.exit(1)
    i = interest / 12.
    M = P * 1000 * i / (1 - (1 + i)**(-nyear * 12))
    print 'Your monthly payment will be:',
    print '$%.2f' %M

def main(argv):
    calc()
    return

#############################
if __name__ == '__main__':
    sys.exit(main(sys.argv))
#############################
