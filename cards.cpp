#include <iostream>
#include <fstream>
#include <ctime>
#include <vector>
#include <algorithm>
using namespace std;

// Create deck of n cards (vector of booleans)
vector<bool> makeDeck(int n){
	vector<bool> deck;
	for(int i = 0; i < n; i++){
		bool a = true;
		deck.push_back(a);
	}
	return deck;
}

// Print deck (debugging)
void printDeck(vector<bool> *deck){
	cout << "[ ";
	for(int i = 0; i < deck->size(); i++){
		cout << deck->at(i) << " ";
	}
	cout << "]" << endl;
}

// Check if deck orientation matches first card
bool isHomo(vector<bool> *deck){
	bool first = deck->at(0);
	bool isHomo = true;
	for(int i = 1; i < deck->size(); i++){
		if( deck->at(i) != first){
			isHomo = false;
			break;
		}
	}
	return isHomo;
}

// Split deck, flip bottom half, reverse bottom half, clear deck, faro shuffle to recombine halves 2,1,2,1...
void flipShuffle(vector<bool> *deck){
	vector<bool> half1;
	vector<bool> half2;
	int deckSize = deck->size();
	
	for(int i = 0; i < deckSize / 2; i++){
		half1.push_back(deck->at(i));
	}
	
	for(int i = deckSize / 2; i < deckSize; i++){
		half2.push_back(deck->at(i));
	}

	half2.flip();
	reverse(half2.begin(),half2.end());
	deck->clear();

	for(int i = 0, j = 0, k = 0; i < deckSize; i++){
		if(i % 2 == 0){
			deck->push_back(half2.at(j));
			j++;
		}
		else{
			deck->push_back(half1.at(k));
			k++;
		}
	}
}

int main(int argc, char * argv[]){
	clock_t start = clock();


// To operate from command line :
// ~./compiledFileName lowerLimit upperLimit (verboseMode)

	int lowerLim = stoi(argv[1]);
	int upperLim = stoi(argv[2]);
	string verbose;

// Verbose modes:
//   commandLine :   Prints deck size, number of steps to command line instead of csv
//   showSteps   :   Prints out deck after each shuffle (debugging tool) 
	

	bool commandLine = false;
	bool showSteps = false;
	if(argc >= 4){
	verbose = argv[3];
		if(verbose == "commandLine"){
			commandLine = true;
		}
		if(verbose == "showSteps"){
			showSteps = true;
		}
	}

	

	ofstream csv;
	csv.open("cards.csv");

	for(int i = lowerLim; i <= upperLim; i++){
		vector<bool> deck = makeDeck(i);
		vector<bool> *p = &deck;
		int steps = 0;

		if(showSteps){
			printDeck(&deck);
		}    

		flipShuffle(&deck);
		steps++;

		if(showSteps){
			printDeck(&deck);
		}

		while(isHomo(&deck) == false){
			flipShuffle(&deck);

			if(showSteps){
		 printDeck(&deck);
			}
			steps++;
		}

		if(i % 100 == 0){
			cout << i << endl;
		}

		if(commandLine){
			cout << i << ", " << steps << endl;
		}else{ csv << i << ", " << steps << endl; }
	}
	clock_t end = clock();
	int elapsed_time = (end - start) / CLOCKS_PER_SEC;

	if(elapsed_time > 300){
		int minutes = elapsed_time / 60;
		int seconds = elapsed_time % 60;
		
		cout << minutes << ":" << seconds << endl;
	}else{ cout << elapsed_time << " seconds" << endl; }
}
