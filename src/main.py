import os
import shutil

from copystatic import copy_static_files
from generate_page import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    # Delete contents of public directory to be idempotent
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_static_files(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "/index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )


main()
