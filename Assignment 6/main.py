from currency_utils import convert,show_all_rates
rates={"GBP":1.0,"USD":1.27,"EUR":1.16,"INR":124.17,"AED":4.76,"JPY":196.08}
show_all_rates(rates)

print("Enter the source currency:")
source_currency=input()
print("Enter the target currency:")
target_currency=input()
print("Enter the Amount:")
amount=int(input())
convert(amount,source_currency,target_currency,rates)