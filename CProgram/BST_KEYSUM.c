//Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

struct Node {
    int val;
    struct Node* left,*right;
};

//create a node
struct Node* newNode(int value) {
    struct Node* node = (struct Node*) malloc (sizeof (struct Node));
    node->val=value;
    node -> left = node -> right = NULL;
    return node;
}
//insert a new node
struct Node* insert(struct Node* root,int value) {
    if(!root) return newNode(value);
    if(value < root->val)
    root->left = insert(root->left, value);
    else if(value > root->val)
       root->right = insert(root->right, value);
    return root;
}
//count the total number of nodes
int countNode(struct Node* root)
{
    if(!root)return 0;
    return 1 + countNode(root->left) + countNode(root->right);
}
//inorder insertion in an array
void inorder(struct Node* root, int arr[],int* index) {
    if(!root) return;
    inorder(root->left, arr, index);
    arr[(*index)++] = root->val;
    inorder(root->right, arr, index);

}
//main function to find whether the sum of two nodes is equal to the key provided
bool findTarget(struct Node* root,int k) {
    int n = countNode(root);
    int* arr = (int*)malloc(n * sizeof(int));
    int index = 0;
    inorder(root, arr, &index);
    int left=  0, right = n - 1;
    while(left < right) {
        int sum = arr[left] + arr[right];
        if(sum == k)
          return true;
        else if(sum < k)
          left++;
        else
          right++;
    }
    free(arr);
    return false;
}

int main() {
    struct Node* root = NULL;
    int n, i, val, k;
    printf("Enter the number of nodes: ");
    scanf("%d", &n);
    
    printf("\n Enter %d nodes of the BST tree: \n", n);
    for(i = 0; i < n; i++) {
      scanf("%4d", &val); 
      root = insert(root, val);
    }
    
    printf("\nEnter the target sum: ");
    scanf("%d", &k);
    if(findTarget(root, k))
     printf("\nTRUE!");
    else 
     printf("\nFALSE!");
    return 0;
}
