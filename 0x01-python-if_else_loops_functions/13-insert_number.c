#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - Inserts a node in a sorted linked list.
 * @head: Pointer to the head of the linked list.
 * @number: Value to be inserted in the new node.
 *
 * Return: Address of the new node, or NULL on failure.
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *current = *head;
listint_t *new;

new = (listint_t *) malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

while (current != NULL)
{
if (number > current->n)
{
if (current->next == NULL || number <= current->next->n)
{
listint_t *tmp;

new->n = number;
tmp = current->next;
current->next = new;
new->next = tmp;
return (new);
}
}
else
{
new->n = number;
new->next = current;
*head = new;
return (new);

}
current = current->next;
}
return (add_nodeint_end(head, number));
}
