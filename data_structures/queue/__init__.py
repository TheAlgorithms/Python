"""
Implementation of Queue using python lists
Queue is a data which in which data can be added from one end and removed from 
the other end.
Follows first in first out principal (FIFO)
"""

class queue:
  def __init__(self,val=[]):
    if type(val)==list:
      self.vals=val
    else:
      self.vals=[val]
  
  def __str__(self) -> str:
    '''
    Prints all the values in the queue as a list
    >>> q = queue()
    >>> print(q)
    []

    >>> q.enqueue('A')
    >>> print(q)
    ['A']

    >>> q.enqueue('B')
    >>> print(q)
    ['B','A']
    '''
    return str(self.vals)

  def isEmpty(self) -> bool:
    '''
    Returns wether the list is empty or not
    >>> q = queue()
    >>> print(q)
    []
    >>> q.isEmpty()
    True

    >>> q.enqueue('A')
    >>> print(q)
    ['A']
    >>> q.isEmpty()
    False

    >>> q.dequeue()
    'A'
    >>> q.isEmpty()
    True
    '''
    return self.vals==[]

  def enqueue(self,val):
    '''
    Add elements to the front of the queue
    >>> q = queue()
    >>> print(q)
    []

    >>> q.enqueue('A')
    >>> print(q)
    ['A']

    >>> q.enqueue('B')
    >>> print(q)
    ['B','A']
    '''
    self.vals.insert(0,val)
  
  def dequeue(self):

    '''
    Removes the oldest element present in the queue and returns the element
    >>> q = queue()
    >>> print(q)
    []

    >>> q = dequeue()
    Traceback (most recent call last):
    ...
    Exception: Queue is empty

    >>> q.enqueue('A')
    >>> print(q)
    ['A']

    >>> q.enqueue('B')
    >>> print(q)
    ['B','A']

    >>> q.dequeue()
    'A'

    >>> print(q)
    ['B']
    '''

    if len(q)==0:
      raise Exception("Queue is empty")
    return self.vals.pop()

  def __len__(self) -> int:

    """
    Returns length of the queue
    >>> q = queue()
    >>> len(q)
    0
    >>> q.enqueue("A")
    >>> len(q)
    1
    """

    return len(self.vals)
