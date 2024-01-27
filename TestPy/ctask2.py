def find_combinations(arr, target_sum):
    def backtrack(start, target, path):
        print("path",path)
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(arr)):
            backtrack(i + 1, target - arr[i], path + [arr[i]])

    result = []
    backtrack(0, target_sum, [])
    return result

# 示例用法
if __name__ == "__main__":
    #arr = [66033, -33096, 39459, -11469, 66033, -33096, 39459, -11469]
    #target = 94023
    #arr = [2750, -34560, 2460, 20044, 1047, -8881, 7618, -29780, 5505, 440, 3721, 223124, 13744, -152136, -1788, -1031112, -792970]
    arr = [2750, -34560, 2460, 20044, 1047, -8881, 7618, -29780]    
    target = -153491
    combinations = find_combinations(arr, target)
    if combinations:
        for combo in combinations:
            print(combo)
    else:
        print("没有找到任何组合等于目标值。")
