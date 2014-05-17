def main():
    p = 1
    q = 3
    final_Number = 0
    for count in range(49):
        p += 2
        q += 2
        final_Number += (p/q)
        
    print("The final number is", final_Number)

if __name__ == "__main__":
    main()

    
        
        

