import subprocess

from pyman.check import check_in_options as check


def init(config: str) -> int:
    result = check(
        tag="configuration",
        options=["Debug", "Release", "RelWithDebInfo", "MinSizeRel"],
        value=config,
    )
    if result is None:
        return 1
    match result:
        case "Debug":
            print(
                "> CMAKE_BUILD_TYPE -> Debug: Disable optimizations - include debug information"
            )
        case "Release":
            print(
                "> CMAKE_BUILD_TYPE -> Release: Optimize for speed - exclude debug information"
            )
        case "RelWithDebInfo":
            print(
                "> CMAKE_BUILD_TYPE -> RelWithDebInfo: Optimize for speed - include debug information"
            )
        case "MinSizeRel":
            print(
                "> CMAKE_BUILD_TYPE -> MinSizeRel: Optimize for smallest binary size - exclude debug information"
            )
    args = [
        "cmake",
        "-S=.",
        "-B=build",
        f"-DCMAKE_BUILD_TYPE={config}",
        "-DCMAKE_C_COMPILER=gcc",
        "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
    ]
    return subprocess.run(args).returncode
