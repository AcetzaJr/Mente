import subprocess


def run(target: str) -> int:
    return subprocess.run([f"./build/{target}"]).returncode
