import re

with open("max_procedures.txt","r") as fi:
    temp_text = fi.read()
temp_text = re.sub(r'\n+', '\n', temp_text)
temp_text = re.sub(r'\. ', '.\n', temp_text)
result = '\n'.join(temp_text.split('\n')[:])
text = result + "\n=\n"
with open("max_procedures_lines.txt","w") as fi:
    fi.write(text)