def cut(sticks, n):
	return [s - n for s in sticks if s > n]

def main():
	num_sticks = int(input())

	stick_str = input()
	sticks = [int(x) for x in stick_str.split()]

	while len(sticks) != 0:
		print(len(sticks))
		sticks = cut(sticks, min(sticks))


if __name__ == "__main__":
	main()