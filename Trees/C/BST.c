#include<stdio.h>
#include<stdlib.h>

struct node
{
    int key;
    struct node *left , *right;
};

struct node* newNode(int item)
{
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    temp->key = item;
    temp->left = temp->right = NULL;
    return temp;
}

void inorder(struct node* root)
{
    if(root != NULL)
    {
        inorder(root->left);
        printf("%d ", root->key);
        inorder(root->right);
    }
}

struct node* insert(struct node* node, int key)
{
    if(node == NULL)
    {
        return newNode(key);
    }

    if(key < node->key)
    {
        node->left = insert(node->left, key);
    }
    else if(key > node->right)
    {
        node->right = insert(node->right, key);
    }

    return node;
}

struct node* search(struct node* root, int key)
{
    // Base Cases: root is null or key is present at root
    if (root == NULL || root->key == key)
       return root;
    
    // Key is greater than root's key
    if (root->key < key)
       return search(root->right, key);
 
    // Key is smaller than root's key
    return search(root->left, key);
}

/* Given a non-empty binary search 
   tree, return the node
   with minimum key value found in
   that tree. Note that the
   entire tree does not need to be searched. */

struct node* minValueNode(struct node* node)
{
    struct node* current = node;
 
    /* loop down to find the leftmost leaf */
    while (current && current->left != NULL)
        current = current->left;
 
    return current;
}


struct node* deleteNode(struct node* root, int key)
{
    if(root == NULL)
    {
        return root;
    }

    if(key < root->key)
    {
        root->left = deleteNode(root->left, key);
    }
    else if(key > root->key)
    {
        root->right = deleteNode(root->right, key);
    }

    else{
        //node with only one child or no child
        if(root-> left == NULL)
        {
            struct node* temp = root->right;
            free(root);
            return temp;
        }
        else if(root->right == NULL)
        {
            struct node* temp = root->left;
            free(root);
            return temp;
        }

        //node with two children
        //Get the inorder successor (smallest in the right subtree)
        struct node* temp = minValueNode(root->right);

        //Copy the inorder successor's value to the root
        root->key = temp->key;
        //Delete the inorder successor from the right subtree
        root->right = deleteNode(root->right, temp->key);
    }
    return root;
}


int main()
{
    struct node* root = NULL;
    root = insert(root,50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);

    inorder(root);
    printf("\n");
    deleteNode(root,30);
    inorder(root);
    
}
