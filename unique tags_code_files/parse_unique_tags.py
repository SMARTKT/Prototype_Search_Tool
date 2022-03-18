import xml.dom.minidom
from xml.dom.minidom import parse
from collections import defaultdict 

filename = 'inherit_comb.xml'


def recursively_add_spellings(unique_tags,file):

	for child in file.childNodes:
		if child.nodeType != child.TEXT_NODE:				
			unique_tags[child.tagName].add(child.getAttribute("spelling"))
			recursively_add_spellings(unique_tags,child)
			

unique_tags = defaultdict(set)

DOMTree = xml.dom.minidom.parse(filename)
collection = DOMTree.documentElement

print(collection)
files = collection.getElementsByTagName("TranslationUnit")
# print(files)

for file in files:
	recursively_add_spellings(unique_tags,file)


f = open("extern_clang.txt", "w")
f.write("------------LIST OF UNIQUE TAGS------------"+"\n"+"\n")
	

for keys,value in unique_tags.items():
	f.write(keys+"\n")

f.write("\n"+"------------LIST OF TAGS WITH NO SPELLING------------"+"\n"+"\n")


for keys,value in unique_tags.items():
	if(len(value)<=1):
		f.write(keys+"\n")

f.close()