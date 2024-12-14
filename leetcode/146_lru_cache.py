class ListNode:
    def __init__(self, key: int, value: int, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.nodes = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1, self.head)
        self.head.right = self.tail
    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self.remove(node)
        self.append(node)
        return node.value
    def put(self, key: int, value: int) -> None:
        if key in self.nodes: #replacing an old key/value
            node = self.nodes[key] #get the node from the dictionary
            node.value = value #update its value
            self.remove(node) #remove the node from the linked list
        else:
            if self.count == self.capacity: #inserting a new key when the cache is full
                node = self.nodes.pop(self.head.right.key) #delete its key from the dictionary
                node.key = key #replace its key and value with the new ones being inserted
                node.value = value
                self.remove(node) #remove it from the linked list
            else: #inserting a new key when the cache is not full
                node = ListNode(key, value) #create a new node and set its key and value
            self.nodes[key] = node #update the dictionary to point to the new node
        self.append(node) #insert the node at the end of the linked list
    def append(self, node: ListNode):
        node.left = self.tail.left
        node.left.right = node
        self.tail.left = node
        node.right = self.tail
        self.count += 1
    def remove(self, node: ListNode):
        node.left.right = node.right
        node.right.left = node.left
        self.count -= 1
