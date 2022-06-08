/*
The Problem: Hard
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, 
it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) 
which adds the element to the end, and a get(index) which returns the node at index.*/

/*Notes

    the node structure will just contain data and then 'both' where both is  prev XOR next


*/


/*My solution*/

/*includes*/
#include <stdio.h>
#include <stdlib.h>

/*my definition of an XOR node*/
typedef struct Node {
    int data;
    struct Node *both;
} Node;

/*header functions*/
int add(Node *head, int element);
Node get(int index);

int add(Node *head, int element){

    /*create a new node*/
    Node *temp = malloc(sizeof(Node));
    Node *prev = head;
    Node *curr = head;
    Node *old = NULL;

    /*assign element to new node*/
    temp -> data = element;

    /*find where the new element should go, and then insert it*/

    /*this means that the list is empty, so change the first elements both to be 0 xor new data as the list would be
         NULL -> Head -> New*/
    if(head -> both == NULL){
        head -> both = 0 ^ (temp -> data);
        temp ->  both = (head -> data) ^ 0;
    } else {
        /*this means that the list is more then just the head, so iterate through the list until it there is a null, then append*/

        while(curr -> both != &(curr -> both)){
            /*if curr->both is equal to the address at the current, then this is the end of the list*/
            old == curr;
            /*curr == (curr -> both) ^ (prev -> both);*/
            prev == old;

        }


    }



    return 1;
}


int main(void){
    printf("this is the main function");
}