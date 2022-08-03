# CXX Project Template

## Overview

This project helps you kickoff new projects the easy way. This C++ project template creates ready-to-code project structures that support:
- [X] modern cmake project structure
- [X] executable & library packaging
- [X] unit tests using Catch2
- [ ] docker default development environments
- [ ] C++ package manager support

## Dependencies

This projects depends of **Catch2** ([github](https://github.com/catchorg/Catch2)) for test purposes.

## How to use

To use this template, clone it and run the following command :

```
python ./init/kickoff.py [project-type] [project-name]
```

For example, to kickoff a ```library``` project named ```mylib```, run the following command :

```
python ./init/kickoff.py library mylib
```

## Todo list

- [ ] Add DLL export capabilities in cmake scripts
- [X] Add executable support 
- [ ] Add docker support for development basic features (build, debug...)
- [ ] Add conan support for C++ dependency management
- [ ] Add static analysis support
- [ ] Add documentation generation tool support (e.g. doxygen)