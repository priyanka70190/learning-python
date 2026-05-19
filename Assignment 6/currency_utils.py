def show_all_rates(rates):
    print(40*"-")
    print(40*"-")
    print("currency converter")
    print(40*"-")
    print(40*"-")
    for key in rates:
        print(key,"  |  ",rates[key]," GBP")
    print(40*"-")
    print(40*"-")

def convert(amount,from_currency,to_currency,rates):
    i=0
    for key in rates:
        if(from_currency == key):

            result = amount * rates[from_currency] * rates[to_currency]
            print(amount, from_currency, "=", result, to_currency)
            break

        else:
            i=i+1
            if(len(rates)<i):
                continue
            else:
                if(len(rates)==i):
                    print("Error ,not valid currency")



