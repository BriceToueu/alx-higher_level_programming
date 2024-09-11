#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function that inserts number into a sorted singly linked list
 * @head: head of the linked list
 * @number: data of the new node
 * Return: address of new node or NULL if fails
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *temp1 = *head, *temp2 = *head, *temp3 = *head;
    unsigned int count = 0, position = 0;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    while (temp1->next)
    {
        position++;
        temp3 = temp3->next;
        if (temp1->n > number)
        {
            position--;
            break;
        }
        else if (temp1->next->next == NULL && temp3->n < number)
        {
            position++;
            break;
        }
        temp1 = temp1->next;
    }
    if (position == 0)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }
    while (temp2 != NULL && count < position - 1)
    {
        temp2 = temp2->next;
        count++;
    }
    if (count == position - 1)
    {
        new_node->next = temp2->next;
        temp2->next = new_node;
        return (new_node);
    }
    return (NULL);
}
