#include <iostream>
#include <vector>
#include <ctime>

#define ARRAY_SIZE 100000000
#define NUM_TESTS 1000

using namespace::std;

int binarySearch(vector<int> array, int target) {
  int upperbound = array.size();
  int lowerbound = 0;

  while (lowerbound <= upperbound) {
    int middle = (lowerbound + upperbound) / 2;
    
    if (array[middle] == target) return middle;
    if (array[middle] > target) upperbound = middle - 1;
    if (array[middle] < target) lowerbound = middle + 1;
  }
  return -1;
}

int linearSearch(vector<int> array, int target) {
  for (int i = 0; i < array.size(); i++) {
    if (array[i] == target) return i;
  }
  return -1;
}

vector<int> generateBigArray() {
  vector<int> array;
  for (int i = 0; i < ARRAY_SIZE; i++) {
    array.push_back(i);
  }
  return array;
}

double binarySearchTimes(vector<int> array) {
  double average = -1;
  for (int i = 0; i < NUM_TESTS; i++) {
    double start = clock();
    binarySearch(array, rand() % ARRAY_SIZE);
    double end = clock();
    double time = end - start;

    if (average == -1) average = time;
    else average = (average + time) / 2;
  }
  return average;
}

double linearSearchTimes(vector<int> array) {
  double average = -1;
  for (int i = 0; i < NUM_TESTS; i++) {
    double start = clock();
    linearSearch(array, rand() % ARRAY_SIZE);
    double end = clock();
    double time = end - start;
   
    if (average == -1) average = time;
    else average = (average + time) / 2;
  }
  return average;
}

int main(int argc, char * argv[]) {
  vector<int> array = generateBigArray();
  
  double binSearchTime = binarySearchTimes(array);
  double linSearchTime = linearSearchTimes(array);
  
  cout << "Binary Search Times: " << binSearchTime << " Milliseconds" << endl;
  cout << "Linear Search Times: " << linSearchTime << " Milliseconds" << endl;

  cout << "Difference: " << linSearchTime - binSearchTime << endl;
}
