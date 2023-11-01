#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the head of the linked list
 *
 *  Return: 1 if there is a cycle, otherwise 0
 */
int check_cycle(listint_t *list)
{
listint_t *S = list;
listint_t *F = list;

while (S && F && F->next)
{
S = S->next;
F = F->next->next;

/* If meets at some point */
if (S == F)
return (1);
}
return (0); /* No cycle found */
}
