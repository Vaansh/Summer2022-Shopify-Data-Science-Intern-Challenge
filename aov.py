import csv

import numpy as np


def main():
    """
    main method
    """
    # open csv file
    data = csv.reader(open('data.csv'))
    res = aov(data)
    print("Average Order Value: ${:.2f}".format(res), \
        "\nHave a nice day! :)")


def aov(data):
    """ 
    calculate saverage order value of the gicen csv file.

    Args:
        data (reader object): given csv file

    Returns:
        decimal: average order value calculated.
    """
    # initialize empty strings
    total_items, order_amount = [], []

    # add each row into list
    for row in data:
        order_amount.append(row[3])
        total_items.append(row[4])

    # sanitize: remove 'order_amount' and 'total_items' from our list
    order_amount.pop(0), total_items.pop(0)

    # sum uo the lists and return the aov calculated
    return np.sum(np.array(order_amount).astype(int))/np.sum(np.array(total_items).astype(int))


if __name__ == "__main__":
    main()
