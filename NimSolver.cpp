#include <iostream>

#define N_ROWS 3
#define MAX 10000000
#define MIN -10000000

using namespace::std;

int sticks[N_ROWS];
int best_i, best_j;

int computer_move(int depth);
int user_move(int depth);

bool didWin() {
  for (int i = 0; i < N_ROWS; i++) {
    if (sticks[i] != 0) return false;
  }
  return true;
}

int computer_move(int depth) {
  int max = MIN+1;

  if (didWin()) return MIN;
  
  for (int i = 0; i < N_ROWS; i++) {
    for (int j = 1; j <= sticks[i]; j++) {
      sticks[i] -= j;

      int result = user_move(depth+1);

      if (result > max) {
	max = result;
	
	if (depth == 0) {
	  best_i = i;
	  best_j = j;
	}
      }
      
      sticks[i] += j;
    }
  }
  
  return max;
}

int user_move(int depth) {
  int min = MAX-1;

  if (didWin()) return MAX;

  for (int i = 0; i < N_ROWS; i++) {
    for (int j = 1; j <= sticks[i]; j++) {
      sticks[i] -= j;
      
      int result = computer_move(depth+1);

      if (result < min) {
	min = result;
      }

      sticks[i] += j;
    }
  }

  return min;
}

int main(int argc, char *argv[]) {
  for (int i = 0; i < 3; i++) {
    cin >> sticks[i];
  }
  
  cout << computer_move(0) << endl;
  cout << "Take " << best_j << " from pile " << best_i+1;
}
