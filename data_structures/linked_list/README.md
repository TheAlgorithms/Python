<h1> Linked List </h1>

<h3> Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers.</h3>

![image](https://user-images.githubusercontent.com/91491296/135705938-ba59da5f-b681-4eff-913d-f544402c1507.png)

<h4>Why Linked List?</h4> <br>
Arrays can be used to store linear data of similar types, but arrays have the following limitations. <br>
1) The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage. <br>
2) Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted. <br>
For example, in a system, if we maintain a sorted list of IDs in an array id[]. <br>
id[] = [1000, 1010, 1050, 2000, 2040]. <br><br>
And if we want to insert a new ID 1005, then to maintain the sorted order, we have to move all the elements after 1000 (excluding 1000). <br>
Deletion is also expensive with arrays until unless some special techniques are used. For example, to delete 1010 in id[], everything after 1010 has to be moved.<br>
Advantages over arrays <br>
1) Dynamic size <br>
2) Ease of insertion/deletion<br>
Drawbacks: <br>
1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation. Read about it here.<br> 
2) Extra memory space for a pointer is required with each element of the list. <br>
3) Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.<br>
Representation: <br><br>
A linked list is represented by a pointer to the first node of the linked list. The first node is called the head. If the linked list is empty, then the value of the head is NULL. <br>
Each node in a list consists of at least two parts: <br>
1) data <br>
2) Pointer (Or Reference) to the next node <br>
<br><br><br>
<h2>Linked List (Inserting a node)</h2>

methods to insert a new node in linked list are discussed. A node can be added in three ways 
1) At the front of the linked list 
2) After a given node. 
3) At the end of the linked list.

<br>
<br>
<br>
Add a node at the front: (4 steps process) <br>
The new node is always added before the head of the given Linked List. And newly added node becomes the new head of the Linked List. <br>
For example, if the given Linked List is 10->15->20->25 and we add an item 5 at the front, then the Linked List becomes 5->10->15->20->25. <br>
Let us call the function that adds at the front of the list is push(). The push() must receive a pointer to the head pointer, because push must change the head pointer to point to the new node<br>
<br> <br> <br><br><br>
Add a node after a given node: (5 steps process) <br><br
We are given a pointer to a node, and the new node is inserted after the given node.<br>
![image](https://user-images.githubusercontent.com/91491296/135706113-91b7b772-aee5-42cf-ab58-5d1d1aa9504d.png)<br>
<br>
Time complexity of insertAfter() is O(1) as it does a constant amount of work.<br><br><br>

Add a node at the end: (6 steps process) <br>
The new node is always added after the last node of the given Linked List. For example if the given Linked List is 5->10->15->20->25 and we add an item 30 at the end, then the Linked List becomes 5->10->15->20->25->30.<br><br> 
Since a Linked List is typically represented by the head of it, we have to traverse the list till the end and then change the next to last node to a new node.<br>
Time complexity of append is O(n) where n is the number of nodes in linked list. Since there is a loop from head to end, the function does O(n) work. <br>
This method can also be optimized to work in O(1) by keeping an extra pointer to the tail of linked list/<br>
