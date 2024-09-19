from random import random
from threading import Event, Thread, current_thread
from time import sleep


class CustomSemaphore:
    """
    Semaphore class to control the access to a shared resources.

    >>> semaphore = CustomSemaphore(2)
    >>> semaphore.permits
    2
    >>> event = Event()
    >>> semaphore.acquire(event, "Thread-1")
    Thread-1 has acquired a resource.
    >>> semaphore.acquire(event, "Thread-2")
    Thread-2 has acquired a resource.
    >>> semaphore.release()
    A resource has been released.
    >>> semaphore.release()
    A resource has been released.
    """

    def __init__(self, permits):
        self.permits = permits
        self.waiting_queue = []
        self.event_queue = []

    def acquire(self, event, thread_name):
        # Acquires a resource for a thread. If no resources are available,
        # the thread waits.
        self.permits -= 1
        if self.permits < 0:
            self.event_queue.append(event)
            self.waiting_queue.append(thread_name)
            print(f"{thread_name} is waiting for a resource.")
            event.wait()  # Thread waits until a resource is released
        else:
            print(f"{thread_name} has acquired a resource.")

    def release(self):
        # Releases a resource and signals a waiting thread, if any
        self.permits += 1
        if self.permits <= 0:
            event = self.event_queue.pop(0)
            self.waiting_queue.pop(0)
            event.set()  # Release the waiting thread
            print("A waiting thread has been released.")
        else:
            print("A resource has been released.")


class ThreadManager:
    """
    A class to manage the creation and execution of threads using the custom semaphore.
    >>> semaphore = CustomSemaphore(2)
    >>> manager = ThreadManager(semaphore, 2)
    >>> manager.start_threads()
    Thread-1 (thread_task) has acquired a resource.
    Thread 1 is working with the resource.
    Thread-2 (thread_task) has acquired a resource.
    Thread 2 is working with the resource.
    """

    def __init__(self, semaphore, thread_count):
        """
        Initializes the thread manager.

        Args:
            semaphore (CustomSemaphore): The semaphore object to control access.
            thread_count (int): The number of threads to create.
        """
        self.semaphore = semaphore
        self.thread_count = thread_count

    def start_threads(self):
        """
        Starts the specified number of threads.
        """
        for i in range(self.thread_count):
            thread = Thread(target=self.thread_task, args=(i + 1,))
            thread.start()

    def thread_task(self, thread_id):
        """
        Task executed by each thread: acquiring, using, and releasing the resource.

        Args:
            thread_id (int): The ID of the thread.
        """
        event = Event()
        thread_name = current_thread().name
        self.semaphore.acquire(event, thread_name)
        print(f"Thread {thread_id} is working with the resource.")
        sleep(2 + random())  # Simulate some work
        print(f"Thread {thread_id} has finished and is releasing the resource.")
        self.semaphore.release()


if __name__ == "__main__":
    resource_count = int(input("Enter the number of resources: "))
    thread_count = int(input("Enter the number of threads: "))

    semaphore = CustomSemaphore(resource_count)
    thread_manager = ThreadManager(semaphore, thread_count)

    thread_manager.start_threads()
