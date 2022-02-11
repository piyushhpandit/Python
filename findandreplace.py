string= "she is beautiful and she is good dancer"
# print(string.replace(" ","_"))
# print(string.replace("is","was",1))
print(string.find("is"))
is_pose1 = string.find("is")
is_pos2 = string.find ("is", is_pose1 + 1)
print(is_pos2)