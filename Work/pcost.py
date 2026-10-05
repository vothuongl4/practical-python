# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        headers = next(f)

        for line in f:
            try:
                row = line.split(',')
                nshares = int(row[1])
                price = float(row[2])
                total_cost += (nshares * price)
            except ValueError:
                print('Bad row', row)
    return total_cost

cost  = portfolio_cost('Data/portfolio.csv')
print(f"Total cost {cost:.2f}")