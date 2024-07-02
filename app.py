import subprocess


llama_command = "ollama run llama3:8b"


with open("input.txt", "r") as file:
    input_text = file.read()

additional_line = "explain it in three ways, 1.EASY(explain in simple terms), 2.EASIER(Explain it well to a newbie by changing some context.). 3 EASIEST(explain it to a 10 year old) and remeber to give these headings with each explanation so that blocks of these 3 answers can be differentiated in output file"

full_input_text = input_text + "\n" + additional_line


process = subprocess.Popen(llama_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output, error = process.communicate(full_input_text)

with open("llama_output.txt", "w") as file:
    file.write("LLAMA 3 Output:\n")
    file.write(output)


if error:
    print("Error:", error)
