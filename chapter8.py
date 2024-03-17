############# Palindrome Linked List #############
# input1: 1-> 2
# output1: false
# input2: 1-> 2-> 2-> 1
# output2: True

class ListNode: #ListNode라는 자료 구조 지정
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head:ListNode)-> bool:
    #q:list=[]
    q=[]
    if not head:
        return True
    node=head
    #리스트 변환
    while node is not None:
        q.append(node.val)
        node=node.next

    # 팰린드론 판별
    while len(q)>1:
        if q.pop(0)!=q.pop():
            return False
    return True

one=ListNode(1)
two=ListNode(2)
three=ListNode(2)
four=ListNode(1)

one.next=two
two.next=three
three.next=four
four.next=None

print(isPalindrome(one))


# 데크 사용
import collections

def isPalindrome(one:ListNode)-> bool:
    if not one:
        return True # input값이 none이면 true반환

    d=collections.deque()
    node=one # 약간 copy느낌!!

    while node:
        d.append(node.val)
        node=node.next

    # palindrome 검사
    while len(d)>1:
        if d.pop()!=d.popleft():
            return False
    return True

print(isPalindrome(one))

# 런너를 이용한 풀이
def isPalindrome(head:ListNode)-> bool:
    rev = None
    slow = fast = head #init Runner

    # 러너이용해 역순 연결 리스트 구성
    while fast and fast.next: # 종료조건 fast가 fasle이거나 fast.next가 false일때
        # 지속조건: fast가 존재하고 fast.next가 존재할 때
        # <=>종료조건: fast가 false이거나 fast.next가 false일 때
        # fast가 false일 때에는 짝수일 때-> 4번까지 진행되고 fast는 없음,
        # fast.next가 false일때에는 홀수개 일때
        print(f'fast:{fast.val}')
        print(f'slow:{slow.val}')
        fast=fast.next.next
        rev,rev.next,slow= slow, rev,  slow.next

    if fast: # fast.next가 false이고 fast는 true
        print(f'fast:{fast.val}')
        print(f'slow:{slow.val}')
        print('If fast is implecated...!')
        slow=slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val ==slow.val:
        slow,rev=slow.next, rev.next
    return not rev

#####
print('-----짝수------')
one1=ListNode(1)
two1=ListNode(2)
three1=ListNode(2)
four1=ListNode(1)


one1.next=two1
two1.next=three1
three1.next=four1
four1.next=None
print(isPalindrome(one))


print('------홀수------')
one1=ListNode(1)
two1=ListNode(2)
three1=ListNode(3)
four1=ListNode(2)
five1=ListNode(1)


one1.next=two1
two1.next=three1
three1.next=four1
four1.next=five1
five1.next=None
print(isPalindrome(one))

############# Merge Two sorted Lists #############
# input: 1->2->4, 1->3->4 두 정렬된 리스트 합치기 -> 정렬된 형태로!
# output: 1->1->2->3->4->4,

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next


def mergeTwoLists(l1:ListNode, l2:ListNode)-> ListNode:
    if (not l1) or (l2 and l1.val > l2.val): # not l1 -> not l1이 참이면 -> l1이 거짓이면 -> l1이 Null이면
        # (l1이 거짓) 이거나 (l2가 참이고, l1의 값> l2의 값)이면
        l1,l2=l2,l1 # 작은 값이 l1에 할당
    if l1: # l1이 참이면
        l1.next=mergeTwoLists(l1.next,l2)
    return l1

one=ListNode(1)
one.next=ListNode(2)
one.next.next=ListNode(3)
one.next.next.next=ListNode(5)

two=ListNode(1)
two.next=ListNode(3)
two.next.next=ListNode(4)

rst=mergeTwoLists(one,two)
while rst:
    print(rst.val)
    rst=rst.next


############# Reverse Linked List #############
# input: 1-> 2-> 3-> 4-> 5-> NULL
# output: 5-> 4-> 3-> 2-> 1-> NULL

