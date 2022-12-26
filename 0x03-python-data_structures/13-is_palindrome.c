#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * reverseList - reverses a singly linked list
 * @head: address of the head pointer to a singly linked list
 * Return: Nothing
 */
void reverse_list(listint_t **head)
{
	listint_t *prev, *current, *next;

	prev = NULL;
	current = *head;

	/* Iterate through the linked list and reverse its order */
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compareLists - checks if two singly linked lists have the same data input
 * @list1: pointer to first linked list
 * @list2: pointer to second linked list
 * Return: 0 if they are not equal, 1 if both lists are equal
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	listint_t *temp1 = list1;
	listint_t *temp2 = list2;

	/* Iterate through the lists and compare equality */
	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}

	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: address of the head pointer to a singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int res;
	listint_t *fast = *head, *slow = *head, *prev_slow = *head;
	listint_t *half, *midnode = NULL;

	if (head == NULL)
		return (0); /* non-existing list is not a palindrome */
	if (*head == NULL || (*head)->next == NULL)
		return (1); /* empty or one node list is a palindrome*/

	while (fast != NULL && fast->next != NULL)
	{
		/* Move slow by 1 and fast by 2. Slow ptr is the mid node */
		prev_slow = slow;
		slow = slow->next;
		fast = fast->next->next;

		if (fast != NULL) /* fast == NULL in even list*/
		{
			midnode = slow; /* Detach middle node from odd list */
			slow = slow->next;
		}

		prev_slow->next = NULL; /* Terminate first half */
		half = slow;
		reverse_list(&half); /* Reverse second half */
		res = compare_lists(*head, half); /* Compare with first half */

		/* Reverse second half and reconstruct original list */
		reverse_list(&half);
		if (midnode != NULL)
		{
			prev_slow->next = midnode; /* Reinsert middle node */
			midnode->next = half;
		}
		else
		{
			prev_slow->next = half;
		}
	}
	return (res);
}

