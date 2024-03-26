def find_Max(nums):
    # 이 함수는 주어진 숫자 리스트에서 최대값을 찾아 반환합니다
    max_num = nums[0]
    
    for num in nums:
        if num > max_num:
            max_num = num 
    return max_num  

# 리스트 예시
num_list = [1, 2, 3, 4, 5]

# 결과 출력
print("최대값:", find_Max(num_list))
