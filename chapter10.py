############# 26. Design Circular Deque #############
# 이중 연결 리스트 사용

# MyCircularDequeue(k): 데크 사이즈 k로 지정하는 생성자
# insertFront(): 데크 처음에 아이템 추가, 성공할 경우 true리턴
# insertLast(): 데크 마지막에 아이템 추가, 성공할 경우 true리턴
# deleteFront(): 데크 처음에 아이템 삭제, 성공할 경우 true리턴
# deleteLast(): 데크 마지막에 아이템 삭제, 성공할 경우 true리턴
# getFront(): 데크 첫번째 아이템 가져옴, 비어있으면 -1 리턴
# getRear(): 마지막 아이템 가져옴, 비어있으면 -1 리턴
# isEmpty(): 데크가 비어있는지 여부 판별
# isFull(): 데크 가득차 있는 지 여부 판별


class ListNode:
    def __init__(self,val=0, next=None):
        self.val=val
        self.next=None


class MyCircularDeque: # 이해 안 됨 -> 다시 생각해 볼 것!!!!!
    # 책에서는 right, left로 되어 있지만 이해를 위해 prev, next로 바꿔서 쓰자
    def __init__(self,k:int):
        self.head, self.tail=ListNode(None), ListNode(None)
        self.k, self.len= k, 0
        self.head.prev, self.tail.next = self.tail, self.head
        # 이중 연결 리스트는 처음과 끝이 정해저 있지만,"원형"데크는 처음과 끝이 정해져 있지 않으므로 head의 이전값은 tail이고 tail이 다음 값은 head라고 연결해줌

    # 이중 연결리스트에 신규 노드 삽입
    def _add(self,node:ListNode, new:ListNode)->ListNode: # new-> node로 삽입함
        n=node.prev
        node.prev=new # 윗줄이랑 이 줄이랑 합쳐서 걍 node.prev=new하면 안되나? 왜 굳이 n이라는 변수를 등장시켰지?
        new.next , new.prev = node, n
        n.next=new

    def _del(self,node:ListNode):
        n=node.prev.prev
        node.prev=n
        n.next=node

    def insertFront(self,value:int)->bool:
        if self.len==self.k:
            return False
        self.len+=1
        self._add(self.head,ListNode(value))
        return True

    def insertLast(self,value:int)-> bool:
        if self.len==self.k:
            return False
        self.len+=1
        self._add(self.tail.next, ListNode(value))
        return True

    def deleteFront(self)->bool:
        if self.len==0:
            return False
        self.len-=1
        self._del(self.head)
        return True

    def deleteLast(self)->bool:
        if self.len==0:
            return False
        self.len-=1
        self._del(self.tail.next.next)
        return True

    def getFront(self)->int:
        return self.head.prev.val if self.len else -1

    def getRear(self)-> int:
        return self.tail.next.val if self.len else -1

    def isEmpty(self)->bool: # 이해 완료
        return self.len==0

    def isFull(self)->bool: # 이해 완료
        return self.len==self.k


test=MyCircularDeque(5)
print(test.insertFront(1))
print(test.insertLast(2))



############# 27. Merge k Sorted Lists  #############-> 여기서 부터 시작하기! 아이고 졸리다
# input: k=3. [1->4-> 5, 1->3->4, 2->6]
# output: 1->1->2->4->4->5->6
# 우선 순위 큐 이용
# 우선순위 큐는 힙 자료구조와 관련이 깊음 -> 힙 자료구조 이해해보자! : 태블릿에 정리함
# 참고 자료: https://littlefoxdiary.tistory.com/3
# 힙 자료 구조 예제
import heapq
# h = []
# heapq.heappush(h, (5, 'write code')) # heappush(list, value) 형태인데, 이 때 value는 튜플 형식 일 수 있다.
# heapq.heappush(h, (7, 'release product'))
# heapq.heappush(h, (1, 'write spec'))
# heapq.heappush(h, (3, 'create tests'))
# print(h) # [(1,'writhe spec'),(3, 'create tests'),(5,'write code'),(7,'release product')] 출력됨


def mergeKLists(lists:list)->ListNode:
    root=result=ListNode(None)
    heap=[]

    # 각 연결리스트의 루트를 힙에 저장함
    for i in range(len(lists)): # k값 만큼 돌기
        #if lists[i]: # 이 조건이 꼭 필요한가? 당연한거 아닌가? -> 책에서는 이 제어문 있는데 없어도 괜찮다고 판단해서 주석 처리
        # 왜냐면 루프문이 lists개수만 큼 도는데 이는 당연히 list에 원소가 있는 만큼 도는 거니까!!
        heapq.heappush(heap, (lists[i].val, i, lists[i])) # heap=[(1,0,1->4->5), (1,1, 1->3->5), (2,2, 2->6)]

    # 힙 추출 이후 다음노드는 다시 저장
    while heap:
        node=heapq.heappop(heap)
        idx=node[1]
        result.next=node[2]

        result=result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))

    return root.next



    

k=3
one=ListNode(1)
one.next=ListNode(4)
one.next.next=ListNode(5)

two=ListNode(1)
two.next=ListNode(3)
two.next.next=ListNode(4)

three=ListNode(2)
three.next=ListNode(6)

output=[one, two, three]
print(output) # output=[1->4->5, 1->3->4, 2->6]
# heapq.heappush(heap, (lists[i].val, i, lists[i]))


# t=mergeKLists(output)
# print(t.val)
# print(t.next.val)
# print(t.next.next.val)

print('-------------------------')
h=[]
heapq.heappush(h, (5, 'write code')) # heappush(list, value) 형태인데, 이 때 value는 튜플 형식 일 수 있다.
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
print(h) # [(1,'writhe spec'),(3, 'create tests'),(5,'write code'),(7,'release product')] 출력됨
heapq.heappop(h)
print(h)



