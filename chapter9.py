# Stack의 ADT(Abstract Data Type 구현): 연결 리스트로 구현하기
class Node:
    def __init__(self,item,next):
        self.item=item
        self.next=next

class Stack:
    def __init__(self):
        self.last=None

    def push(self,item): # 연결리스트에 요소 추가, 가장 마지막 값을 next로 이동 by 포인터 last 이동
        self.last=Node(item,self.last)

    def pop(self): # 가장 마지막 아이템을 끄집어 내고 last 포인터를 한칸 앞으로 전진하기
        item=self.last.item
        self.last=self.last.next
        return item

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

# 스택 값 출력 -> by pop
for _ in range(5):
    print(stack.pop())

print("=========ATD finished...!==========")

############# 20. Valid Parentheses #############
# input: (){}[]
# output: True
# (, {, [ 를 만나면 stack에 push 하고, ),},]를 만나면 stack에서 pop한다. => stack에서 다 나가면 True, 남아있는 게 있으면 False
# 따라서, )를 만나면 (를 pop해야하니까 dictionary로 연결해줌

def isValid(s:str)->bool:
    stack=[]
    table={')':'(',
           '}':'{',
           ']':'['}

    # 스택 이용해 예외 처리 및 일치여부 판별
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char]!=stack.pop():
            # not stack: stack에 append된 것이 없음,
            # table[char] != stack.pop() => (와 )는 바로 다음에 위치하기 때문에 (가 입력되고 바로 pop되야함
            # 즉, table[char]!=stack.pop() : 가장 최근에 stack에 들어 온 것이 table[char]가 아님.
            return False
    return len(stack)==0


print(isValid('()[]{}'))

############# 21. Remove Duplicate Letters #############
# 중복문자 제외후 사전식 순서로 나열
# input1: "bcabc"
# output1: abc
# input2: "cbacdcbc"
# output2: "acdb"
# input1에서 b,c는 중복되므로 위치 변경 가능 -> a뒤에 있는 bc가 살아남
# input2에서 c,b가 중복되므로 위치 변경 가능 -> b의 경우 a뒤에 있는 것이 살아나는데, c의 경우 a와 d사이에 있는 것이 살아남

# 재귀를 이용한 풀이 -> 이해 다시 하기: 시간 복잡도 O(N^2)
def removeDuplicatLetters(s:str)->str:
    # 집합으로 정렬
    for char in sorted(set(s)):
        suffix=s[s.index(char):] # 현재 char 포함 이후의 s원소 저장-> 이게 꼭 필요한 과정인가?
        # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        if set(s)==set(suffix): # 여기서 set(s)가 사용될때, 들어오는 순서는? -> 순서 상관 없음 ({'a','b','c'}={'c','b','a'})
            # 이 경우는 중복된 원소들을 모두 제거한 거임 -> 근데 사전식 정렬됨을 어떻게 보장할까?

            return char+removeDuplicatLetters(suffix.replace(char,''))
    return ''


s='bcabc'
print(removeDuplicatLetters(s))


# 스택 이용
# 스택 내 조회하는 연산 없는데 -1로 가장 최근 요소를 검색함 -> 변칙적 풀이
import collections
def removeDuplicateLetters(s:str)->str:
    counter, seen, stack = collections.Counter(s), set(),[]
    # seen의 의미는? -> 이미 처리된 문자인지 확인하기 위한 set 변수

    for char in s:
        counter[char]-=1
        if char in seen: # char이 seen에 저장되어 있으면 다음 루프 실행함 -> 이미 한번 검색했던 char임.
            continue
        # 뒤에 붙일 문자가 남아있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]]>0:
            # stack: 검색한 문자가 있어야 함
            # char < stack[-1]의 의미는? -> 사전식 순서임을 감안한 것임, 'b'<'c'이면 True
            # counter[stack[-1]]>0의 의미는?
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    return ''.join(stack)


print(removeDuplicateLetters('cbacdcbc'))


############# 22. Daily Temperatures #############
# input: t=[73,74,75,71,69,72,76,73]
# output: [1,1,4,2,1,1,0,0]
# 설명: 73도 보다 더 따뜻한 날은 하루만 기다리면 되고, 74도 보다 더 따뜻한 날은 하루,
# 75도는 4일 뒤 76, 71도는 2일 뒤 72도, 69도는 1일 뒤 72도, 72도는 1일 뒤 76도, 76도와 73도는 더 따뜻한 날 엇음

def dailyTemperatures(T:list)->list:
    answer=[0]*len(T)
    stack=[]
    for i, cur in enumerate(T):
        # 현재 온도가 스택값 보다 높다면 정답처리
        while stack and cur>T[stack[-1]]: # stack에 값이 있고, cur>T[stack[-1]]이면
            last=stack.pop() # 이전 온도(낮음)의 인덱스
            answer[last]=i-last # 이전 온도의 인덱스 = 현재 인덱스 - 이전 온도 인덱스
        stack.append(i) # stack에는 index를 저장함
    return answer

t=[73,74,75,71,69,72,76,73]
print(dailyTemperatures(t))


############# 23. Implement Stack using Queues #############
# 큐를 이용해 다음 연산 지원하는 스택 구현하기
# 보통 ADT할 때는 스택은 연결리스트로, 큐는 배열로 구현하는데 본 문제는 큐로 스택 구현
# python내 deque관련 함수: 입력함수 -> append(), appendleft() 출력함수 -> popleft(), pop()
# append(): 오른쪽에 값 입력, appendleft(): 왼쪽에 값 입력
# pop(): 오른쪽 값 출력, popleft(): 왼쪽 값 출력
# deque는 queue와는 다르게 출입구 양쪽에 모두 가짐 -> 스택과 큐의 기능 모두 가진 객치

