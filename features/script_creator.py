import subprocess
import os
import re

class ScriptCreator:
    
    def __init__(self):
        self.python_scripts_folder = "generated_scripts"
        os.makedirs(self.python_scripts_folder, exist_ok=True)
        

    def extract_python_code(self, response):
        # Regular expression pattern
        pattern = r"```python(.*?)```"
        
        # To find all code blocks in the input text
        code_blocks = re.findall(pattern, response, re.DOTALL)
        
        # Code blocks are joined into a single string
        extracted_code = "\n".join(code_blocks)
        
        return extracted_code


    def generate_python_script(self, response):
        # Generate the Python script here
        python_script = self.extract_python_code(response)
        
        counter = 1
        
        while True:
            script_file_path = os.path.join(self.python_scripts_folder, f"generated_script_{counter}.py")
            
            if not os.path.exists(script_file_path):
                break
                
            counter += 1

        with open(script_file_path, "w") as script_file:
            script_file.write(python_script)

        return script_file_path
    
    
    def run_generated_script(self, response):
        
        script_file_path = self.generate_python_script(response)

        # Execute the generated Python script
        try:
            subprocess.run(["python", script_file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the script: {e}")
        



if __name__ == "__main__":
    
    # creator = ScriptCreator()

    # prompt = """
    # Here is some text before the code block.

    # ```python
    # print("Hello, World!")
    # x = 10
    # y = 20

    # def add(x, y):
    #     return x + y
        
    # z = add(x, y)

    # print(z)
    # ```
    # Text after the code
    # """
    command = "calculate the sum of 10 and 20"
    command = "Write a python script for me. I want it to " + command
    
    print(command)
    pass


    