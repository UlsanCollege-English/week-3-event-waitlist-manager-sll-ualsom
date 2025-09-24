class _Node:
    __slots__ = ("name", "next")
    def __init__(self, name, next=None):
        self.name = name
        self.next = next

class Waitlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        """Return number of people on the waitlist."""
        return self._size

    def to_list(self):
        """Return names from head to tail as a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.name)
            current = current.next
        return result

    def join(self, name):
        """Append name at the tail (O(1))."""
        new_node = _Node(name)
        if not self.head:
            # Empty list
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def find(self, name):
        """Return True if name exists, else False."""
        current = self.head
        while current:
            if current.name == name:
                return True
            current = current.next
        return False

    def cancel(self, name):
        """Remove first occurrence; return True if removed."""
        prev = None
        current = self.head
        while current:
            if current.name == name:
                if prev:
                    prev.next = current.next
                else:
                    # Removing head
                    self.head = current.next
                # If tail is removed, update tail
                if current == self.tail:
                    self.tail = prev
                self._size -= 1
                return True
            prev = current
            current = current.next
        return False

    def bump(self, name):
        """Move first occurrence to the head; return True if moved."""
        if not self.head or self.head.name == name:
            # Already at head or empty list
            return False

        prev = None
        current = self.head
        while current:
            if current.name == name:
                # Remove current from its position
                if prev:
                    prev.next = current.next
                # If current is tail, update tail
                if current == self.tail:
                    self.tail = prev
                # Insert current at head
                current.next = self.head
                self.head = current
                return True
            prev = current
            current = current.next
        return False
