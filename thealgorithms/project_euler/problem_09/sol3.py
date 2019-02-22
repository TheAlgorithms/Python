def main():
    print([a*b*c for a in range(1,999) for b in range(a,999) for c in range(b,999) 
    if (a*a+b*b==c*c) and (a+b+c==1000 ) ][0])
  
if __name__ == '__main__':
    main()
