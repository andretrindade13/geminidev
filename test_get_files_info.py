from functions.get_files_info import get_files_info

def main():
    working_dor = "calculator"
    root_content = get_files_info(working_dor)
    print(root_content + "\n")
    pkg_content = get_files_info(working_dor, "pkg")
    print(pkg_content + "\n")
    pkg_content = get_files_info(working_dor, "calculator.py")
    print(pkg_content + "\n")
    erro_content = get_files_info(working_dor, "/bin")
    print(erro_content + "\n")
    erro2_content = get_files_info(working_dor, "../")
    print(erro2_content + "\n")

main()