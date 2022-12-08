#include "lists.h"
/**
 * check_cycle - 
 * @list: pointer to head of linked list
 * Return: 0 if no cycle or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	while (slow && fast && fast->next)
	{
		/* Slow pointer will move one node per iteration */
		/* fast node will move two nodes per iteration */
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}

