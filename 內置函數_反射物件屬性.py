

l =['asdfads',124,'asdf123']
l2=[]





if __name__ == '__main__':

    for i in l:
        if type(i) is str:
            tmp_str=''
            for s in i:
                if s.isdigit() == False:
                    tmp_str += s
            l2.append(tmp_str)

        elif type(i) is int:
            l2.append(i)
    print(l2)


    print(isinstance(l,list))

