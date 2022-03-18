import time
import itertools
from itertools import permutations
import re

string = """
PREFIX prop: <http://smartKT/ns/properties#>
PREFIX function: <http://smartKT/ns/symbol/function#>

SELECT ?id ?type 
WHERE
{
 	<<SUBJECT>> <<PREDICATE>> <<OBJECT>> .
}
"""

pat = re.compile(r'SELECT(.*?)\n')
obj = pat.search(string,re.MULTILINE)
print(obj)

# place_holder_position = {key : [] for key in range(1)}		#dictionary to hold placeholder positions for every template
# templates = list()		#list of templates stored as string
# templates.append(string)
# all_template_list = list()  #list of templates stored as list


# for template_no,template in enumerate(templates):
# 	template = template.split('\n')
# 	for line_no,line in enumerate(template):
# 		template[line_no] = line.split()
# 		for word_no,word in enumerate(line):
# 			if word.startswith('<<'):
# 				place_holder_position[template_no].append((line_no,word_no))

# 	all_template_list.append(template)

# template_id = 0
# positions = place_holder_position[template_id]

# start_time = time.time()

# for position in positions:
# 	x = position[0]
# 	y = position[1]

# temp = list()
# for line in all_template_list[template_id]:
# 	string = ' '.join(line)
# 	temp.append(string)

# sparql = '\n'.join(temp)

# end_time = time.time()

# print(sparql)
# print("Time taken",+end_time-start_time)

# start_time = time.time()

# holder_list = re.findall("<<.*?>>", string)

# for placeholder in holder_list:
# 	string = string.replace(placeholder,'function')

# end_time = time.time()

# print(sparql)
# print("Time taken",+end_time-start_time)
