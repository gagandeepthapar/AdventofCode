#include "utils.hpp"

#include <iostream>

using namespace std;

vector<string> myread(const string& filename){
	return read_file(filename);
}

