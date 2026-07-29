class ListNode:
    def __init__(self, val=[], next=None):
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.head = None

    def put(self, key: int, value: int) -> None:
        if not self.head:
            self.head = ListNode([key, value])  
            return
        
        temp = self.head
        if self.get(key) == -1:
            while temp.next:
                temp = temp.next
            
            temp.next = ListNode([key, value])
            return
        
        while temp.val[0] != key:
            temp = temp.next
        
        temp.val[1] = value
        return
        

    def get(self, key: int) -> int:
        temp = self.head
        while temp:
            if temp.val[0] == key:
                return temp.val[1]
            temp = temp.next
        
        return -1


    def remove(self, key: int) -> None:
        if self.get(key) == -1:
            return
        
        if self.head.val[0] == key:
            self.head = self.head.next
            return
        
        temp = self.head
        while temp.next.val[0] != key:
            temp = temp.next
        
        temp.next = temp.next.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)