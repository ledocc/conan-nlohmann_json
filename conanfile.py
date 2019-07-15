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

    build_requires = (("cmake_installer/3.14.5@conan/stable"),
                      ("ninja_installer/1.9.0@bincrafters/stable" ))

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
        self.run("ctest --output_on_failure --timeout=3000", cwd=cmake.build_folder)

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy("LICENSE.MIT", dst="licenses", ignore_case=True)


    def _configure_cmake(self):
        cmake = CMake(self, set_cmake_flags=True)
        cmake.generator="Ninja"
        cmake.verbose=True
        cmake.configure(source_dir="../json", build_dir="build")

        return cmake
