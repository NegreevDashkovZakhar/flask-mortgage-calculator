from flask import Flask, render_template, request

from service.annuityService import get_annuity_mortgage

app = Flask("Mortgage calculator")


@app.route('/', methods=['post', 'get'])
def annuity_calculator():
    if request.method == 'POST':
        amount = int(request.form.get('mortgage_amount'))
        first_pay = int(request.form.get('first_pay'))
        duration = int(request.form.get('mortgage_duration'))
        interest_rate = float(request.form.get('interest_rate'))
        result = get_annuity_mortgage(amount, first_pay, duration, interest_rate)
        return render_template('annuity.html', result=round(result, 2))
    else:
        return render_template('annuity.html')


if __name__ == '__main__':
    app.run()
