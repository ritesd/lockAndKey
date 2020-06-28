''' Just copy and paste in ipython or run as script file anyway it is not complete code for submission ..final code in kt is coming'''
# input_dict = {0:[6,8,2], 1:[6,1,4], 2:[2,0,6], 3:[7,3,8], 4:[7,8,0]}
input_dict = {0:[2,9,1], 1:[2,4,5], 2:[4,6,3], 3:[5,7,8], 4:[5,6,9]}
#input_dict = {0:[5,4,8], 1:[8,0,6], 2:[1,5,7], 3:[5,3,0], 4:[6,4,7]}
# input_dict = {0:[1,8,9], 1:[1,4,7], 2:[9,6,5], 3:[5,2,3], 4:[2,8,6]}

class LockAndKey:

    def __init__(self, input_dict):
        self.input_dict = input_dict
        num_list = []
        for value in input_dict.values():num_list.extend(value)
        self.result_dict = {key: {"index": [], "occurence_value": 0.0, "is_position": False, "is_active": True, "is_fixed":False} for key in set(num_list)}

    def condition_three(self):
        for v_num in self.input_dict[3]:
            self.result_dict[v_num]["is_active"] = False

    def condition_zero(self):
        value = 3
        for v_num in self.input_dict[0]:
            if not self.result_dict[v_num]["is_active"]:
                value -= 1
        for index, v_num in enumerate(self.input_dict[0]):
            if self.result_dict[v_num]["is_active"]:
                self.result_dict[v_num]["occurence_value"] = 1/value
                self.result_dict[v_num]["is_position"] = True
                self.result_dict[v_num]["index"].append(index)

    def condition_one(self):
        value = 3
        for index, v_num in enumerate(self.input_dict[1]):
            if not self.result_dict[v_num]["is_active"]:
                value -= 1
                continue
            if self.result_dict[v_num]["is_position"] and index==self.result_dict[v_num]["index"][-1]:
                value -=1
                self.result_dict[v_num]["is_active"] = False
            if self.result_dict[v_num]["is_position"] and index!=self.result_dict[v_num]["index"][-1]:
                value = -2
        for index, v_num in enumerate(self.input_dict[1]):
            if self.result_dict[v_num]["is_active"] and self.result_dict[v_num]["is_position"] and index!=self.result_dict[v_num]["index"][-1]:
                self.result_dict[v_num]["occurence_value"] += 1
                break
            if self.result_dict[v_num]["is_active"]:
                self.result_dict[v_num]["occurence_value"] += 1/value
                if value == 1:
                    self.result_dict[v_num]["is_fixed"]=True
            if self.result_dict[v_num]["is_active"] and not self.result_dict[v_num]["is_position"]:
                self.result_dict[v_num]["index"].append(index)
    def condition_two(self):
        value = 3
        for index, v_num in enumerate(self.input_dict[2]):
            if not self.result_dict[v_num]["is_active"]:
                value -= 1
                continue
            if self.result_dict[v_num]["is_position"] and index==self.result_dict[v_num]["index"][-1]:
                value -=1
                self.result_dict[v_num]["is_active"] = False
        for index, v_num in enumerate(self.input_dict[2]):
            if self.result_dict[v_num]["is_active"]:
                self.result_dict[v_num]["occurence_value"] += 2/value
                if value == 2:
                    self.result_dict[v_num]["is_fixed"]=True
            if self.result_dict[v_num]["is_active"] and not self.result_dict[v_num]["is_position"]:
                self.result_dict[v_num]["index"].append(index)
    def condition_four(self):
        value = 3
        for index, v_num in enumerate(self.input_dict[4]):
            if not self.result_dict[v_num]["is_active"]:
                value -= 1
                continue
            if self.result_dict[v_num]["is_position"] and index==self.result_dict[v_num]["index"][-1]:
                value -=1
                self.result_dict[v_num]["is_active"] = False
                continue
            if self.result_dict[v_num]["is_position"] and index!=self.result_dict[v_num]["index"][-1]:
                value = -3
            if self.result_dict[v_num]["is_fixed"]:
                for i in filter(lambda x: x!= v_num, self.input_dict[4]): self.result_dict[i]["is_active"]=False

        for index, v_num in enumerate(self.input_dict[4]):
            if self.result_dict[v_num]["is_active"] and self.result_dict[v_num]["is_position"] and index!=self.result_dict[v_num]["index"][-1]:
                self.result_dict[v_num]["occurence_value"] += 1
                break
            if self.result_dict[v_num]["is_active"]:
                self.result_dict[v_num]["occurence_value"] += 2/value
            if self.result_dict[v_num]["is_active"] and not self.result_dict[v_num]["is_position"]:
                self.result_dict[v_num]["index"].append(index)

a = LockAndKey(input_dict)
a.condition_three()
a.condition_zero()
a.condition_one()
a.condition_two()
a.condition_four()
s_dict = list(filter(lambda x: x[1]["is_active"], a.result_dict.items()))


#three_num = sorted(s_dict, key=lambda x: x[1]["occurence_value"], reverse=True)[0:3]
index_dict = {}
index_list = [0,1,2]


first_num = max(list(filter(lambda x: x[1]["is_position"],s_dict)), key=lambda x: x[1]["occurence_value"])
index_dict[first_num[1]["index"][-1]] = first_num[0]
index_list.remove(first_num[1]["index"][-1])

second_num = max(list(filter(lambda x: len(x[1]["index"]) > 1 and not x[1]["is_position"],s_dict)), key=lambda x: x[1]["occurence_value"])
for index in index_list:
    if index not in second_num[1]["index"]:
        index_dict[index] = second_num[0]
        index_list.remove(index)
        break

#third_num = list(filter(lambda x: x[0] not in index_dict.values(), s_dict))[0]
third_num = max(list(filter(lambda x: x[0] not in index_dict.values() and x[1]["index"]!=index_list, s_dict)), key=lambda x: x[1]["occurence_value"])
index_dict[index_list[-1]] = third_num[0]

key = []
for k, value in index_dict.items():
    key.insert(k, str(value))

print("".join(key))
