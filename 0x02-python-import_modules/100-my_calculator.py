#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit


if len(argv) == 4:
    operator = argv[2]

    a = int(argv[1])
    b = int(argv[3])
    match operator:
        case "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        case "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        case "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        case "/":
            print("{:d}  {:d} = {:d}".format(a, b, div(a, b)))
        case _ :
            print("{}".format("Unknown operator. Available operators: +, -, * and /"))
            exit(1)

else:
    print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
    exit(1)
