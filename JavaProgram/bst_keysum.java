//Program to check if a BST contains two elements whose sum equals a given target.
import java.util.*;
//Node class
class TreeNode{
  int val;
  Node left;
  Node right;
//Constructor to create a new node with a given value 
  Node(int x){
    val=x;
    left=right=NULL;
  }
}
//Main Class
public class BST_KEYSUM{
  //Function to insert a value into the BST
  static Node insert(Node root,int val){
    if(root==NULL)
      //If tree is empty, create new node as root
      return new Node(val);
    if(val<root.val)
      //If value is amaller, insert into left subtree
      
    else
      //If value is larger or equal, insert into right subtree
      root.right=insert(root.right,val);
    return root;
  }

  //Inorder traversal: stores elements in sorted order into a list
  static void inorder(Node root,List<Integer> list){
    if(root==NULL) return;
    inorder(root.left,list);
    list.add(root.val);
    inorder(root.right,list);
  }
  //Function to check if there exists two elements whose sum equals k
  static boolean findTarget(Node root,int k){
    //Step1: store all BST in sorted order
    List<Integer> list=new ArrayList<>();
    inorder(root,list);
    //Step2: Use two-pointer technique on the sorted list
    int left=0;
    int right=list.size()-1;
    while(left<right){
      int sum=list.get(left)+list.get(right);
      if(sum==k)
        return true;
      else if(sum<k)
        left++;
      else
        right--;
    }
    return false;
  }
  //Main function
  public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    //Input number of nodes
    System.out.println("Enter number of nodes: ");
    int n=sc.nextInt();
    //Built the BST by inserting nodes one by one
    Node root=NULL;
    System.out.println("\n Enter node values: ");
    for(int i=0;i<n;i++){
      int val=sc.nextInt();
      root=insert(root,val);
    }
    //Input target sum
    System.out.print("\n Enter target sum: ");
    int k=sc.nextInt();
    //Call function and print result
    if(findTarget(root,k)){
      System.out.println("TRUE!");
      else
      System.out.println("FALSE!");
    sc.close();
  }
}
