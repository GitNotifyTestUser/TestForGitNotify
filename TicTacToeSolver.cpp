#include <iostream>
#include <vector>

#define MAX 100000
#define MIN -10000

#define USER 'x'
#define COM 'o'
#define EMPTY '.'

using namespace::std;

int user_move(int depth);
int computer_move(int depth);

char board[3][3];
int best_i, best_j;

void read_board() {
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      cin >> board[i][j];
    }
  }
}

bool did_win(char who) {
  
  //Check horizontal and vertical wins
  for (int i = 0; i < 3; i++) {
    bool vert = true;
    bool horizontal = true;
    for (int j = 0; j < 3; j++) {
      if (board[i][j] != who) 
	vert = false;
      if (board[j][i] != who) 
	horizontal = false;
    }

    if (vert || horizontal)
      return true;
  }

  bool diag1 = true, diag2 = true;
  for (int i = 0; i < 3; i++) {
    if (board[i][i] != who) diag1 = false;
    if (board[i][2-i] != who) diag2 = false;
  }

  if (diag1 || diag2) return true;
  return false;
}

bool is_draw() {
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      if (board[i][j] == EMPTY)
	return false;
    }
  }
  return true;
}

int computer_move(int depth) {

  int maximum = MIN+1;

  if (did_win(USER)) return MIN;
  if (is_draw()) return 0;

  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      if (board[i][j] == EMPTY) {
	
	//if (depth == 0) 
	//cout << i << " " << j << endl;
	
	board[i][j] = COM;

	int user = user_move(depth+1);
	
	if (user > maximum) {	 
	  maximum = user;
	  if (depth == 0) {
	    best_i = i;
	    best_j = j;
	  }
	}

	board[i][j] = EMPTY;
      }
    }
  }
  
  return maximum;
}

int user_move(int depth) {
  int minimum = MAX-1;

  if (did_win(COM)) return MAX;
  if (is_draw()) return 0;
  
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      if (board[i][j] == EMPTY) {
	board[i][j] = USER;

	int com = computer_move(depth+1);

	if (com < minimum) {
	  minimum = com;
	}
	
	board[i][j] = EMPTY;
      }
    }
  }
  
  return minimum;
}

void print_board() {
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      cout << board[i][j] << " ";
    }
    cout << endl;
  }
}

int main(int argc, char *argv[]) {
  
  //Read in input
  read_board();  

  //Minimax
  int best_outcome = computer_move(0);

  cout << best_outcome << endl;

  //Make best move
  board[best_i][best_j] = COM;

  print_board();
}
