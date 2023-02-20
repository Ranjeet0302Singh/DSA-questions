class MyHashSet:

    def __init__(self):
        self.headSet = set([])

    def add(self, key: int) -> None:
        self.headSet.add(key)

    def remove(self, key: int) -> None:
        if key in self.headSet:
            self.headSet.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.headSet:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)