# push(x): 요소 x를 스택에 삽입
# pop(): 스택의 첫번째 요소를 삭제
# top(): 스택의 첫번째 요소를 가져옴
# empty(): 스택이 비어있는지 여부 리턴

# MyStack stack = new MyStack():
# stack.pop(1)
# stack.push(2)
# stack.top() # 2리턴
# stack.pop() # 2리턴
# stack.empty() # false 리턴

class Mystack:
    def __init__(self):
        self.q=collections.deque()

    def push(self,x):
        self.q.append(x)
        # 요소 삽입 후 맨 처음으로 재 정렬
        for _ in range(len(self.q)-1): # q=[1,2,3,4,x] -> [x,1,2,3,4]
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q)==0

stack=Mystack()
stack.push(1)
stack.push(2)
print(stack.top()) # 2리턴
print(stack.pop()) # 2리턴
print(stack.empty()) # false 리턴


############# 24. Implement Queue using Stacks ############# -> 다시 생각!! peak함수 pop함수 서로 호출 -> 무한루프...??
# 스택을 이용해 큐 구현하기 -> stack 2개 이용
# push(x): 요소 x를 큐 마지막에 삽입
# pop(): 큐 처음에 있는 요소 제거
# peek(): 큐 처음 요소 조회
# empty(): 큐 비어있는 지 여부 리턴

class MyQue:
    def __init__(self):
        self.input=[]
        self.output=[]

    def push(self,x):
        self.input.append(x)

    def pop(self): # 처음 요소 제거
        self.peak() # peak 함수 호출
        return self.output.pop()

    def peak(self): # 처음 요소 조회
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input==[] and self.output==[]

# MyQueue queue = new MyQueue
# queue.push(1)
# queue.push(2)
# queue.peek() # 1리턴
# queue.pop() # 1리턴
# queeu.empty() # false리턴
print('Implement Queue')
queue=MyQue()
queue.push(1)
queue.push(2)
print(queue.peak()) # 1
print(queue.output) # [2,1]
print(queue.pop()) # 1
print(queue.output) # [2]
print(queue.empty()) # false

############# 25. Design Circular Queue #############
# MyCircularQueue CircularQueue = new MyCircularQueue(5)
# circularQueue.enQueue(10) # true 리턴
# circularQueue.enQueue(20) # true 리턴
# circularQueue.enQueue(30) # true 리턴
# circularQueue.enQueue(40) # true 리턴
# circularQueue.Rear() # 40
# circularQueue.isFull() # false
# circularQueue.deQueue() # true
# circularQueue.deQueue() # true
# circularQueue.enQueue(50) # true 리턴
# circularQueue.enQueue(60) # true 리턴
# circularQueue.Rear() # 60
# circularQueue.Front() # 30

class MyCircularQueue:
    def __init__(self,k:int):
        self.q=[None]*k
        self.maxlen=k
        self.p1=0 # front 포인터: 0 ~ (max-1)값 까지 갖는다.
        self.p2=0 # rear 포인터: 0 ~ (max-1)값 까지 갖는다.

    # enqueue(): rear 포인터 이동 -> p2에 값 넣고 p2 포인터 +1 해서 비어있는 공간 포인팅
    def enQueue(self,value:int)->bool:
        if self.q[self.p2] is None:
            self.q[self.p2]=value
            self.p2=(self.p2+1)%self.maxlen
            return True
        else:
            return False

    # dequeue(): front 포인터 이동
    def deQueue(self)-> bool:
        if self.q[self.p1] is None: # 비어있는 원형 큐는 false 반환
            return False
        else:
            self.q[self.p1] =None # 값 제거
            self.p1=(self.p1+1)%self.maxlen
            return True

    def Front(self)->int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self)->int:
        return -1 if self.q[self.p2-1] is None else self.q[self.p2-1]
        # p2는 현재 비어있는 값을 가르키므로 가장 마지막 원소를 추출하기 위해 p2-1을 해줌

    def isEmpty(self)->bool:
        return self.q[self.p1]==self.q[self.p2] and self.q[self.p1] is None # p1=p2=None

    def isFull(self)->bool:
        return self.p2==self.p1 and self.p1 is not None
        # 나는 self.p2==(slef.maxlen-1) 이라고 했는데 답에서는 self.p1==self.p2이라고 함
        # self.p2==(self.maxlen-1)라고 하면 [1,2,3,None]이라고 있는 경우, p2=3이 되므로 full이 아닌데 본 함수에서는 true 리턴함

print('------Circular Queue------')
CircularQueue=MyCircularQueue(5)
print(CircularQueue.enQueue(10))
print(CircularQueue.enQueue(20)) # true 리턴
print(CircularQueue.enQueue(30)) # true 리턴
print(CircularQueue.enQueue(40)) # true 리턴
print(CircularQueue.Rear()) # 40
print(CircularQueue.isFull()) # false
print(CircularQueue.deQueue()) # true
print(CircularQueue.deQueue()) # true
print(CircularQueue.enQueue(50)) # true 리턴
print(CircularQueue.enQueue(60) )# true 리턴
print(CircularQueue.Rear()) # 60
print(CircularQueue.Front()) # 30




