############# Valid Palindrome #############

# 주어진 문자열이 회문인지 True, Flase 확인
# 대소문자 구분 X, 영문자와 숫자대상


# input : 'A man, a plan, a canal: Panama' => output: True
# input : race a car => output: False

#print('test'.isalnum()) # isalnum -> true
# isalnum()메소드: 문자열이 영어, 한글 혹은 숫자로 되어있으면 참 리턴, 아니면 거짓 리턴.
# isalpha()메소드: 문자열이 영어 혹은 한글로 되어있으면 참 리턴, 아니면 거짓 리턴.

#print('Aman,aplan,acanal,Panama'.isalnum()) # 띄어쓰기 때문 -> false
#print(''.join('A man, a plan, a canal: Panama')) # 띄어쓰기 제거, 쉼표 제거

def Palindrome(string):
    strs=[s.lower() for s in string if s.isalnum()]

    # Check Palindrome
    while len(strs)>1:
        if strs.pop()!=strs.pop(0): #같으면이라고 하면 하나라도 같으면 True가 됨
            return False

    return True

print(Palindrome('A man, a plan, a canal, Panama'))
print(Palindrome('race a car'))

### 데크 자료 이용 ###
# 속도 up
import collections

def isPalindrome(string:str)-> bool:
    strs=collections.deque()

    for char in string:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
        if strs.popleft()!=strs.pop():
            return False
    return True

print(isPalindrome('A man, a plan, a canal, Panama'))
print(isPalindrome('race a car'))


### 슬라이싱 이용 ###
# 속도 더 빨라짐
import re
def Palindrome_slice(string:str)-> bool:
    string=string.lower()
    string=re.sub("[^a-z0-9]",'',string) # 정규표현식 사용
    return string==string[::-1]


print(Palindrome_slice('A man, a plan, a canal, Panama'))
print(Palindrome_slice('race a car'))


############# Reverse String #############
# input : ['h','e','l','l','o'] -> output: ['o','l','l','e','h']

def myReverse(string:str)->str:
    mylist=[s for s in string] # list(string) 해도 됨
    return ''.join(mylist[::-1])


### 투 포인터 이용한 스왑
def reverseString(s) -> None:
    left,right =0,len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    #print(s) # 확인용


#print(reverseString(['h','e','l','l','o']))

### 파이썬 리스트 기능 이용 ###
def reverseString1(s): # input: list,
    fin=s.reverse() # reverse메소드는 원래 리스트를 바꾸기 때문에 return None이 된다.
    return fin

input_val=['h','e','l','l','o']
print(reverseString1(input_val))
print(input_val)


### 파이썬 문자열 슬라이싱 기능 이용 ###
def reverseString2(s:str):
    return s[::-1]
input_val2=['h','e','l','l','o']
print(reverseString2(input_val2))

############# Reorder Log files #############
def reorderLogFiles(logs:list)->list:
    letters,digits=[],[]
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 글자 정렬, 숫자는 입력그대로
    letters.sort(key=lambda x:(x.split()[1:],x.split()[0]))
    return letters+digits

input_val = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(input_val))


############# Most Common Word #############
# input1: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",
# input2: banned = ["hit"]
# output: "ball"

def mostCommonWord(paragraph:str, banned:list) -> str:
    words=[word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
    counts=collections.Counter(words)
    return counts.most_common(1)[0][0]

strings="Bob hit a ball, the hit BALL flew far after it was hit."

print(mostCommonWord(strings,banned=['hit']))


############# Group Anagrams #############
# input: ['eat','tea','tan','ate','nat','bat']
# output: [['ate','eat','tea'],['nat','tan'],['bat]]


def groupAnagrams(strs:list)->list:
    anagrams=collections.defaultdict(list)

    for word in strs:
        # 정렬해 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


strs=['eat','tea','tan','ate','nat','bat']

print(groupAnagrams(strs))


############# Longest Palindrome Substring #############
# input: "babad"
# output: "bab"

## 이해시키기
#s='193454381'
#s='bbbad'
#left=3
#right=5
# s[3]=s[5]=4  -> 조건 만족, 다음 루프

# left=2, right=6, s[2]=s[6]=3
# s[2:6] = 34543 -> 조건 만족 다음 루프

# left=1, right=7, s[1]=9, s[7]8 -> 조건 불만족
# left=1, right=7인 상태가 불만족이므로 최종 결과는 s[left+1:right]가 되어야함 -> 왜냐면 슬라이싱은 마지막 인덱스-1까지 출력
###

# 투 포인트가 특정 포인트 중심으로 확장하는 형태
def longestPalindrome(s:str)->str:
    # 제외하는 케이스 : 한글자 or 팰린드롬 그 자체
    if len(s)<2 or s==s[::-1]:
        return s

    # 팰린드롬 yes->  투포인트 확장
    def expand(left:int, right:int)-> str:
        while left>=0 and right<len(s) and s[left]==s[right]: # right=len(s)이면 확장불가능하니까 right<len(s)이어야함
            left-=1
            right+=1
        return s[left+1:right]

    # 우측이동 및 길이 가장 긴 팰린드롬 저장
    result=''
    for i in range(len(s)-1):
        # 왜 구간이 len(s)-1이냐면 3칸짜리 포인터가 가장 끝에 있을 때 -> i+2=len(s) 이기 때문임, i=len(s)-2이여야함, range(len(s)-1)은 len(s)-2까지 돌아감
        result=max(result,
                   expand(i,i+1),
                   expand(i,i+2),
                   key=len)
    return result

print(longestPalindrome('babad'))









