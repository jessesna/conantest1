cmake_minimum_required(VERSION 3.8.0)

project(conantest
  VERSION 0.1
  LANGUAGES CXX)

include(CTest)
enable_testing()

add_executable(conantest1 conantest1.cpp)
add_test(conantest1 conantest1)
add_executable(conantest2 conantest2.cpp)
add_test(conantest2 conantest2)
