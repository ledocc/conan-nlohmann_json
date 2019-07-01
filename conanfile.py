from conans import ConanFile, tools, CMake

import os
import platform
import shutil



class NlohmannjsonConan(ConanFile):
    name = "nlohmann_json"
    version = "3.5.0"
    license = "MIT License"
    author = "David Callu - callu.david at gmail.com"
    url = "https://github.com/nlohmann/json"
    description = "JSON for Modern C++"
    topics = ("json", "c++")
    settings = "os", "arch", "compiler", "build_type"



    def source(self):
        dir_name = "json-"+self.version
        archive_name = "v"+self.version+".tar.gz"
        tools.download( "https://github.com/nlohmann/json/archive/"+archive_name, archive_name )
        tools.check_sha256( archive_name, "e0b1fc6cc6ca05706cce99118a87aca5248bd9db3113e703023d23f044995c1d")
        tools.untargz( archive_name )
        shutil.move( dir_name, "json" )
        os.unlink( archive_name )

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        cmake.test( output_on_failure=True )

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy("LICENSE.MIT", dst="licenses", ignore_case=True)


    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.verbose=True

        if platform.system() != "Windows":
            cmake.definitions["CMAKE_CXX_STANDARD"] = cmake.definitions["CONAN_CMAKE_CXX_STANDARD"]
            cmake.definitions["CMAKE_CXX_EXTENSIONS"] = cmake.definitions["CONAN_CMAKE_CXX_EXTENSIONS"]

        cmake.definitions["CTEST_TEST_TIMEOUT"] = "3000"
        cmake.configure(source_dir="../json", build_dir="build")

        return cmake
