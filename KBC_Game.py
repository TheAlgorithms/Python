#######This is the main KBC GAME ###########
questions = [
    ["What is the capital of Nepal?", "KTM", "Delhi", "Thimphu", "Beijing", 1],
    ["What is the capital of India?", "KTM", "Delhi", "Thimphu", "Beijing", 2],  
    ["What is the capital of Bhutan?", "KTM", "Delhi", "Thimphu", "Beijing", 3],
    ["What is the capital of China?", "KTM", "Delhi", "Thimphu", "Beijing", 4],
    ["What is the capital of Nepal?", "KTM", "Delhi", "Thimphu", "Beijing", 1],
    ["What is the capital of India?", "KTM", "Delhi", "Thimphu", "Beijing", 2],
    ["What is the capital of Bhutan?", "KTM", "Delhi", "Thimphu", "Beijing", 3],
    ["What is the capital of China?", "KTM", "Delhi", "Thimphu", "Beijing", 4],
    ["What is the capital of Nepal?", "KTM", "Delhi", "Thimphu", "Beijing", 1],
    ["What is the capital of India?", "KTM", "Delhi", "Thimphu", "Beijing", 2],
    ["What is the capital of Bhutan?", "KTM", "Delhi", "Thimphu", "Beijing", 3],
    ["What is the capital of China?", "KTM", "Delhi", "Thimphu", "Beijing", 4],
]

levels = [1000, 5000, 10000, 20000, 50000, 100000, 500000, 1000000, 2000000, 3000000, 10000000]
money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\n\nThis question is for {levels[i]} \n\n")
      # Initialize money for the current question
    
  
    
    print(f"\n\n{question[0]} \n \t 1.{question[1]}  \t 2.{question[2]} \n \t 3.{question[3]}  \t 4.{question[4]}")
    
    try :
        if i==2:
            money = 10000
        elif i == 4:
            money = 50000
        elif i == 7:
            money = 1000000
        elif i == 9:
            money = 10000000
        ans = int(input("Please enter your answer (1-4)n and if you want to quit press 0: "))
        if ans>4 :
            raise ValueError('hellooo')
        elif ans==0:
            money=levels[i-1]
            print(" you quitted")
            break 
        elif  ans>0 and ans<5 :    
            if ans == question[5]:  # Check if the answer is correct
                continue
            else:
                print(f"Sorry, the correct answer was option {question[5]}.")
                break
    except ValueError:
        print("Please enter a valid value.")
        break
print(f"\n\n  total money you won is {money}\n")
print("\t\t ***THANKS FOR PLAYING ****")
