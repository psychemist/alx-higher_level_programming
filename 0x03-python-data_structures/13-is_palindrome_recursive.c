#include "lists.h"
#include <stdlib.h>
/**
 * is_pal - Checks if a list contains the same values backwards and forwards
 * @left: pointer to a pointer to the head of a singly linked list
 * @right: pointer to the tail node of a singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_pal(listint_t **left, listint_t *right)
{
	/* Stop recursion when right is NULL */
	if (right == NULL)
		return (1);

	/* Recursively move right pointer to end of list and compare values */
	if (is_pal(left, right->next) && ((*left)->n == right->n))
	{
		/* Move left pointer inwards */
		*left = (*left)->next;
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to the head of a singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = *head;
	listint_t *end = *head;

	if (head == NULL) /* non-existing list is not a palindrome*/
		return (0);
	if (*head == NULL) /* one node list is a palindrome */
		return (1);

	return (is_pal(&start, end));
}

