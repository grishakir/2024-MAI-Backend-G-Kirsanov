class LRUCache:
    def __init__(self, capacity: int =10) -> None:
        self.capacity = capacity
        self.size = 0
        self.d = {}
        pass

    def get(self, key: str) -> str:
        if key in self.d:
            self.d[key] = self.d[key]
            return self.d[key]
        else:
            return ""

    def set(self, key: str, value: str) -> None:
        if self.size + 1 < self.capacity:
            self.d[key] = value
            self.size += 1
        else:
            self.d.popitem()
            self.d[key] = value
        pass

    def rem(self, key: str) -> None:
        if key in self.d:
            self.d.pop(key)
            self.size -= 1
