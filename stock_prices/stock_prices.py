#!/usr/bin/python

import argparse

p = [1050, 270, 1540, 3800, 2]


def find_max_profit(prices):
    max_profit = 0

    for i, left_side_num in prices:
        for right_side_num in prices[i + 1:]:
            profit = right_side_num - left_side_num

            if max_profit == 0 or profit > max_profit:
                max_profit = profit
    return max_profit


print(find_max_profit(p))
pass


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
