class_names = ["jack", "bon", "andre", "galan"]

def data_set():
    import random
    num_enteries    = 5000000
    f   = open("data.txt", "w")
    for i in range(num_enteries):
        current = random.choice(class_names)
        f.write(current+"\n")
    f.close()

def read_data_list():
    class_count     = count()
    for c in class_names:
        class_count.append(0)
    with open("data.txt", "r") as f
        for line in f :
            line    = line.strip()
            if line != "":
                class_count[class_names.index(line)]+=1
    print(class_count)