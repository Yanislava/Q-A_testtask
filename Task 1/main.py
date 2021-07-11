import os.path
import shutil
import xml.etree.ElementTree as ET

config_file = "config.xml"

if __name__ == "__main__":
    try:
        tree = ET.parse(config_file)
        root = tree.getroot()

        for line in root:
            name = line.get("file_name")
            source = line.get("source_path")
            destination = line.get("destination_path")
        print(name)
        print(source)
        print(destination)

        if not os.path.exists(destination):
            try:
                os.mkdir(destination)
            except:
                print(f"The path {destination} is unreachable\n"
                        f"or you are not allowed to make a new directory")
        else:
            if os.path.exists(source + name):
                if os.path.exists(destination + name):
                    print(f"File {name} already exists in directory {destination}")

                    copy = True
                    while copy:
                        rewrite = input("Do you want to overwrite the existing file?\n"
                                        "Type 'y' or 'n'.\n")
                        if rewrite == "y":
                            shutil.copyfile(source + name, destination + name)
                            print(f"File {name} has been successfully rewritten in {destination} directory")
                            copy = False
                        elif rewrite == "n":
                            print("Copying has been canceled by user")
                            copy = False
                        else:
                            print("Invalid input. Please Type 'y' or 'n'")
                else:
                    shutil.copyfile(source + name, destination + name)
                    print(f"File {name} has been successfully copied in {destination} directory")

            else:
                print("File not found")

    except FileNotFoundError:
        print("Can't find config file")
else:
    print("You cannot use this program as a module")
