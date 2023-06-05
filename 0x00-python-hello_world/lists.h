#ifndef LISTS_H
#define LISTS_H


#include <stdlib.h>

size_t print_listint(const listint_t *h);
int check_cycle(listint_t *list);
void free_listint(listint_t *head);
listint_t *add_nodeint(listint_t **head, const int n);

/**
  * struct listint_s - linked list
  * @n: number member
  * @next: node of the lst
  * Description: linked list node strct
  */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

#endif
