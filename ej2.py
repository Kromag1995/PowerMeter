import json

repetidos = [1,2,3,"1","2","3",3,4,5]
r = [1,"5",2,"3"]
d_str = '{"valor":125.3,"codigo":123}'

repetidos_1 = list(set(repetidos))
repetidos_2 = list(set(r).union(set(repetidos)))
d_str_3 = json.loads(d_str)
