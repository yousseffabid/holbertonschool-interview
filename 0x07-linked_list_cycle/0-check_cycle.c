#include "lists.h"

/**
 * check_cycle - checks if a SL list has a cycle
 * @list: pointer to the head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_node, *fast_node;

	if (!list)
		return (0);

	fast_node = list;
	slow_node = list;

	while (slow_node && fast_node && fast_node->next)
	{
		slow_node = slow_node->next;
		fast_node = fast_node->next->next;

		if (fast_node == slow_node)
			return (1);
	}

	return (0);
}
