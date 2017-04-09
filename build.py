import os
import sys
import subprocess

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def main(argv):
    if len(sys.argv) != 2:
        print("Invalid number of arguments, try python3 build.py <project_name>")
        sys.exit(1)

    my_path = get_script_path()
    project_name = sys.argv[1]
    print("Building '{}'".format(project_name))
    subprocess.run(["mkdir", "-p", project_name])
    subprocess.run(["curl", "https://raw.githubusercontent.com/anchovieshat/common_c_host/master/common.h", "-o", "common.h"], cwd=project_name)
    subprocess.run(["cp", "{}/starter_main".format(my_path), "{}/main.c".format(project_name)])
    subprocess.run(["cp", "{}/starter_build".format(my_path), "{}/build.sh".format(project_name)])
    subprocess.run(["cp", "{}/starter_gitignore".format(my_path), "{}/.gitignore".format(project_name)])

    pre_text = ""
    with open("{}/build.sh".format(project_name), "r") as build_file:
        pre_text = build_file.read().strip()
    with open("{}/build.sh".format(project_name), "w") as build_file:
        build_file.write("{} {}\n".format(pre_text, project_name))

    with open("{}/.gitignore".format(project_name), "a") as git_file:
        git_file.write("{}\n".format(project_name))

    subprocess.run(["chmod", "+x", "build.sh"], cwd=project_name)

    subprocess.run(["git", "init"], cwd=project_name)
    subprocess.run(["git", "add", "main.c", "build.sh", "common.h", ".gitignore"], cwd=project_name)
    print("{} is ready to go!".format(project_name))

if __name__ == "__main__":
    main(sys.argv[1:])
