def get_annuity_mortgage(amount, first_pay, duration, interest_rate):
    left_amount = amount - first_pay
    month_interest_rate = interest_rate / 1200
    month_duration = duration * 12
    return left_amount * month_interest_rate / (1 - (1 + month_interest_rate) ** -month_duration)
