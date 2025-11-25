from typing import Any, List, Optional

class Stack:
    def __init__(self, items: Optional[List[Any]] = None, limit: int = 100) -> None:
        if items is None:
            self.items: List[Any] = []
        else:
            self.items = list(items)
        self.limit: int = limit

    def isEmpty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: Any) -> None:
        if self.full():
            raise OverflowError("Stack is full")
        self.items.append(item)

    def pop(self) -> Optional[Any]:
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self) -> Optional[Any]:
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def size(self) -> int:
        return len(self.items)

    def full(self) -> bool:
        return len(self.items) >= self.limit

    def search(self, target: Any) -> int:
        # Return distance from top (0-based) if target found, else -1
        # Top is self.items[-1]
        try:
            index = self.items[::-1].index(target)
            return index
        except ValueError:
            return -1
