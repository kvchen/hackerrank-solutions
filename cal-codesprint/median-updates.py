from bisect import bisect_left


def binary_search(lst, x):
	m = bisect_left(lst, x, 0, len(lst))
	return m

def median(lst):
	x = len(lst)
	if x == 0:
		return "Wrong!"

	if x % 2 == 0:
		m = (lst[x // 2] + lst[x // 2 - 1]) / 2
	else:
		m = lst[x//2]

	return ('%f' % m).rstrip('0').rstrip('.')


def main():
	nums = []
	k = int(input())

	for i in range(k):
		operation, n = input().split()
		n = int(n)

		idx = binary_search(nums, n)

		if operation == "r":

			if idx >= len(nums) or nums[idx] != n:
				print("Wrong!")
				continue
			else:
				nums.pop(idx)

		elif operation == "a": 
			nums.insert(idx, n)
		
		print(median(nums))


if __name__ == "__main__":
	main()