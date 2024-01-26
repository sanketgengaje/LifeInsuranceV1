import PyPDF2
import re

file = open(r'C:\pdf_reader\pdf_extractor\result.pdf', 'rb')
reader = PyPDF2.PdfFileReader(file)
page1=reader.getPage(0)
print(reader.numPages)
list = (page1.extractText().split('\n'))
print(list)
print("------------------------------")

compare_option = list.index('Age of Life Assured')
print(compare_option)
act_result = (compare_option+1)
print(list[compare_option]+": "+ list[act_result])
print("------------------------------")

compare_option = list.index('Pay')
print(compare_option)
act_result = (compare_option+1)
print(list[compare_option]+": "+ list[act_result])
print("------------------------------")

compare_option = list.index('Policy Term (years)')
print(compare_option)
act_result = (compare_option+1)
print(list[compare_option]+": "+ list[act_result])
print("------------------------------")

compare_option = list.index('Annualized Premium')
print(compare_option)
act_result = (compare_option+1)
print(list[compare_option]+": "+ list[act_result])
print("------------------------------")

compare_option = list.index('Policy Op\x16on')
a = list[compare_option+1]
print(a)
# a = 'Opon 2: Extra Life Cover (Life Cover with Accidental Death Beneﬁt)'
b =a.split("(")
c = b[0].split(":")
act_result = c[1].lstrip()
print(list[compare_option]+": "+ act_result)
# print(re.split("()]", a))
