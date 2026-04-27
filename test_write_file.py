from functions.write_file import write_file

def main():
    working_dir = "calculator"
    pkg_content = write_file(working_dir,  "lorem.txt", "wait, this isn't lorem ipsum")
    print(pkg_content + "\n")
    pkg_content = write_file(working_dir, "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(pkg_content + "\n")
    parent_dir_content = write_file(working_dir, "anotherPkg/temp.txt", "this should be allowed")
    print(parent_dir_content + "\n")
    erro_content = write_file(working_dir, "/tmp/temp.txt", "this should not be allowed")
    print(erro_content + "\n")

main()