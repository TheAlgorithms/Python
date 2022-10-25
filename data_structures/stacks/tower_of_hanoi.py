 # @tower_of_hanoi.py
 # @reference:https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
 # @details:
 # The Tower of Hanoi is the problem in which there are 3 towers,let’s mark it with the names Tower A, Tower B, and Tower C.
 # And in Tower A, we have n number of disks.
 # The task is to move all disks from Tower A to Tower C using Tower B.
 # We solve this problem using RECURSION(a func. which calls itself).
 # @algorithm:
 # For any n number of disks, firstly the n-1 disk will be moved from source to auxiliary.
 # Then the nth disk will be moved from the source tower to the destination tower.
 # And then last, the n-1 disk will be moved from the auxiliary tower to the destination tower.
 # And these n-1 moves are called recursively such that
 # individual function call is responsible to handle the 1 disk move in each call.
 # @author [Ankit Akash](https://github.com/ankit-akash)
 


def TOH(source, auxiliary, destination, numOfDisk):
 #Base case of Recursion that when there is no disk to move 
 #then terminate the call.

  if numOfDisk > 0:
 #Recursively calling for moving the n-1 disk from source
 #to auxiliary using destination. 
 
TOH(source, destination, auxiliary, numOfDisk-1)
#Moving the disk from source to destination

print(“Move 1 disk from {0} to {1} using {2}.”.format(source, destination, auxiliary)) 
 #Recursively asking to move remaining disk from 
 #auxiliary to destination using source.
 
  TOH(auxiliary, source, destination, numOfDisk-1)
if __name__ == “__main__”:
 numOfDisk = int(input())
 
  TOH(‘A’, ‘B’, ‘C’, numOfDisk)
