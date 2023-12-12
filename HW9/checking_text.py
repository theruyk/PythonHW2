import subprocess
from typing import Tuple
def checking_text(command: str, text: str) -> bool:
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout
        return text in output
    except subprocess.CalledProcessError:
        return False


print(checking_text('echo "Hello, world!"', 'Hello, world!')) #True
#print(testing_text( 'not_a_comand', 'Hello, world!'))# False