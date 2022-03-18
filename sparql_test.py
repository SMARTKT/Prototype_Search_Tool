filename = "/home/manad/SmartKT/smartKT/NEW_TTL/TTL files/libpng TTL/final.ttl"
import rdflib
from collections import defaultdict
g = rdflib.Graph()
print(type(g))
g.parse(filename, format='ttl')

print(type(g))
# print(result)
# query = """
#     PREFIX prop: <http://smartKT/ns/properties#>
#     PREFIX symbol: <http://smartKT/ns/symbol#>

#     SELECT DISTINCT ?seqid ?obj1 ?threadid ?name
#     WHERE
#     {
#         ?seqid prop:is_a ?obj1.
#         ?seqid prop:thread_id ?threadid.
#         ?seqid prop:var_name ?name.
#         {
#             SELECT DISTINCT ?seqid
#             WHERE
#              {
#                 ?seqid prop:var_id ?obj.
#                 FILTER (?obj = ?symbol)
#                 {
#                     SELECT DISTINCT ?symbol
#                     WHERE
#                     {
#                         ?symbol prop:is_a "VarDecl".
#                         ?symbol prop:is_defined_file "http.c".
#                         ?symbol prop:comment_token "copyright".
#                         ?symbol prop:comment_token "daniel".
#                     }   
#                 }
#              }  
#         }
#     }	
# """

query1 =  """
            
            PREFIX prop: <http://smartKT/ns/properties#> 
            PREFIX symbol: <http://smartKT/ns/symbol#> 

            SELECT DISTINCT ?id ?pred ?obj
                    WHERE
                    {
                        ?id ?pred ?obj ;
                    prop:is_defined_file "png.c";   
                    prop:is_a "VarDecl".
                    } """

query2 =  """

PREFIX prop: <http://smartKT/ns/properties#> 
PREFIX symbol: <http://smartKT/ns/symbol#> 

SELECT DISTINCT ?id ?pred ?obj
        WHERE
        {
            ?id ?pred ?obj ;
        prop:is_defined_file "png.c";   
        prop:is_a "VarDecl".
                    FILTER (?pred IN (
                    prop:storage_class, 
                    prop:is_defined_file, 
                    prop:type, prop:spelling, 
                    prop:is_a, 
                    prop:isDef_file_line, 
                    prop:isDecl_file_line, 
                    prop:linkage_kind, 
                    prop:isUse_file_line, 
                    prop:is_array, 
                    prop:array_size, 
                    prop:is_pointer, 
                    prop:is_subclass_of, 
                    prop:is_friend_of) ). 
        } """

result = g.query(query1)
print(type(result))
# result_dict = defaultdict(dict)
# for stmt in result:
#     print(stmt)
#     print(stmt['id'])
#     print(stmt['pred'])
#     print(stmt['obj'])
    # row = stmt
    # curr_id = row['id'].split('#')[1]
    # if curr_id == "2304229297849":
    #     print(row)
    #     print('\n')
    #     print(str(row['pred'].split('#')[1]))
    #     if str(row['pred'].split('#')[1]) == "isUse_file_line":
    #         if "isUse_file_line" in result_dict[curr_id].keys():
    #             result_dict[curr_id][str(row['pred'].split('#')[1])].append(str(row['obj']))
    #         else:
    #             temp = []
    #             temp.append(str(row['obj']))
    #             result_dict[curr_id][str(row['pred'].split('#')[1])] = temp

    #     else:
    #         result_dict[curr_id][str(row['pred'].split('#')[1])] = str(row['obj'])


# for key in result_dict:
#     if key == "2304229297849":
#         print(result_dict[key])
#         print('\n')

# myset = set()

# myset.add("abc")
# myset.add("cda")
# print(myset)
# for item in myset:
#     print(item)

# scores = defaultdict(dict)
# scores["manad"] = 4
# scores["saloni"] = 7
# scores["dhruv"] = 45

# sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

# print(type(sorted_scores))
        

# for w in sorted(scores, key=scores.get, reverse=True):S
#     print(w, scores[w])
# # query = """
#     PREFIX prop: <http://smartKT/ns/properties#> 
#             PREFIX symbol: <http://smartKT/ns/symbol#> 

#             SELECT DISTINCT ?id ?pred ?obj
#                     WHERE
#                     {
#                         ?id ?pred ?obj ;
#                     prop:is_defined_file "png.c";
#                     prop:is_a "VarDecl".
#                                 FILTER (?pred IN (prop:storage_class, prop:is_defined_file, prop:type, prop:spelling, prop:is_a, prop:is_array, prop:array_size, prop:is_pointer, prop:is_subclass_of, prop:is_friend_of) ) . 
#         } """

