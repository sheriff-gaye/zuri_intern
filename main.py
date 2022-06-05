
def read_file_content(filename):
    # [assignment] Add your code here 

    with open (filename,'r') as f:
        file_name=f.read()
    
    return file_name


def count_words():
    text = read_file_content("./shertiff.txt")

    text=text.lower()

    list_of_words=text.split()

    result={}

    for words in list_of_words:
        if words in result.keys():

            result[words]+=1

        elif words=="":
            pass

        else:

            result[words]=1


    print(result)

count_words() 


