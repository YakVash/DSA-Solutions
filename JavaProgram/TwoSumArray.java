import java.util.*;

class NumIndex {
  int value;
  int index;

NumIndex(int value, int index) {
  this.value = value;
  this.index = index;
}
}
public class TwoSumSorted {
  //Function to swap two elements
  private static void swap(NumIndex[] arr,int i,int j) {
    NumIndex temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }

  //Simple selection sort based on value
  private static void sortArray(NumIndex[] arr) {
    int n = arr.length;
    for (int i = 0;i< n - 1; i++) {
      int minIdx = i;
      for (int j = i + 1; j < n; j++) {
        if (arr[j].value < arr[minIdx].value) {
          minIdx = j;
        }
      }
      swap(arr, i, minIdx);
    }
  }

  //Function to find two numbers that sum upto target
  private static int[] twoSum(NumIndex[] numbers,int target){
     int left = 0, right = numbers.length - 1;
    while(left < right){
      int sum = numbers[left].value + numbers[right].value;
     if(sum == target) {
       //return original 1-indexed positions
       return new int[]{numbers[left].index + 1, numbers[right].index + 1};
     } else if(sum<target) {
       left++;
     } else {
       right--;
     }
  }
  return null;//no solution
  }

  public static void main(String[] arg){
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter the number of elements: ");
    int n = sc.nextInt();
    
    NumIndex[] numbers = new NumIndex[n];
    System.out.println("Enter Elements: ");
    for(int i = 0;i < n; i++) {
      int val = sc.nextInt();
      numbers[i] = new NumIndex(val,i);
    }

    System.out.println("Enter target sum: ");
    int target = sc.nextInt();

    //sort array
    sortArray(numbers);
    int[] indices = twoSum(numbers, target);
    if(indices != null) {
      System.out.println("Indices: [" + indices[0] + "," + indices[1] + "]");
    }else {
      System.out.println("No solutions found.");
    }

    sc.close();
  }
  }
  
