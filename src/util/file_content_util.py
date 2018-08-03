import datetime
from dateutil.tz import tzlocal

new_line_char = '\r\n'
tab_char = '    '

def get_introduction(total_capitol, number_of_days):
    introduction = []
    introduction.append(new_line_char)
    introduction.append(
        "This is your report requested at: {0} for a capitol expenditure of: {1} over a duration of: {2} days".format(
            datetime.datetime.now(tzlocal()).strftime("%A, %d %B %Y %I:%M%p"),
            '${:,.2f}'.format(total_capitol),
            number_of_days))
    introduction.append(new_line_char)
    introduction.append(new_line_char)
    introduction.append("Report Details:")
    introduction.append(new_line_char)
    introduction.append(new_line_char)
    return introduction

def print_security_info(security_info):
    security_info_content = []
    security_info_content.append("Security: {0}".format(security_info.name))
    security_info_content.append(new_line_char)
    security_info_content.append(new_line_char)
    security_info_content.append(
        """
        With the given configuration you are able to purchase {0} share(s) every {1} days. Over the duration of this plan you will
        make {2} purchases for a total of {3} share(s) and expected contribution of ${4:,.2f}. This calculation was unable to
        consider ${5:,.2f} due to lack of alignment in purchase amount and expected contribution.
        """.format(
            security_info.batch_size,
            security_info.frequency,
            security_info.num_transactions,
            security_info.number_of_shares,
            security_info.actual_contribution,
            security_info.excess))
    security_info_content.append(new_line_char)
    security_info_content.append(new_line_char)
    for index, purchase_date in enumerate(security_info.purchase_days):
        security_info_content.append(tab_char)
        security_info_content.append("Buy Number {0}: {1}".format(
            str(index + 1),
            purchase_date.strftime("%A, %d %B %Y")))
        security_info_content.append(new_line_char)
    security_info_content.append(new_line_char)    
    security_info_content.append(new_line_char)    
        
    return ''.join(map(str, security_info_content))