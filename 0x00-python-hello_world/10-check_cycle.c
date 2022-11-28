#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
	slow = fast = list;

	while(slow && fast && fast->next)
	{
		/* Slow pointer will move one node per iteration whereas
		 * fast node will move two nodes per iteration
		 */
		slow = slow->next;
		fast  = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
