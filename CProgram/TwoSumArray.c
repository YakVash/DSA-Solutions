#include<stdio.h>
#include<stdlib.h>
typedef struct {
int value;
int index;
} NumIndex;

//Function too swap two elements
void swap(NumIndex* a, NumIndex* b){
  NumIndex temp = *a;
  *a = *b;
  *b = temp;
}

//simple selection sort based on value
void sortArray(NumIndex arr[], int n) {
  for(int i = 0; i < n - 1; i++) {
    int midIdx = i;
    for(int j = i + 1; j < n; j++) {
      if(arr[j].value < arr[midIdx].value) {
        midIdx = j;
      }
   }
   swap(&arr[i], &arr[midIdx]);
  }
}

//Function to find two numbers that sum up to target
int* twoSum(NumIndex* numbers, int numbersSize, int target, int* returnSize) {
  int left = 0;
  int right = numbersSize - 1;
  *returnSize = 2;
  int* result = (int*)malloc(2*sizeof(int));
  while(left < right){
    int sum = numbers[left].value + numbers[right].value;
    if(sum == target) {
//return original 1-indexed position
      result[0] = numbers[left].index + 1;
      result[1] = numbers[right].index + 1 ;
      return result;
    }
    else if(sum < target)
      left++;
    else
      right--;
  }
  return NULL;
}

int main() {
  int n, target;
  printf("Enter number of elements:");
  scanf("%d", &n);

  NumIndex numbers[n];
  printf("Enter elements: \n");
  for(int i = 0; i < n; i++){
    scanf("%d", &numbers[i].value);
    numbers[i].index = i;
  }
  printf("Enter Target sum: ");
  scanf("%d", &target);
//sort array
  sortArray(numbers, n);
  int returnSize;
  int* indices = twoSum(numbers, n, target, &returnSize);
  if(indices != NULL) {
    printf("Indices:[%d %d]\n", indices[0], indices[1]);
    free(indices);
  }
  else
    printf("No solution found.\n");

return 0;
}
