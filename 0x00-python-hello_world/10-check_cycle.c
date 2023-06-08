
#include "lists.h"

/**
  * check_cycle - function that checks linked list cycle
  * @list:- linked list
  * Return:- Always 0
  */

int check_cycle(listint_t *list)
{
	listint_t *lst;

	if (list && list->next)
	{
		lst = list->next;
	}
	else
	{
		return (0);
	}

	while (list && lst)
	{
		if (list == lst)
		{
			return (1);
		}

		list = list->next;

		if (lst->next)
		{
			lst = lst->next;
		}
		else
		{
			return (0);
		}

		if (lst->next)
		{
			lst = lst->next;
		}
		else
		{
			return (0);
		}
	}

	return (0);
}
