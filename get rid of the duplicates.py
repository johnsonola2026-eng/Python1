student_data={
"id1":{"name":"sara","class":"V","subject":"english,math,science"},
"id2":{"name":"david","class":"V","subject":"english,math,science"},
"id3":{"name":"sara","class":"V","subject":"english,math,science"},
"id4":{"name":"surya","class":"V","subject":"english,math,science"},}
result={}
seen_keys=[]
for student_id, details in student_data.items():
    unique_key=(details["name"], details["class"], details["subject"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result [student_id] = details
for k,v in result.items():
    print(k,":",v)