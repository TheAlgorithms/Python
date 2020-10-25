# coding=utf-8

def selective_reading():
    archive = "insert the path here"
    with open(archive, 'r') as arch:
        for line in arch:
            line = line.partition('#')[0] # split the line into elements before "#" and after "#" 
            line = line.rstrip() # remove the after "#"
            print(line)

def main():
    selective_reading()

if __name__ == "__main__":
    main()