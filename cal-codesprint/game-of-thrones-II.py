from math import factorial, log


def fact_large(x, mod):
	total = 1
	while x > 0:
		total = (total * x) % mod
		x -= 1
	return total

def exp_large(x, n, mod):
	if n == 0:
		return 1
	elif n == 1:
		return x % mod

	if n%2 == 0:
		total = exp_large(x, n // 2, mod) ** 2
	else:
		total = exp_large(x, n-1, mod) * x

	return total % mod


def main():
	letters = input()
	mod = 10**9 + 7
	answer = 51681694264200 % mod

	counts = {}
	for letter in letters:
		if letter not in counts:
			counts[letter] = 1
		else:
			counts[letter] += 1
	
	psl = 0
	for letter, count in counts.items():
		psl += count // 2

	output = fact_large(psl, mod)

	for letter, count in counts.items():
		for i in range(1, count//2+1):
			exp = exp_large(i, mod - 2, mod)
			output = (output * exp) % mod

	print(output)
	

if __name__ == "__main__":
	main()