
def get_expensive_products(prices):
    expensive=[]
    for price in prices:
        if price > 100:
            expensive.append(price)
    return expensive
prices=[120,45,300,85,150]
result= get_expensive_products(prices)
print(result)
 


