#include <iostream>
#include <algorithm>
#include <vector>
#include <stdlib.h>

#define NUM_REPETITIONS 10
#define ARRAY_SZ 20000

using namespace::std;

void insert(int num, vector<int> &array) {
  for (int i = 0; i < array.size(); i++) {
    if (num < array[i]) {
      array.insert(array.begin() + i, num);
      return;
    }
  }
  array.push_back(num);
}

void insertion_sort(vector<int> &array) {
  vector<int> result;

  for (int i = 0; i < array.size(); i++) {
    insert(array[i], result);
  }
  array = result;
}

vector<int> generateRandomArray() {
  vector<int> newArray;
  for (int i = 0; i < ARRAY_SZ; i++) {
    newArray.push_back(rand());
  }
  return newArray;
}

void insertion_sort_times(vector<int> array) {
  double averageTime = 0;

  for (int i = 0; i < NUM_REPETITIONS; i++) {
    int strt, end;
    strt = time(NULL);
    insertion_sort(array);
    end = time(NULL);

    double taken = end - strt;
    averageTime += taken;
  }
  averageTime /= NUM_REPETITIONS;

  cout << "Insertion Sort: " << averageTime << endl;
}

void better_sort_times(vector<int> array) {
    double averageTime = 0;

  for (int i = 0; i < NUM_REPETITIONS; i++) {
    int strt, end;
    strt = time(NULL);
    sort(array.begin(), array.end());
    end = time(NULL);

    double taken = end - strt;
    averageTime += taken;
  }
  averageTime /= NUM_REPETITIONS;

  cout << "Better Sort: " << averageTime << endl;
}

int main(int argc, char *argv[]) {
  vector<int> array = generateRandomArray();
  cout << "Starting Sorting Time Comparison" << endl;
  insertion_sort_times(array);
  better_sort_times(array);
}
