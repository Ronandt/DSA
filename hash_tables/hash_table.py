#Hashcode wioll be e.g 0-10000 (For our keys), This will be our hash
#Since our hash table will only have 10 elements
#You would mod 10 (the capacity) for example
#If there's a collison the hashtable for each index will be a linked list (Add another address ) (We will search until there's the correct key )
from typing import Any
class HashMap:
    def __init__(self) -> None:
        self.size = 100000
        self.bucket = [None] * self.size
    def _hash(self, key: int) -> int:
        return hash(key) % self.size
    def __setitem__(self, key: int, value: Any) -> None:
        self.bucket[self._hash(key)] = value
    def __getitem__(self, key: int) -> Any:
        return self.bucket[self._hash(key)]
    def __delitem__(self, key: int) -> None:
        self.bucket[self._hash(key)] = None