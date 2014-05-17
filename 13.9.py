def main():
    input_raw = input("Enter an input filename to encrypt")
    output_raw = input("Enter an output filename to save to")

    user_in = open(input_raw,'rb')
    user_out = open(output_raw,'wb')

    user_out.write(bytes(bite-5 for bite in user_in.read()))

    user_out.close()
    user_in.close()



if __name__ == "__main__":
    main()
