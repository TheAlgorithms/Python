// Function to insert at the end
void insertEnd(struct Node** start, int value)
{
	// If the list is empty, create a single node
	// circular and doubly list
	if (*start == NULL)
	{
		struct Node* new_node = new Node;
		new_node->data = value;
		new_node->next = new_node->prev = new_node;
		*start = new_node;
		return;
	}

	// If list is not empty

	/* Find last node */
	Node *last = (*start)->prev;

	// Create Node dynamically
	struct Node* new_node = new Node;
	new_node->data = value;

	// Start is going to be next of new_node
	new_node->next = *start;

	// Make new node previous of start
	(*start)->prev = new_node;

	// Make last previous of new node
	new_node->prev = last;

	// Make new node next of old last
	last->next = new_node;
}
