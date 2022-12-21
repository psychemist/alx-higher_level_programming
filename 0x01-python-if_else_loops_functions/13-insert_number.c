#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * *insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of a singly linked list
 * @number: integer value of new linked list node
 * Return: address of the new node (success) or NULL (fail)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	/* Allocate memory to new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	/* Assign data values to new node */
	new_node->n = number;

	/* Special case for head */
	if (*head == NULL || (*head)->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		/* Locate the node before the insertion point */
		current = *head;
		while (current->next != NULL && current->next->n < new_node->n)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}

	return (new_node);
}

