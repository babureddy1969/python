import sys

import csv
def cost(filename):
    total_price=0
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                row[3] = float(row[3])
                row[4] = int(row[4])
            except ValueError as e:
                print("Value error",e)
                continue
            total_price += row[3]*row[4]
    return total_price
if __name__ == "__main__":
    program_name = sys.argv[0]
    
    arguments = sys.argv[1:]
    count = len(arguments)
    if count < 1:
        print("Usage python exception.py <filename>.csv")
        exit()
    print("Cost %10.2f" % cost(arguments[0]))