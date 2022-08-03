#include <catch2/catch.hpp>

#include "example.hpp"

TEST_CASE("test square function", "")
{
  REQUIRE(example::square(1) ==  1);
  REQUIRE(example::square(2) ==  4);
  REQUIRE(example::square(3) ==  9);
  REQUIRE(example::square(4) == 16);
  REQUIRE(example::square(5) == 25);
}