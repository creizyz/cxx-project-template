# Project {{CXX_PROJECT}}

## Overview

**[ TODO ]** Write a brief introduction to the project and the library here.

*Note : this project was kickstarted using the [cxx-project-template](https://github.com/creizyz/cxx-project-template) project.*

## Setup & Requirements

This section explains how to setup this project in your environment.

### Development Environment

This CXX project uses ***cmake*** as a build orchestrator and requires a ***C++20 compatible compiler***. At this stage, the following compilers were tested:
- ***gcc-10+ (msys2)*** : OK
- ***gcc-10+ (linux)*** : UNKNOWN
- ***MSVC 17+*** : UNKNOWN
- ***clang*** : UNKNOWN
- ***intel compiler*** : UNKNOWN

### Dependencies

**[ TODO ]** Declare your dependencies here

### Cmake Presets

An easy way to manage multiple cmake configurations for a CXX project is to use [cmake presets](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html). This project declares a default cmake configuration in ```./CMakePresets.json``` that you can expand in ```./CMakeUserPresets.json```. By default, two configurations are present in the project (Debug and Release). Feel free to modify / add any configuration in the ***CMakeUserPresets.json*** file, as it is not synced through git.

Aside from managing cmake configurations, you can also manage your dependencies through the ***CMakeUserPresets.json*** file. The base file comes with a ***dependencies*** configuration that lets you declare paths and append them to ***CMAKE_PREFIX_PATH***. When setting up the project, make sure to update those paths.

## Project development

This section explains how to configure, build, test and package this project.

### How to configure the project

To configure the project using one of the available presets, go to the root directory of the project and run:

```> cmake --preset <preset>```

For a list of available presets for this project, please run:

```> cmake --list-presets```

### How to build the project

To build the project, configure the project and go to the ```./build/<preset>``` folder to run:

```> cmake --build .```

To build this project using multiple cores, run instead:

```> cmake -j<nb_cores> --build .```

### How to test the project

This project include various cases for testing purposes. These tests are implemented in the ```./test``` folder, and depend on ***Catch2*** (more info [here](https://github.com/catchorg/Catch2)). To enable the compilation of those tests, make sure to declare the ***BUILD_TESTS*** cmake variable in your presets or in the command line (```-DBUILD_TESTS```). Then, build the project.

To run these tests, go to the  ```./build/<preset>``` folder and run:

```> ctest```

### How to package the project

To package the project, configure the project and go to the ```./build/<preset>``` folder to run:

```> cmake --install .```

To select the folder in which to install this project, run instead:

```> cmake -DCMAKE_INSTALL_PREFIX=<install_path> --install .```

## Hints & Tips

If this section is empty, you're on your own. Your predecessor decided to move quickly... and leave you behind. Enjoy !

