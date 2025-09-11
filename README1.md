**Two Sum IV - Input is a BST**
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

Features
Build a BST from user input.
Search for two numbers that add up to a target sum.
Returns TRUE if such a pair exists, otherwise FALSE.

HOW TO RUN in C
1. Open a terminal in the project folder
2. Compile the program:
    gcc BST_KEYSUM.C -o BST_KEYSUM
3. Run the executable:
    .\BST_KEYSUM

HOW TO RUN in Java
1. Open a terminal in the project folder
2. Compile the program:
    javac BST_KEYSUM.java
3. Run the executable:
    java BST_KEYSUM

CONCEPTS USED
1. Binary Search Tree
2. Inorder Traversal
3. Two pointer on sorted list

**Two Sum II - Input Array is sorted**

📌 Problem Statement

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one, as an integer array [index1, index2] of length 2.
You may not use the same element twice.
The tests are generated such that there is exactly one solution.
Your solution must use only constant extra space.

✅ Example
Input
numbers = [2, 7, 11, 15], target = 9

Output
[1, 2]

Explanation
numbers[1] + numbers[2] = 2 + 7 = 9
So, the answer is [1, 2].

💡 Approach

Since the array is sorted, a two-pointer technique works efficiently.

Initialize two pointers:
left = 0 (start of array)
right = numbers.length - 1 (end of array)

While left < right:
Compute sum = numbers[left] + numbers[right]

If sum == target, return [left+1, right+1]
If sum < target, move left forward to increase sum
If sum > target, move right backward to decrease sum
Time complexity: O(n)
Space complexity: O(1)
