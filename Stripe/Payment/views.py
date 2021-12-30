from django.shortcuts import render
from django.http import HttpResponse
import stripe

# Create your views here.
def index(request):
    return render(request, 'product.html') 


def payment(request):
    stripe.api_key = "sk_test_4NBbDxxVc50ogIZOEARYRKNP00AnsXYzDi"

    # c = stripe.Charge.create(
    #     amount=2000,
    #     currency="inr",
    #     source="tok_mastercard",
    #     description="Rent",
    # )

    # r= stripe.Refund.create(
    #     charge="ch_1KCMvpAyRbhKDr5DUIYga3TZ",
    # )
    # print(r)

    # token = stripe.Token.create(
    # card={
    #         "number": "4242424242424242",
    #         "exp_month": 12,
    #         "exp_year": 2022,
    #         "cvc": "314",
    #     },
    # )
    # print(token)
    return HttpResponse("Hello, world. You're at the polls index.")

def CardDetails(request):
     if request.method=='POST':
        amount = request.POST['totalPrice']
        print(amount)
        return render(request, 'payment.html', {'amount': amount})


def PaymentDone(request):
    stripe.api_key = "sk_test_4NBbDxxVc50ogIZOEARYRKNP00AnsXYzDi"
    if request.method=='POST':
        print(request.POST)

        c = stripe.Charge.create(
            amount=int(request.POST['amount'])*100,
            currency="inr",
            source=request.POST['stripeToken'],
            description="Rent",
        )

        print(c.status)

        if c.status=='succeeded':
            return HttpResponse("Payment Done")