def find_max_count():
    s = [int(num) for num in input().split()]
    print(max(a for a in s if s.count(a) == max(map(s.count, s))))

if __name__ == "__main__":
    find_max_count()