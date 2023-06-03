#include "read_file.hpp"

#include <iostream>
#include <fstream>

using namespace std;

vector<string> read_file(const string& filename){
	ifstream file(filename);
	vector<string> file_data;
	string line;

	if(file.is_open()){
		while(getline(file, line)){
			file_data.push_back(line);
		}
		file.close();
	}
	else{
		cout << "Unable to open file: " << filename << endl;
	}

	return file_data;
}

