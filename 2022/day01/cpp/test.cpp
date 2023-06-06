#include "src.hpp"
#include "utils.hpp"

#include <climits>
#include <iostream>
#include <gtest/gtest.h>

using namespace std;

// ensure gtest is working
TEST(DAY01, Sanity){
	EXPECT_EQ(1+1, 2);
}

// test demo values for part 1
TEST(DAY01, DemoOne){
  int test = part_one("../demo.txt");
  int expect = 24000;

  EXPECT_EQ(test, expect);
}

// test input values for part 1
TEST(DAY01, InputOne){
  int test = part_one("../input.txt");
  int expect = 66719;

  EXPECT_EQ(test, expect);
}

// test demo values for part 2
TEST(DAY01, DemoTwo){
  int test = part_two("../demo.txt");
  int expect = 45000;
  EXPECT_EQ(test, expect);
}

// test input values for part 2
TEST(DAY01, InputTwo){
  int test = part_two("../input.txt");
  int expect = 198551;
  EXPECT_EQ(test, expect);
}
