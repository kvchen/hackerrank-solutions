def main():
	letters = input()

	counts = {}
	for letter in letters:
		if letter not in counts:
			counts[letter] = 1
		else:
			counts[letter] += 1
	
	odd_counts = 0
	for letter, count in counts.items():
		if count % 2 == 1:
			odd_counts += 1

	print("YES" if odd_counts < 2 else "NO")

if __name__ == "__main__":
	main()