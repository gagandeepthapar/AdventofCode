#include "main.hpp"

#include <iostream>
#include <gtest/gtest.h>

using namespace std;

TEST(DAY01, READ_TEST){
	// expect data
	vector<string> expect = {"1000", "2000", "4000"};

	// test data
	vector<string> data = myread("test.txt");
	
	// ensure non-empty file
	if(data.size() == 0){
		cout << "NOTHING IN FILE" << endl;
		FAIL();
	}

	if(data.size() != expect.size()){
		cout << "Differently sized vectors. Test: " << data.size() << "; Expected: " << expect.size() << endl;
		FAIL();
	}

	for(int i = 0; i < data.size(); i ++){
		EXPECT_EQ(data[i], expect[i]) << " Position: " << i;
	}

}

TEST(DAY01, Basic){
	EXPECT_EQ(1+1, 2);
}

TEST(DAY01, Pass){
	EXPECT_EQ(1-1, 0);
}

