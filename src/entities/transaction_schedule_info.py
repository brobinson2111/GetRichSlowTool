'''
Created on August 30th, 2018
Created By: Brandon Robinson (brobinson2111)
'''

class TransactionScheduleInfo(object):

    """
    This class is stores all of the information regarding a single transaction within a produced schedule.
    An array of these items will allow users to track their transaction purchase progress.

    :security_name The name of the security for this transaction
    :number_of_shares The number of shares to be purchased for a given transaction.
    :datetime The Date to execute the transaction represented as a datetime object.
    """
    def __init__(self, security_name, number_of_shares, datetime):
        self.security_name = security_name
        self.number_of_shares = number_of_shares
        self.datetime = datetime