# 재귀구조 뒤집기
def reverseList(head:ListNode)-> ListNode:
    def reverse(node:ListNode, prev: ListNode=None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    return reverse(head)


# 반복구조 뒤집기
def reverseList(head:ListNode)-> ListNode:
    node, prev = head, None # init 해줌
    # node=1,2,3,N
    while node:
        next, node.next= node.next, prev
        # 1. next에는 2,3,N node.next는 n
        # 2. next에는 3,n node.next는 1,n
        # 3. next에는 n node.next에는 2,1,n

        prev, node = node, next
        # 1. prev에는 1,n node에는 2,3,n
        # 2. prev에는 2,1,n node에는 3,n
        # 3. prev에는 3,2,1,n node에는 n

    return prev

############# Add Two Numbers #############
# input (2->4->3) + (5->6->4)
# output (7->0->8)

# 자료형 변환
class solution:
    # 연결 리스트 뒤집기
    def reverseList(self, node: ListNode)-> ListNode:
        node, prev = node.next, node #약간 하노이 탑 느낌: node -> prev로 가는데, next를 임시변수로 이용
        while node:
            next, node.next = node.next, prev
            prev, node= node, next
        return prev

    # 연결 리스트 -> 리스트
    def toList(self, node:ListNode)-> list:
        list=[]
        while node:
            list.append(node.val)
            node=node.next
        return list

    # 리스트 -> 연결 리스트
    def toReversedLinkedList(self,result:str)-> ListNode:
        prev: ListNode = None
        for r in result:
            node=ListNode(r) # node에는 한자리의 숫자 들어감
            node.next=prev # node.next에는 prev
            prev=node
        return node

    # 두 연결리스트의 덧셈
    def addTwoNumbers(self, l1:ListNode, l2:ListNode)-> ListNode:
        a=self.toList(self.reverseList(l1))
        b=self.toList(self.reverseList(l2))

        resultStr=int(''.join(str(e) for e in a))+ int(''.join(str(e) for e in b))

        return self.toReversedLinkedList(str(resultStr))

one=ListNode(2)
one.next=ListNode(4)
one.next.next=ListNode(3)
one.next.next.next=None

two=ListNode(5)
two.next=ListNode(6)
two.next.next=ListNode(4)
two.next.next.next=None
#print(solution().addTwoNumbers(one,two)) # class는 이렇게 사용한다!!!
# 메모리 에러 뜸


# 계산 원리로 구현
def addTwoNumbers2(l1:ListNode,l2:ListNode)->ListNode:
    root=head=ListNode(0) # python 다중할당기능 이용
    carry=0
    while l1 or l2 or carry:
        sum=0
        # 두 입력값의 합 계산
        if l1:
            sum+=l1.val
            l1=l1.next # l1의 포인터 이동
        if l2:
            sum+=l2.val
            l2=l2.next # l2의 포인터 이동

        # 몫과 나머지 계산
        carry, val = divmod(sum+carry, 10 ) # sum+carry / 10을 (몫, 나머지)형태로 반환
        head.next=ListNode(val)
        head=head.next # head의 포인터 이동
    return root.next


one=ListNode(2)
one.next=ListNode(4)
one.next.next=ListNode(3)
one.next.next.next=None

two=ListNode(5)
two.next=ListNode(6)
two.next.next=ListNode(4)
two.next.next.next=None

print(addTwoNumbers2(one,two).next.next.val)

############# Add Two Numbers #############
# input: 1->2->3->4
# output: 2->1->4->3 , pair단위로 swap하기

# 변칙적 방법
def swapPairs(head:ListNode)->ListNode:
    cur=head
    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur=cur.next.next
    return head # cur로 할 경우, cur.next가 none일 경우 cur.next.val 할당오류 남

one=ListNode(1)
one.next=ListNode(2)
one.next.next=ListNode(3)
one.next.next.next=ListNode(4)
one.next.next.next.next=None
#one.next.next.next.next.next=ListNode(6)
#one.next.next.next.next.next.next=None


rst=swapPairs(one)
print(rst.val) # 2
print(rst.next.val) # 1
# 참고) print(swapPairs(one).val), print(swapPairs(one).next.val)하면 1,1 나옴
# 객체를 먼저 만들어주고 시행해야함

# 반복구조로 스왑 -> 이해 다시하기
def swapPairs(head:ListNode)-> ListNode:
    root=prev=ListNode(None)
    prev.next=head
    # 이 때, root=prev이기 때문에 root.next=head가 됨.
    while head and head.next:
        # b(임시버퍼)가 head가르키도록 할당
        b=head.next # b의 첫번째 원소는 head의 짝수차항부터 저장함
        head.next=b.next # head의 2번째 원소는 b의 2번째 항부터! 그니까 원래 head의 3번째 항부터~
        # 즉, 새로운 head=h1->h3->h4...
        b.next=head # b=h2-> h1

        # prev가 b를 가르키도록 할당
        prev.next=b # prev: None-> 2->1

        # 다음번 비교를 위해 이동
        head=head.next # head: 3->4
        prev=prev.next.next # prev: 1-> 여기서 root는 바뀌지 않나?
        # 여기서는 prev 자체를 지정하는 것이기 때문에 prev에 따라 root가 바뀌지 않는다.
    return root.next

one=ListNode(1)
one.next=ListNode(2)
one.next.next=ListNode(3)
one.next.next.next=ListNode(4)
one.next.next.next.next=None
print('-------')
t=swapPairs(one)
print(t.val)
print(t.next.val)
print(t.next.next.val)
print(t.next.next.next.val)

# 재귀구조로 스왑
def swapPairs(head:ListNode)->ListNode:
    if head and head.next:
        p=head.next #p: h2->h3->h4

        # 스왑값 리턴
        head.next=swapPairs(p.next) # head: h1-> swapPairs(h3->h4)
        p.next=head # p: h2-> h1->swapPairs(h3->h4)
        return p

    # head가 없거나 head.next가 없으면 (홀수개가 남거나 아무것도 안남으면)
    return head
    # swapPairs(h3->h4) : p:h4, head: h3-> N, p: h4-> h3-> N


print('------------')
one=ListNode(1)
one.next=ListNode(2)
one.next.next=ListNode(3)
one.next.next.next=ListNode(4)
one.next.next.next.next=None
t=swapPairs(one)

print(t.val)#2
print(t.next.val) # 1
print(t.next.next.val) #4
print(t.next.next.next.val) #3

############# Odd Even Linked List #############
# 연결리스트를 홀수노드 다음에 짝수노드가 오도록 재구성, 공간복잡도 O(1), 시간복잡도 O(n)
# input1: 1->2->3->4->5->N
# output1: 1,3,5,2,4,N
# input2: 2,1,3,5,6,4,7,N
# output2: 2,3,6,7,1,5,4,N

def oddEvenList(head:ListNode)->ListNode:
    # 예외처리
    if not head:
        return None

    odd=head
    even=head.next
    even_head=head.next # 이 공간들은 입력 데이터 개수 n에 대해 변하지 않으므로 공간복잡도 O(1)임.

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    # 홀수 노드의 마지막을 짝수 헤드로 연결
    odd.next=even_head
    return head

one=ListNode(1)
one.next=ListNode(2)
one.next.next=ListNode(3)
one.next.next.next=ListNode(4)
one.next.next.next.next=ListNode(5)
rst=oddEvenList(one)
print('--------------')
print(rst.val)
print(rst.next.val)
print(rst.next.next.val)
print(rst.next.next.next.val)
print(rst.next.next.next.next.val)

############# Reverse Linked List2 #############
# input: 1->2->3->4->5->None, m=2, n=4
# output: 1->4->3->2->5->None
# 인덱스 m에서 n까지 역순으로 만들기, 인덱스 m은 1부터 시작함
def reverseBetween(head:ListNode, m:int, n:int)->ListNode:
    # 예외 처리
    if not head or m==n:
        return head
    root=start=ListNode(None)
    root.next=head

    # start, end 지정
    for _ in range(m-1):
        start=start.next
    end=start.next

    # 반복하면서 노드 차례로 뒤집기
    for _ in range(n-m):
        tmp, start.next, end.next=start.next, end.next, end.next.next
        start.next.next=tmp
    return root.next

one=ListNode(1)
one.next=ListNode(2)
one.next.next=ListNode(3)
one.next.next.next=ListNode(4)
one.next.next.next.next=ListNode(5)
one.next.next.next.next.next=None

t=reverseBetween(one,m=2,n=4)
print()
print(t.val)
print(t.next.val)
print(t.next.next.val)
print(t.next.next.next.val)
print(t.next.next.next.next.val)




