'''
Created on August 2nd, 2018
Created By: Brandon Robinson (brobinson2111)
'''

import logging
import math
import random
from decimal import Decimal, ROUND_DOWN
from src.entities.transaction_info import TransactionInfo       
from src.util import calendar_util

class SecurityInfo(object):
    """
    This class will store all of the Security Information for a Single Security. It will calculate needed statistics
    from the provided attributes.

    input properties:
    :config_json The json configuration from file for a single Security. Conforms to the schema name, contribution,
                 current_price
    :total_capitol The total amount of capitol delegated to this Application Run. This will be used to determine
                   the individual contribution for the Security.
    :requested_length The duration requested for this Application Run. This will determine how often and how many
                      times a Security must be purchased.

    class level properties:
    :name The Name of the Security.
    :number_of_shares The total number of shares to be purchased over the duration
    :num_transactions The total number of transactions that will be made for this Security.
    :frequency The frequency at which the shares will be purchased over the duration in days
    :actual_contribution The total amount of capitol to be invested in this Security
    :excess The amount of capitol that would not evenly be divided into this Security.
            This was disregarded when determining the :actual_contribution.
    :transaction_list The list of Transaction Info objects indicating how many shares of a security to purchase
                      and on what date to make that purchase.
                      Note: None of these dates shall fall on a weekend.
    """

    __logger = logging.getLogger('src.entities.SecurityInfo')

    __reduction_coefficient = 1.01
    __min_frequency = 9

    def __init__(self, config_json, total_capitol, requested_length):

        name = config_json['name']
        conrtribution = config_json['contribution']
        share_price = config_json['current_price']
        expected_contribution = math.floor(total_capitol * conrtribution)

        # Return None if there are not enough funds to purchase this security.
        # No plan will be provided.
        if (share_price > expected_contribution):
            raise Exception('There were not enough funds to support the purchase of {0}. Please fix configuration and run again.'.format(name))

        self.name = name

        target_shares = math.floor(expected_contribution / share_price)
        initial_frequency = math.floor(requested_length / target_shares)

        if(initial_frequency > self.__min_frequency):
            self.frequency = initial_frequency
            self.__handle_high_frequency(requested_length)
        else:
            self.__handle_low_frequency(target_shares, requested_length)


        self.num_transactions = len(self.transaction_list)
        self.number_of_shares = sum(transaction.number_of_shares for transaction in self.transaction_list)
        self.actual_contribution = self.number_of_shares * share_price
        self.excess = self.__round_down_precision_2(expected_contribution - self.actual_contribution)

    def __handle_high_frequency(self, requested_length):
        transaction_list = []
        for day in range(self.frequency, requested_length + 1, self.frequency):
            expected_day = calendar_util.account_for_weekend(
                calendar_util.days_from_today(
                    random.randint(day - self.frequency, day)))
            transaction = TransactionInfo(1, expected_day)
            transaction_list.append(transaction)
        self.transaction_list = transaction_list

    def __handle_low_frequency(self, target_shares, requested_length):

        # Set Frequency to __min_frequency
        # Get all of the transactions for that frequency
        # All transactions will have a number_of_shares = 1
        self.frequency = self.__min_frequency
        self.__handle_high_frequency(requested_length)

        # Calculate the shares that still must be distributed across transactions
        number_of_transactions = len(self.transaction_list)
        additional_shares = target_shares - number_of_transactions
        
        # For the remainder of the shares that may be equally distributed, add
        # those shares to each transaction
        even_distribution_amount = math.floor(additional_shares / number_of_transactions)
        for index in range(0, number_of_transactions):
            self.transaction_list[index].number_of_shares += even_distribution_amount

        # Randomly distribute the remainder of the shares across all of the transactions
        remainder = additional_shares % number_of_transactions
        possible_locations = list(range(0, number_of_transactions))
        for index in range(0, remainder):
            random_index = possible_locations[random.randint(0, len(possible_locations) - 1)]
            random_item = self.transaction_list[random_index]
            random_item.number_of_shares += 1
            del possible_locations[possible_locations.index(random_index)]

    def __round_down_precision_2(self, value):
        return Decimal(Decimal(value).quantize(Decimal('.01'), rounding=ROUND_DOWN))

