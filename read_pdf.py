from PyPDF2 import PdfReader
import re

reader = PdfReader("sample.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
    
barcode = r'RL.*'

try:
    
    found = re.findall(barcode, text, flags=re.IGNORECASE)
    
except AttributeError:
    
    found = '- #NotFound' 

print("---------------------------------------------")

for txt in found:
    string = str(txt).replace(' ', '')
    print(string)
#print(text)

print("---------------------------------------------")
