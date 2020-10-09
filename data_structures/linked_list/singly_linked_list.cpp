// Linked list operations in C++

#include <stdlib.h>
#include <iostream>

using namespace std;

// Create a node
struct Node
{
    int item;
    struct Node *next;
};

void insertAtBeginning(struct Node **ref, int data)
{

    // Allocate memory to a node
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));

    // insert the item
    new_node->item = data;
    new_node->next = (*ref);

    // Move head to new node
    (*ref) = new_node;
}
// Insert a node after a node
void insertAfter(struct Node *prev_node, int data)
{
    if (prev_node == NULL)
    {
        cout << "the given previous node cannot be NULL";
        return;
    }

    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->item = data;
    new_node->next = prev_node->next;
    prev_node->next = new_node;
}

void insertAtEnd(struct Node **ref, int data)
{
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    struct Node *last = *ref;

    new_node->item = data;
    new_node->next = NULL;

    if (*ref == NULL)
    {
        *ref = new_node;
        return;
    }

    while (last->next != NULL)
        last = last->next;

    last->next = new_node;
    return;
}
void deleteNode(struct Node **ref, int key)
{
    struct Node *temp = *ref, *prev;

    if (temp != NULL && temp->item == key)
    {
        *ref = temp->next;
        free(temp);
        return;
    }
    // Find the key to be deleted
    while (temp != NULL && temp->item != key)
    {
        prev = temp;
        temp = temp->next;
    }

    // If the key is not present
    if (temp == NULL)
        return;

    // Remove the node
    prev->next = temp->next;

    free(temp);
}
// Print the linked list
void printList(struct Node *node)
{
    while (node != NULL)
    {
        cout << node->item << " ";
        node = node->next;
    }
}

// Driver program
int main()
{
    struct Node *head = NULL;

    insertAtEnd(&head, 1);
    insertAtBeginning(&head, 2);
    insertAtBeginning(&head, 3);
    insertAtEnd(&head, 4);
    insertAfter(head->next, 5);

    cout << "Linked list: ";
    printList(head);

    cout << "\nAfter deleting an element: ";
    deleteNode(&head, 3);
    printList(head);
}
