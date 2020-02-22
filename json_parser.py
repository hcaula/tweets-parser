file_name = "./showdopavao_1_2020-02-22T15_59_11.json"
new_file_name = "./parsed/showdopavao_1.json"

with open(file_name, "r") as r:
  data = r.read()
  data = data.replace("\n{", ",\n{")
  data = "[{}]".format(data)

  with open(new_file_name, "w") as w:
    w.write(data)

