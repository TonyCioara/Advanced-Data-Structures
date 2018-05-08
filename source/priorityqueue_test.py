#!python

from priorityqueue import PriorityQueue
import unittest


class QueueTest(unittest.TestCase):

    def test_init(self):
        q = PriorityQueue()
        assert q.front() is None
        assert q.length() == 0
        assert q.is_empty() is True

    def test_init_with_list(self):
        q = PriorityQueue()
        q.enqueue('B', 3)
        q.enqueue('C', 5)
        q.enqueue('A', 1)
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_length(self):
        q = PriorityQueue()
        assert q.length() == 0
        q.enqueue('A', 5)
        assert q.length() == 1
        q.enqueue('B', 1)
        assert q.length() == 2
        q.dequeue()
        assert q.length() == 1
        q.dequeue()
        assert q.length() == 0

    def test_enqueue(self):
        q = PriorityQueue()
        q.enqueue('A', 3)
        assert q.front() == 'A'
        assert q.length() == 1
        q.enqueue('B', 1)
        assert q.front() == 'B'
        assert q.length() == 2
        q.enqueue('C', 4)
        assert q.front() == 'B'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_front(self):
        q = PriorityQueue()
        assert q.front() is None
        q.enqueue('A', 6)
        assert q.front() == 'A'
        q.enqueue('B', 10)
        assert q.front() == 'A'
        q.dequeue()
        assert q.front() == 'B'
        q.dequeue()
        assert q.front() is None

    def test_dequeue(self):
        q = PriorityQueue()
        q.enqueue('A', 1)
        q.enqueue('B', 2)
        q.enqueue('C', 3)
        assert q.dequeue() == 'A'
        assert q.length() == 2
        assert q.dequeue() == 'B'
        assert q.length() == 1
        assert q.dequeue() == 'C'
        assert q.length() == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.dequeue()


if __name__ == '__main__':
    unittest.main()
