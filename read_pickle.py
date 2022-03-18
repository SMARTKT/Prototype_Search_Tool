import pickle

read_file = 'Data files/curl_all_store.p'
file_new = pickle.load( open(read_file, "rb" ) )
print(file_new)
