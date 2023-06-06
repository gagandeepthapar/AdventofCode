#include "src.hpp"
#include "utils.hpp"

#include <numeric>
#include <iostream>
#include <unistd.h>

using namespace std;

// Part 1

vector<int> read_int_from_file(const string& filename){
  /*
   * method to return total calories per elf
   */

  vector<string> file_data = read_file(filename); 
  vector<int> elf_cals;
  int current_cals = 0;
  elf_cals.reserve(file_data.size());
  
  for(const string& line : file_data){
    // push value on vector if new line
    if(line.size() == 0){
      elf_cals.push_back(current_cals);
      current_cals = 0;
    }
    // update current elf calories
    else{
      current_cals += stoi(line);
    }
  }
  
  return elf_cals;
}

// Part One
int part_one(const string& filename){
  /*
   * return calorie count of elf with max calories
   */
 
  int max_value = 0;
  vector<int> elf_cals = read_int_from_file(filename);

  for(const int cal_count : elf_cals){
    max_value = (max_value > cal_count) ? max_value : cal_count;
  }

  return max_value;
}


// Part 2
int part_two(const string& filename){


  return 0;
}

