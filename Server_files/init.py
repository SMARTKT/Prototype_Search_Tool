from flask import Flask, render_template, flash, request, url_for, redirect
import random
import time
import rdflib
import query_run
import werkzeug
import xml.dom.minidom
from xml.dom.minidom import parse
from query_run import QueryConversion
from werkzeug.utils import secure_filename
from collections import defaultdict

RegexFile = '../Data files/regex.txt'

#FOR LIBPNG PROJECT

all_files = '../Data files/libpng_files.p'
all_name_tokens_dict = '../Data files/libpng_name_tokens_dict.p'
all_comment_tokens_dict = '../Data files/libpng_comment_tokens_dict.p'
program_domain_dict = '../Data files/libpng_program_domain_dict.p'
tf_idf_name_tokens = '../Data files/libpng_tf_idf_name_tokens.p'
tf_idf_symbol = '../Data files/libpng_tf_idf_symbol.p'
all_store_file = '../Data files/libpng_all_store.p'
TTLfile = '../TTL files/libpng TTL/final_2.ttl'

#FOR MRFS PROJECT

# all_files = '../Data files/mrfs_files.p'
# all_name_tokens_dict = '../Data files/libpng_name_tokens_dict.p'
# all_comment_tokens_dict = '../Data files/mrfs_comment_tokens_dict.p'
# program_domain_dict = '../Data files/libpng_program_domain_dict.p'
# tf_idf_name_tokens = '../Data files/mrfs_tf_idf_name_tokens.p'
# tf_idf_symbol = '../Data files/mrfs_tf_idf_symbol.p'
# all_store_file = '../Data files/mrfs_all_store.p'
# TTLfile = '../TTL files/mrfs TTL/final.ttl'

#FOR CURL PROJECT

# all_files = '../Data files/curl_files.p'
# all_name_tokens_dict = '../Data files/curl_name_tokens_dict.p'
# all_comment_tokens_dict = '../Data files/curl_comment_tokens_dict.p'
# program_domain_dict = '../Data files/curl_program_domain_dict.p'
# # tf_idf_name_tokens = '../Data files/mrfs_tf_idf_name_tokens.p'
# # tf_idf_symbol = '../Data files/mrfs_tf_idf_symbol.p'
# all_store_file = '../Data files/curl_all_store.p'
# TTLfile = '../TTL files/curl TTL/final.ttl'


#Load our TTL file here.
graph = rdflib.Graph()
start_time = time.time()
print("here")
graph.load(TTLfile, format='turtle')
end_time = time.time()
print("Time taken to load TTL",+end_time-start_time)

app = Flask(__name__)

# This function is responsible for the query system homepage. 
@app.route('/', methods = ['GET', 'POST'])
def homepage():                 ##kya ho rha hai idher

	if request.method == "POST":
		query = request.form.get('qry')
		file = request.files.get('file')

		print(query,file)
		if query:
			resp = get_response_single_query(query)
		else:
			filename = secure_filename(file.filename)
			file.save(filename)
			resp = get_response_query_file(filename)

		return render_template("main.html",resp=resp)

	return render_template("main.html")


# This is the main function that takes the query as input and calls the function "execute_query" in file "query_run.py" where all processing is done and final output is returned here.
def get_response_single_query(query):

	start_time = time.time()
	queryObj = QueryConversion(all_store_file,all_files,all_name_tokens_dict,all_comment_tokens_dict,program_domain_dict,tf_idf_name_tokens,tf_idf_symbol)
	ans = queryObj.execute_query(graph,TTLfile,RegexFile,query)
	end_time = time.time()
	print("Time taken",+end_time-start_time)

	return ans

# This is the main function that takes the query file as input and calls the function "execute_query_file" in file "query_run.py" where all processing is done and final output is returned here.
def get_response_query_file(filename):

	start_time = time.time()
	queryObj = QueryConversion(all_store_file,all_files,all_name_tokens_dict,all_comment_tokens_dict,program_domain_dict,tf_idf_name_tokens,tf_idf_symbol)
	ans = queryObj.execute_query_file(graph,TTLfile,RegexFile,filename)
	end_time = time.time()
	print("Time taken",+end_time-start_time)

	return ans


if __name__ == "__main__":
    app.run(host= '0.0.0.0')


