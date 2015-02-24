def main():
	n, k, q = [int(x) for x in input().split()]
	elements = [int(x) for x in input().split()]

	el = len(elements)
	elements = elements

	for i in range(q):
		idx = int(input())
		print(elements[(el-k+idx) % len(elements)])


if __name__ == "__main__":
	main()