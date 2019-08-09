from conans import ConanFile, tools, CMake


class NlohmannjsonConan(ConanFile):
    name = "nlohmann_json"
    version = tools.load("version.txt")
    license = "MIT License"
    author = "David Callu - callu.david at gmail.com"
    url = "https://github.com/nlohmann/json"
    description = "JSON for Modern C++"
    topics = ("json", "c++")
    settings = "os", "arch", "compiler", "build_type"
    homepage = "https://github.com/nlohmann/json"
    build_requires = (("cmake_installer/3.14.5@conan/stable"),
                      ("ninja_installer/1.9.0@bincrafters/stable" ))

    exports = ("version.txt")

    def source(self):
        archive_name = "v"+self.version+".tar.gz"
        tools.get( self.homepage+"/archive/"+archive_name,
                   sha256="80c45b090e40bf3d7a7f2a6e9f36206d3ff710acfa8d8cc1f8c763bb3075e22e")


    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        if self._should_build_test() and self._should_run_test():
            self.run("ctest --output_on_failure --timeout=3000", cwd=cmake.build_folder)

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy("LICENSE.MIT", dst="licenses", ignore_case=True)


    def _configure_cmake(self):
        cmake = CMake(self, set_cmake_flags=True)
        cmake.generator="Ninja"
        cmake.verbose=True
        if not self._should_build_test():
            cmake.definitions["BUILD_TESTING"]="OFF"

        cmake.configure(source_dir="../json-"+self.version, build_dir="build")
        return cmake

    def _should_build_test(self):
        if ( self.settings.get_safe("compiler") == "Visual Studio" ) and ( self.settings.get_safe("build_type") == "Debug" ) :
            self.output.warn("Skipping test : Visual Studio build in Debug mode fail to compile.")
            return False
        return True

    def _should_run_test(self):
        if tools.cross_building(self.settings):
            self.output.warn("Skipping test : cross built package.")
            return False
        return True
