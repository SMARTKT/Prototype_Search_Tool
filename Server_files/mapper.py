import re

class CreateLists():

	# compiles and stores all the regexes in the 'regex.txt' file in a list 'all_regex'
	def createRegexList(self,RegexFile):

		all_regex = list()

		with open(RegexFile) as rf:
			for line in rf:
				line = line.strip('\n')
				all_regex.append(re.compile(line,re.IGNORECASE))

		rf.close()

		return all_regex

	






# # stores all the templates in the 'templates.txt' file in a list 'all_templates' in string format
# 	def createTemplateList(self,TemplateFile):

# 		temp = list()
# 		all_templates = list()
# 		count = 0

# 		with open(TemplateFile) as tf:
# 			for line in tf:
# 				line = line.strip('\n')
# 				if line.startswith('--'):
# 					if count == 0:				#first template
# 						count += 1
# 						continue
# 					else:
# 						all_templates.append("\n".join(temp))
# 						temp = []
# 				else:
# 					temp.append(line)

# 		tf.close()
# 		all_templates.append("\n".join(temp))

# 		return all_templates


# 	# stores all the rules in the 'rules.txt' file in a list 'all_rules' in string format
# 	def createRuleList(self,RuleFile):

# 		temp = list()
# 		all_rules = list()
# 		count = 0

# 		with open(RuleFile) as tf:
# 			for line in tf:
# 				line = line.strip('\n')
# 				if line.startswith('--'):
# 					if count == 0:				#first template
# 						count += 1
# 						continue
# 					else:
# 						all_rules.append("\n".join(temp))
# 						temp = []
# 				else:
# 					temp.append(line)

# 		tf.close()
# 		all_rules.append("\n".join(temp))

# 		return all_rules

# stores all the rules in a list 'all_rule_list' in list form. This list is iterated and all the positions of place-holders are stored in a dictionary 'place_holder_position'
# def createRuleAsList(self,all_rules):

# 	place_holder_position = {key : [] for key in range(len(all_rules))}
# 	all_rule_list = list()

# 	for template_no,template in enumerate(all_rules):
# 		template = template.split('\n')
# 		for line_no,line in enumerate(template):
# 			template[line_no] = line.split()
# 			for word_no,word in enumerate(template[line_no]):
# 				if word.startswith('<<'):
# 					place_holder_position[template_no].append((line_no,word_no))

# 	all_rule_list.append(template)

# 	return all_rule_list, place_holder_position
