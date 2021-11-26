import csv
# https://kaworu.jpn.org/kaworu/2018-06-02-1.php#2018-06-02-1-06a2d1c6c23ae1b0658b6752c409944d


# data = read("text.txt")
def read(filename):
  f = open(filename, "r")
  reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) #クオーテーションで囲まれているものは文字として認識
  data = [ e for e in reader]

  # 数字はfloat型で出力される
  return data


# write("test.txt", 'a', data=["string", 1, 3, 4])
def write(filename, type, data):
    with open(filename, type, newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(data)
