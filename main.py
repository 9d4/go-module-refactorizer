import os
import re
import sys


GO_REGEX = "\.go$"
OLD_MODULE_NAME = ""
NEW_MODULE_NAME = ""

Counter = 0


def usage_exit():
    print("Usage: python3 main.py <directory> <old_module_name> <new_module_name>")
    exit(1)


def get_dir():
    try:
        return sys.argv[1]
    except:
        return None


def get_old_module_name():
    try:
        return sys.argv[2]
    except:
        return None


def get_new_module_name():
    try:
        return sys.argv[3]
    except:
        return None


def get_module_names():
    global OLD_MODULE_NAME, NEW_MODULE_NAME

    OLD_MODULE_NAME = get_old_module_name()
    NEW_MODULE_NAME = get_new_module_name()
    if OLD_MODULE_NAME == None or NEW_MODULE_NAME == None:
        usage_exit()
    print("OLD: " + OLD_MODULE_NAME)
    print("NEW: " + NEW_MODULE_NAME)


def parse_dir(dir):
    if dir is None:
        return usage_exit()
    else:
        # join pwd with dir
        return os.path.join(os.getcwd(), dir)


# func to check dir exists
def check_dir(dir):
    if dir is None:
        return False
    else:
        if os.path.isdir(dir):
            return
        else:
            return usage_exit()


def replace_module(abs_path):
    global OLD_MODULE_NAME, NEW_MODULE_NAME, Counter

    print(abs_path)
    with open(abs_path, "r+") as f:
        content = f.read()

        if re.search(OLD_MODULE_NAME, content):
            content = re.sub(OLD_MODULE_NAME, NEW_MODULE_NAME, content)
            f.seek(0)
            f.write(content)
            f.truncate()
            Counter += 1


def replace_go_modules(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if re.search(GO_REGEX, file):
                replace_module(os.path.join(root, file))


# main func to run
def main():
    dir = get_dir()
    dir = parse_dir(dir)
    check_dir(dir)
    get_module_names()
    replace_go_modules(dir)
    print("DONE: " + str(Counter) + " files changed")


main()
