'''
Created on August 2nd, 2018
Created By: Brandon Robinson (brobinson2111)
'''

import logging
import math
from decimal import Decimal, ROUND_DOWN       
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
    :frequency The frequency at which the shares will be purchased over the duration in days
    :actual_contribution The total amount of capitol to be invested in this Security
    :excess The amount of capitol that would not evenly be divided into this Security.
            This was disregarded when determining the :actual_contribution.
    :purchase_days The list of datetime objects indicating when to purchase this security.
                   Note: None of these dates shall fall on a weekend.
    """

    __logger = logging.getLogger('src.entities.SecurityInfo')

    def __init__(self, config_json, total_capitol, requested_length):

        name = config_json['name']
        conrtribution = config_json['contribution']
        share_price = config_json['current_price']
        expected_contribution = math.floor(total_capitol * conrtribution)

        # Return None if there are not enough funds to purchase this security.
        # No plan will be provided.
        if (share_price > expected_contribution):
            raise Exception('There were not enough funds to support the purchase of %s. Please fix configuration and run again.'.format(name))

        self.name = name
        self.number_of_shares = math.floor(expected_contribution / share_price)
        self.actual_contribution = self.number_of_shares * share_price
        self.excess = self.__round_down_precision_2(expected_contribution - self.actual_contribution)
        self.frequency = math.floor(requested_length / self.number_of_shares)
        purchase_days = []
        for day in range(0, requested_length, self.frequency):
            expected_day = calendar_util.account_for_weekend((calendar_util.days_from_today(day)))
            purchase_days.append(expected_day)
        self.purchase_days = purchase_days


    def __round_down_precision_2(self, value):
        return Decimal(Decimal(value).quantize(Decimal('.01'), rounding=ROUND_DOWN))

