project(virtual-abstraction-client)

cmake_minimum_required(VERSION 2.8.12 FATAL_ERROR)

## Make sure C++11 support is enabled
add_compile_options(-std=c++11)
add_definitions(-DRTI_UNIX -DRTI_LINUX -DRTI_64BIT)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lib)

## Add subdirectories
add_subdirectory(src)
