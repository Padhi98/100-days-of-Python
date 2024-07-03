#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:41:23 2024

@author: ankitapadhi
"""

print('Welcome to the tip calculator!\n')
bill = float(input('What was the total bill? Rs.'))
tip = int(input('How much percentage of tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))

tip_percent = tip/100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_per_person = total_bill/people
final_amount = round(bill_per_person)

print(f'Each person should pay: Rs.{final_amount}')
