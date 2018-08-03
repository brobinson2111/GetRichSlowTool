'''
Created on August 3rd, 2018
Created By: Brandon Robinson (brobinson2111)
'''

class TransactionInfo(object):

    """
    This class is stores all of the information regarding a single transaction.

    :number_of_shares The number of shares to be purchased for a given transaction.
    :datetime The Date to execute the transaction represented as a datetime object.
    """
    def __init__(self, number_of_shares, datetime):
        self.number_of_shares = number_of_shares
        self.datetime = datetime