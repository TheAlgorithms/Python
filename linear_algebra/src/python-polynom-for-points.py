def points_to_polynomial(coordinates[][]):
    #the list is two dimensional: [[x, y],[x, y],...]
    
    from decimal import *
    getcontext()
    getcontext().prec=28

    if __name__ == __main__ :
        #number of points you want to use
        try:
            d=coordinates[0][0]
            for j in range(len(coordinates)):
                if j==0:
                    continue
                if d==coordinates[j][0]:
                    more_check+=1
                    solved="x="+str(coordinates[j][0])
                    if more_check == len(coordinates)-1:
                        check=2
                        break
                    elif more_check > 0 and more_check != len(coordinates)-1:
                        check=3
                    else:
                        check=1

            if len(coordinates)==1 and coordinates[0][0]==0:
                check=2
                solved="x=0"
        except:
            check=3

        if check==1:
            count_of_line=0
            matrix=[]
            #put the x and x to the power values in a matrix
            while count_of_line < x:
                count_in_line=0
                a=coordinates[count_of_line][0]
                count_line=[]
                while count_in_line < x:
                    count_line.append(a**(x-(count_in_line+1)))
                    count_in_line+=1
                matrix.append(count_line)
                count_of_line+=1

            count_of_line=0
            #put the y values into a vector
            vector=[]
            while count_of_line < x:
                count_in_line=0
                vector.append(coordinates[count_of_line][1])
                count_of_line+=1

            count=0

            while count < x:
                zahlen=0
                while zahlen < x:
                    if count==zahlen:
                        zahlen+=1
                    if zahlen==x:
                        break
                    bruch=(matrix[zahlen][count])/(matrix[count][count])
                    counting_columns=0
                    for i in range(len(matrix[count])):
                        #manipulating all the values in the matrix
                        matrix[zahlen][counting_columns]-=(matrix[count][i])*bruch
                        counting_columns+=1
                    #manipulating the values in the vector
                    vector[zahlen]-=vector[count]*bruch
                    zahlen+=1
                count+=1

            count=0
            #make solutions
            solution=[]
            while count < x:
                solution.append(vector[count]/matrix[count][count])
                count+=1

            count=0
            solved="f(x)="

            while count < x:
                remove_e=str(solution[count]).split("E")
                if len(remove_e) > 1:
                    solution[count]=remove_e[0]+"*10^"+remove_e[1]
                solved+="x^"+ str(x-(count+1))+ "*" +str(solution[count])
                if count+1 != x:
                    solved+="+"
                count+=1

            return solved

        elif check==2:
            return solved
        else:
            return "The program cannot work out a fitting polynomial."
