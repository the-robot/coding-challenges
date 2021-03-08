# https://leetcode.com/problems/design-hashmap/

"""
Topic: Data Structure
"""

class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000001
        self.nodes = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.nodes[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        val = self.nodes[key]
        return val if val != None else -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.nodes[key] = None
