############# Two Sum #############
# input1 : nums=[2,7,11,15]
# input2 : target=9
# output : [0,1] -> 2개가 아닐 수도 있음

def twoSum(nums:list,target:int)-> list: # 시간복잡도 o(n^2)
    # target이상인 수 제외
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

print(twoSum([2,7,11,15],9))


# in 연산 이용
# 시간복잡도는 같지만 속도 향상
def twoSum(nums:list,target:int)-> list:
    for i,n in enumerate(nums):
        remains=target-n
        if remains in nums[i+1:]:
            return [nums.index(n),nums[i+1:].index(remains)+(i+1)]
print(twoSum([2,7,11,15],9))


# 위 코드 이용해서 내가 수정한 것
def twoSum(nums:list,target:int)-> list:
    for i,n in enumerate(nums):
        if n>target:
            pass
        remains=target-n
        if remains in nums[i+1:]:
            return [nums.index(n),nums[i+1:].index(remains)+(i+1)]

print(twoSum([11,7,2,15],9))
print(twoSum([2,7,11,15],9))

# 첫번째 수 뺀 결과 키 조회
# 실질적 시간복잡도 개선: 평균적으로 o(1), 최악 o(n) -> 분할 상황분석 시간 복잡도 o(1)
def twoSum(nums:list, target:int)-> list:
    nums_map={}
    for i,num in enumerate(nums):
        nums_map[num]=i

    for i,num in enumerate(nums):
        if target-num in nums_map and i != nums_map[target-num]:
            return [i,nums_map[target-num]]

print(twoSum([2,7,11,15],9))


# 조회구조 개선
# 성능상 이점은 미약
def twoSum(nums:list, target:int)->list:
    nums_map={}
    # 하나의 for문으로 통합
    for i,num in enumerate(nums):
        nums_map[num] = i # nm[2]=0, nm[7]=1,
        if target-num in nums_map:
            return [nums_map[target-num],i] # 인덱스가 큰 값이 i가 됨. 맨 처음에는 nums_map에 아무것도 없으니까 pass되고, 점차 nums_map에 데이터가 쌓이면서 i가 더 큰 인덱스

print(twoSum([2,7,11,15],9))


# 투 포인터 이용
# 입력값은 정렬된 리스트임을 가정하고 푼다.
def twoSum_ordered(nums:list,target:int)-> list:
    left,right=0,len(nums)-1
    while left<right:
        # 합이 target보다 작을 때
        if nums[left]+nums[right]<target:
            left+=1 # 하한이 커져야함
        # 합이 target보다 클 때
        elif nums[left]+nums[right]>target:
            right-=1 # 상한이 작아져야함
        else:
            return [left,right]

print(twoSum_ordered([2,7,11,15],9))

# 만약에 인덱스가 아니라, 값을 리턴하라는 것이고, 입력값이 정렬이 안되어 있을 때
def twoSum_val(nums:list, target:int)->list:
    nums.sort() # 인덱스 망해버림
    left,right=0,len(nums)-1
    while left!=right:
        if nums[left]+nums[right]<target:
            left+=1
        elif nums[left]+nums[right]>target:
            right-=1
        else:
            return [nums[left],nums[right]]

print(twoSum_val([11,7,15,2],9))


############# Trapping Rain Water #############
### 이해못함-> stack 부분!! water, dist 계산식 의미 다시 생각해보기
# input: [0,1,0,2,1,0,1,3,2,1,2,1]
# output: 6

def trap(height:list)-> int:
    if not height:
        return 0
    volume=0
    left, right=0,len(height)-1
    left_max, right_max=height[left],height[right]

    while left<right:
        left_max, right_max=max(height[left],left_max), max(height[right],right_max)

        # 더 높은 쪽을 향해 투포인터 이동
        # 왼쪽 max보다 오른쪽 max가 더 크거나 같으면 왼쪽 포인터 한칸 오른쪽 이동
        # 오른쪽 max 보다 왼쪽 max가 더 크면 오른쪽 포인터 왼쪽 한칸 이동
        # 가장 높은 위치에서 왼쪽, 오른쪽 포인터 만남
        # 이 과정중 현재 높이와 그때까지 max 차이 계산해 더함
        if left_max <= right_max:
            volume+=left_max-height[left]
            left+=1
        else:
            volume+=right_max-height[right]
            right-=1
    return volume


height=[0,1,0,2,1,0,1,3,2,1,2,1]

print(trap(height))


# 스택 쌓기
# 시간복잡도 o(n)
# 스택 쌓아넣으면서 이전보다 높이 높아지면(변곡점) 그 차이만큼 더해주기

def trap(height:list)-> int :
    stack=[]
    volume=0

    for i in range(len(height)):
        # stack.append(i) # 여기다 놓으면 안됨 -> 왜? 생각해보자!
        # 변곡점
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼냄
            top=stack.pop()
            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance= i-stack[-1]-1
            waters=min(height[i],height[stack[-1]])-height[top]

            volume+=distance*waters

        stack.append(i)
    return volume

