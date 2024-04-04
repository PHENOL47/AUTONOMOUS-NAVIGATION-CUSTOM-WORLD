cmake_minimum_required(VERSION 3.8)
project(ayush_publisher_cc)

set(ayush_publisher_cc_MAJOR_VERSION 0)
set(ayush_publisher_cc_MINOR_VERSION 0)
set(ayush_publisher_cc_PATCH_VERSION 0)
set(ayush_publisher_cc_VERSION
  ${ayush_publisher_cc_MAJOR_VERSION}.${ayush_publisher_cc_MINOR_VERSION}.${ayush_publisher_cc_PATCH_VERSION})

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
