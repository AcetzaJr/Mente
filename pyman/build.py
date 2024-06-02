import subprocess


def build(target: str, config: str) -> int:
    return subprocess.run(
        [
            "cmake",
            "--build",
            "build",
            "--config",
            config,
            "--target",
            target,
            "--parallel",
            "16",
        ]
    ).returncode
