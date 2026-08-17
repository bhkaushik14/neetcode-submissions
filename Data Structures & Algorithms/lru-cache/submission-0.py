class LRUCache:
    def __init__(self, capacity: int):
        self.access = {}
        self.capacity = capacity

        self.left = Node(0, 0)   # LRU dummy
        self.right = Node(0, 0)  # MRU dummy

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.access:
            return -1

        node = self.access[key]

        # Move accessed node to MRU position
        self.removeNode(node)
        self.insertBefore(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.access:
            node = self.access[key]
            node.val = value

            # Move updated node to MRU position
            self.removeNode(node)
            self.insertBefore(node)
            return

        # Cache is full, remove LRU node
        if len(self.access) == self.capacity:
            lru = self.left.next
            self.removeNode(lru)
            self.access.pop(lru.key)

        # Add new node as MRU
        node = Node(key, value)
        self.access[key] = node
        self.insertBefore(node)

    def insertBefore(self, node):
        left = self.right.prev

        node.prev = left
        node.next = self.right

        left.next = node
        self.right.prev = node

    def removeNode(self, node):
        left = node.prev
        right = node.next

        left.next = right
        right.prev = left


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None