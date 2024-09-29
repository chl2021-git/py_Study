def find_combination(numbers, target, partial=[], start=0):
    s = sum(partial)
    if s == target:
        print("组合:", partial, s)
    if s >= target:
        return
    for i in range(start, len(numbers)):
        remaining = numbers[i+1:]
        find_combination(remaining, target, partial + [numbers[i]], i + 1)

if __name__ == "__main__":
    numbers = [7114, -5000, -1780, 361609, 3875, 29800, -330, 2750, -34560, 2460, 20044, 1047, -8881, 7618, -29789, 5505, 440, 3721, 223124, 13744, -152136, -1788]
    target = 241797
    numbers.sort()  # 排序
    find_combination(numbers, target)
    print("end", target)
