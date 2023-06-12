#include "lists.h"

int going_in_circle(listint_t *lf, listint_t *end, int s);
void map(listint_t **head);
/**
  * going_in_circle - function that checking for palindm
  * @lf:- start point
  * @s:- size of list
  * @end:- end point
  * Return:- Always 0
  */

int going_in_circle(listint_t *lf, listint_t *end, int s)
{
	int lap = 0;

	if (lf == NULL || end == NULL)
		return (1);

	for (; lap < s; lap++)
	{
		if (lf->n != end->n)
			return (0);
		lf = lf->next;
		end = end->next;
	}

	return (1);
}


/**
  * is_palindrome - checking weather singly-linked list is
  * @head:- start node of list
  * Return:- Always 0
  */

int is_palindrome(listint_t **head)
{
	int len = 0, j;
	listint_t *dck;
	listint_t *tmp;

	if (head == NULL || *head == NULL)
	{
		return (1);
	}

	dck = *head;
	tmp = *head;

	for (; tmp != NULL; len++)
		tmp = tmp->next;

	len = len / 2;

	for (j = 1; j < len; j++)
	{
		dck = dck->next;
	}

	if ((len % 2) != 0 && len != 1)
	{
		dck = dck->next;
		len = len - 1;

	}

	map(&dck);
	j = going_in_circle(*head, dck, len);

	return (j);
}

/**
  * map - function maps node and revese them
  * @head:- head ptr
  * Return:- Always 0
  */

void map(listint_t **head)
{
	listint_t *ran;
	listint_t *prv;
	listint_t *next;

	if (head == NULL || *head == NULL)
		return;

	ran = *head;
	prv = NULL;

	while (ran != NULL)
	{
		next = ran->next;
		ran->next = prv;
		ran = next;

	}

	*head = prv;
}
