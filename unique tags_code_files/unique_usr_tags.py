import xml.dom.minidom
from xml.dom.minidom import parse
from collections import defaultdict 

filename = 'inherit_comb.xml'


def recursively_add_tags(tags_with_usr,tags_with_other_usr,tags_with_no_usr,file):

	for child in file.childNodes:
		if child.nodeType != child.TEXT_NODE:
			if(child.hasAttribute("usr")):				
				tags_with_usr.add(child.tagName)
			elif(child.hasAttribute("ref_usr") or child.hasAttribute("def_usr")):
				tags_with_other_usr.add(child.tagName)
			else:
				tags_with_no_usr.add(child.tagName)

			recursively_add_tags(tags_with_usr,tags_with_other_usr,tags_with_no_usr,child)
			

tags_with_usr = set()
tags_with_other_usr = set()
tags_with_no_usr = set()

DOMTree = xml.dom.minidom.parse(filename)
collection = DOMTree.documentElement

print(collection)
files = collection.getElementsByTagName("TranslationUnit")
# print(files)

for file in files:
	recursively_add_tags(tags_with_usr,tags_with_other_usr,tags_with_no_usr,file)


f = open("usr_tag_list.txt", "w")
f.write("------------LIST OF TAGS WITH USR------------"+"\n"+"\n")
	

for tags in tags_with_usr:
	f.write(tags+"\n")

f.write("\n"+"------------LIST OF TAGS WITH NO USR BUT HAVE DEF_USR OR REF_USR------------"+"\n"+"\n")

for tags in tags_with_other_usr:
	f.write(tags+"\n")

f.write("\n"+"------------LIST OF TAGS WITH NO KINDS OF USR------------"+"\n"+"\n")

for tags in tags_with_no_usr:
	f.write(tags+"\n")

f.close()