# ================================================================== #
# ================================================== # Dependencies

set(CMAKE_FIND_PACKAGE_PREFER_CONFIG TRUE)
find_package(Catch2 REQUIRED)

# ================================================================== #
# ================================================== # Target

set(TEST_TARGET {{cxx_test}})

file(GLOB_RECURSE HEADERS CONFIGURE_DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/*.hpp)
file(GLOB_RECURSE SOURCES CONFIGURE_DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)

add_executable(${TEST_TARGET} ${HEADERS} ${SOURCES})
target_compile_features(${TEST_TARGET} PRIVATE cxx_std_20)
target_link_options(${TEST_TARGET} PRIVATE -static-libgcc -static-libstdc++)

if (CMAKE_CXX_COMPILER_ID MATCHES "Clang")
	# target_compile_options(${TEST_TARGET} ... )
elseif (CMAKE_CXX_COMPILER_ID MATCHES "GNU")
	target_compile_options(${TEST_TARGET} PRIVATE -W -Wall -Wextra -Werror -pedantic)
elseif (CMAKE_CXX_COMPILER_ID MATCHES "Intel")
	# target_compile_options(${TEST_TARGET} ... )
elseif (CMAKE_CXX_COMPILER_ID MATCHES "MSVC")
	target_compile_options(${TEST_TARGET} PRIVATE /W4 /WX)
endif()

target_link_libraries(${TEST_TARGET} PUBLIC {{cxx_target}} Catch2::Catch2)

# ================================================================== #
# ================================================== # Testing

enable_testing()
include(CTest)
include(Catch)

catch_discover_tests(${TEST_TARGET})

# ================================================================== #
# ================================================== # Installation

install(TARGETS ${TEST_TARGET} EXPORT ${PROJECT_NAME}Targets
	RUNTIME       DESTINATION bin
)
