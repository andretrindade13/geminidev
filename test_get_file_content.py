from functions.get_file_content import get_file_content

def main():
    working_dir = "calculator"

    content_main = get_file_content(working_dir, "main.py")
    print(f"content_main {content_main} \n")
    content_calculator = get_file_content(working_dir, "pkg/calculator.py")
    print(f"content_calculator {content_calculator} \n")
    content_error = get_file_content(working_dir, "/bin/cat")
    print(f"content_error {content_error} \n")
    content_error2 = get_file_content(working_dir, "pkg/does_not_exist.py")
    print(f"content_error2 {content_error2} \n")
    
main()