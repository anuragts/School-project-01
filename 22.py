# Remove all the lines that contain the word "a" in a file and write it into another file.

def remove_line():
    file1 = open("file1.txt", "r")
    file2 = open("file2.txt", "w")
    for line in file1:
        if "a" not in line:
            file2.write(line)
        else:
            line = line.replace("a", " ")

    file1.close()
    file2.close()
remove_line()
