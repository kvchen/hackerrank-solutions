from operator import xor
from functools import reduce

def main():
	cases = int(input())

	for case in range(cases):
		element_count = int(input())
		elements = [int(x) for x in input().split()]

		output = 0
		for i, elem in enumerate(elements):
			if ((element_count-i) * (i + 1)) % 2 == 1:
				output = output ^ elem

		print(output)


if __name__ == "__main__":
	main()


