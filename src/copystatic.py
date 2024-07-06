import os
import shutil


def copy_static_files(from_dir, to_dir):
    # Make sure both paths exist
    if not os.path.exists(from_dir):
        raise ValueError(f"`from_dir` path does not exist: {from_dir}")

    if not os.path.exists(to_dir):
        os.mkdir(to_dir)

    # Get list of files to copy
    files = os.listdir(from_dir)
    for file in files:
        src = os.path.join(from_dir, file)
        dst = os.path.join(to_dir, file)
        if os.path.isfile(src):
            shutil.copy(src, dst)
            print(f"* copied {src} -> {dst}")
        else:
            copy_static_files(f"{src}/", f"{dst}/")
