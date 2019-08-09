[![Download](https://api.bintray.com/packages/ledocc/public-conan/nlohmann_json%3Aledocc/images/download.svg) ](https://bintray.com/ledocc/public-conan/nlohmann_json%3Aledocc/_latestVersion)
[![Build Status Travis](https://travis-ci.org/ledocc/conan-nlohmann_json.svg) ](https://travis-ci.org/ledocc/conan-nlohmann_json)
[![Build Status AppVeyor](https://ci.appveyor.com/api/projects/status/github/ledocc/conan-nlohmann-json?svg=true) ](https://ci.appveyor.com/project/ledocc/conan-nlohmann-json)

## Conan package recipe for *nlohmann_json*

JSON for Modern C++

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/ledocc/public-conan/nlohmann_json%3Aledocc).


## Issues

If you wish to report an issue or make a request for a package, please do so here:

[Issues Tracker](https://github.com/ledocc/conan-nlohmann_json/issues)


## For Users

### Basic setup

    $ conan install nlohmann_json/3.6.1@ledocc/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    nlohmann_json/3.6.1@ledocc/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create . ledocc/stable


### Available Options
| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|


## Add Remote

    $ conan remote add ledocc https://api.bintray.com/conan/ledocc/public-conan


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package boost.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](LICENSE)
