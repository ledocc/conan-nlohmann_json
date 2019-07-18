from cpt.packager import ConanMultiPackager
import platform



if __name__ == "__main__":
    builder = ConanMultiPackager(
        reference = "nlohmann_json/"+tools.load("version.txt")
        channel = "testing"
        stable_branch_pattern = "release/*"
    )
    builder.add_common_builds(pure_c=False)

    filtered_items = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        settings["compiler.cppstd"] = "11"
        if settings["compiler"] == "gcc":
            settings["compiler.libcxx"] = "libstdc++11"
        elif ( settings["compiler"] == "clang" ) and ( "compiler.libcxx" in settings ) and ( settings["compiler.libcxx"] == "libstdc++" ):
            settings["compiler.libcxx"] = "libstdc++11"
        filtered_items.append([settings, options, env_vars, build_requires, reference])
    builder.items = filtered_items

    builder.run()
