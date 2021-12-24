import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

parser.add_argument('--foobar', action='store_true', default=False)
parser.add_argument('--foo', dest='bar', type=int)
parser.add_argument('--foo1', type=int)

args = parser.parse_args()
print(args.integers)
print(args.accumulate)
print(args.accumulate(args.integers))
print(args.foobar)
print(args.bar, type(args.bar))
print(args.foo1, type(args.foo1))
