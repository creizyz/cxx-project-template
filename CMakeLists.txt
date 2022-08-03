cmake_minimum_required(VERSION 3.20)

# ================================================================== #

set(PROJECT_NAME {{CXX_PROJECT}})

set(${PROJECT_NAME}_MAJOR_VERSION 0 CACHE STRING "Project major version")
set(${PROJECT_NAME}_MINOR_VERSION 0 CACHE STRING "Project minor version")
set(${PROJECT_NAME}_PATCH_VERSION 0 CACHE STRING "Project patch version")
set(${PROJECT_NAME}_VERSION ${${PROJECT_NAME}_MAJOR_VERSION}.${${PROJECT_NAME}_MINOR_VERSION}.${${PROJECT_NAME}_PATCH_VERSION})

project(${PROJECT_NAME} VERSION ${${PROJECT_NAME}_VERSION})

# ================================================================== #
# ================================================== # Git revision

execute_process(COMMAND git log --pretty=format:'%h' -n 1 OUTPUT_VARIABLE ${PROJECT_NAME}_GIT_REVISION ERROR_QUIET)
if ("${${PROJECT_NAME}_GIT_REVISION}" STREQUAL "")
	set(${PROJECT_NAME}_GIT_REVISION "N/A")
	set(${PROJECT_NAME}_GIT_BRANCH   "N/A")
else()
	execute_process(COMMAND git rev-parse --abbrev-ref HEAD OUTPUT_VARIABLE ${PROJECT_NAME}_GIT_BRANCH)
	string(STRIP "${${PROJECT_NAME}_GIT_REVISION}" ${PROJECT_NAME}_GIT_REVISION)
	string(STRIP "${${PROJECT_NAME}_GIT_BRANCH}"   ${PROJECT_NAME}_GIT_BRANCH)
	string(STRIP "${${PROJECT_NAME}_GIT_REVISION}" ${PROJECT_NAME}_GIT_REVISION)
endif()

# ================================================================== #
# ================================================== # Version file

set(PROJECT_MAJOR_VERSION ${${PROJECT_NAME}_MAJOR_VERSION})
set(PROJECT_MINOR_VERSION ${${PROJECT_NAME}_MINOR_VERSION})
set(PROJECT_PATCH_VERSION ${${PROJECT_NAME}_PATCH_VERSION})
set(PROJECT_GIT_REVISION  ${${PROJECT_NAME}_GIT_REVISION})
set(PROJECT_GIT_BRANCH    ${${PROJECT_NAME}_GIT_BRANCH})

configure_file(source/version.hpp.in ${CMAKE_BINARY_DIR}/include/version.hpp)

# ================================================================== #
# ================================================== # External Modules

list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/modules")

# ================================================================== #
# ================================================== # Targets

add_subdirectory(source)

if(EXISTS test)
	option(BUILD_TESTS "Build tests for ${PROJECT_NAME}" ON)
	if(BUILD_TESTS)
		add_subdirectory(test)
	endif()
endif()