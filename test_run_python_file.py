from functions.run_python_file import run_python_file

def main():
    working_dir = "calculator"
    result_main_output = run_python_file(working_dir,  "main.py")
    print(result_main_output)
    
    result_main_output = run_python_file(working_dir,  "main.py", ["3 + 5"])
    print(result_main_output)

    result_main_output = run_python_file(working_dir,  "tests.py")
    print(result_main_output)

    result_main_output = run_python_file(working_dir,  "../main.py")
    print(result_main_output)

    result_main_output = run_python_file(working_dir, "nonexistent.py")
    print(result_main_output)

    result_main_output = run_python_file(working_dir,  "lorem.txt")
    print(result_main_output)
   
main()