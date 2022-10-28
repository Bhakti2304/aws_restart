"""
Preparing to Analyze Insulin with Python
"""
import re

file = open("/home/ec2-user/environment/preproinsulin-seq.txt",'r')
data = file.read()

#print(data)


my_string=re.sub(r'[^\w]', '', data)
sol = re.sub(r'[~^0-9]', '', my_string)
new_String= re.sub(r'ORIGIN', '', sol)
print(new_String)

text_file = open("/home/ec2-user/environment/preproinsulin-seq-clean.txt", "w")
text_file.write(new_String)

#new_String= "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"


count=0
for i in new_String:
      if(i.islower()):
            count=count+1
print("The number of lowercase characters is:",count)


first_char=new_String[0:25]
print('signal sequence : ', first_char)
text_file = open("/home/ec2-user/environment/lsinsulin-seq-clean.txt", "w")
text_file.write(first_char)
text_file.close()

second_char=new_String[26:55]
print('Amino acids : ', second_char)
text_file = open("/home/ec2-user/environment/binsulin-seq-clean.txt", "w")
text_file.write(second_char)

third_char=new_String[56:90]
print('proinsulin molecule : ', third_char)
text_file = open("/home/ec2-user/environment/cinsulin-seq-clean.txt", "w")
text_file.write(third_char)

forth_char=new_String[91:111]
print('amino acids-processed insulin molecule : ', forth_char)
text_file = open("/home/ec2-user/environment/ainsulin-seq-clean.txt", "w")
text_file.write(forth_char)