print(trap(height))


############# 3sum #############
# input: nums=[-1,0,1,2,-1,4] # 3개의 합이 0인것 찾기
# output: [[-1,0,1],[-1,-1,2]]

def my3Sum(nums:list)->list: #### Error!!!
    res = []

    for i,v in enumerate(nums):
        target = 0
        target -= v

        for j in range(i + 1, len(nums) ):
            #print('value of j: ', nums[j])
            #print('target2', target)
            if target - nums[j] in nums[i + j + 1:]:
                res.append([v, nums[j], target - nums[j]])
                #print('-----------')

        nums.pop(0)
    #print(set(map(tuple, test)))
    return list(map(list,set(map(tuple,[sorted(x) for x in res])))) # 출력 자료형 너무 복잡함
    # 이러한 자료형 이유? : [0,0,0,0] -> Not [[0,0,0],[0,0,0,]]  [-1,0,1,0] ->  [[-1,0,1],[-1,1,0]]
# 에러 뜸 -> test=[3,0,-2,-1,1,2]  # [[-2,-1,3],[-2,0,2],[-1,0,1]] => 실제로는 [[-2,-1,3]] 나옴


# 투포인터 이용
def threeSum(nums:list)-> list:
    result=[]
    nums.sort()

    for i in range(len(nums)-2):
        # 중복된 값 건너뛰기
        if i>0 and nums[i]==nums[i-1]: # 이전에 추가함
            continue
        # 간격 좁혀가며 합 sum 계산
        left, right =i+1,len(nums)-1 # 세 수중 첫번째 수 i로 고정시키고 i이후에 나오는 숫자들은 투포인터 이용함

        while left < right:
            sums=nums[i]+nums[left]+nums[right]
            if sums<0: # 수 키워야함 : 하한 크게
                left+=1
            elif sums >0: # 수 줄여야함: 상한 작게
                right-=1
            else: # sum==0
                # 정답 및 스킵처리
                result.append([nums[i],nums[left],nums[right]])

                # 중복값 스킵
                while left<right and nums[left]==nums[left+1]: # 현재값이 다음값과 같다면, 바로 넘김
                    left+=1 # left는 하한이니까 다음값과 비교
                # 중복값 스킵
                while left<right and nums[right]==nums[right-1]: # 현재값이 이전값과 같다면, 바로 넘김
                    right-=1 # right는 상한이니까 이전값과 비교
                left+=1
                right-=1
    return result


############# Array Particion1 #############
# input: [1,4,3,2]
# output: 4
# min(1,2) + min(3,4) = 4

# 링크 사라짐
nums=[1,4,3,2]


def myminPart(nums:list)-> int:
    nums.sort()
    res=[nums[i] for i in range(len(nums)) if i%2==0]
    return sum(res)
print(myminPart(nums))

# 더 파이썬 냄새 풍기기
def arrPairSum(nums:list)->int:
    return sum(sorted(nums[::2]))

print(arrPairSum(nums))


############# Product of Array Except self #############
# input: [1,2,3,4]
# output: [24,12,8,6]

def myProduct(nums:list)-> list:
    output=[]

    for i in range(len(nums)):
        prod=1
        for j in range(len(nums)):
            if i!=j:
                prod*=nums[j]
        output.append(prod)

    return output

nums=[1,2,3,4]
print(myProduct(nums))


# 시간복잡도 줄이기 o(n^2) -> o(n)
# 왼쪽과 오른쪽 곱 사용
def ProductExcept(nums:list)->list:
    output=[]

    #왼쪽 곱
    p=1
    for i in range(len(nums)):
        output.append(p)
        p*=nums[i]

    # 오른쪽 곱
    p=1
    for j in range(len(nums)-1,0-1,-1):
        output[j]*=p
        p*=nums[j]

    return output

print(ProductExcept(nums))


############# Best Time to Buy sell Stock #############
# 한번의 거래로 낼 수 있는 최대 이익 산출
# input: [7,1,5,3,6,4]
# output: 5 : 1일때 사서 6일때 팜

# 비교: [7,6,5,4,3,2,1]일 경우는? -> [2,1]
# 언제 사느냐에 관계없이 바로 다음날 팔아야함 -1

def maxProfit(prices:list)-> int:
    profit=0
    min_price=float('inf')

    for price in prices:
        min_price=min(min_price,price)
        profit=max(profit,price-min_price)

    if profit==0:
        return None
    else:
        return profit

nums=[7,1,5,3,6,4]
print(maxProfit(nums))

nums1=[7,6,5,4,3,2,1] # 만약 이 경우는? -> 이익x 사고 팔지 않는다.
print(maxProfit(nums1))

