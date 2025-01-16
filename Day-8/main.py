import art

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text,shift_amount,direction):
    main=""
    if (direction=='decode'):
        shift_amount*=-1
    for letter in original_text:
        if letter not in alphabet:
            main+=letter
        else:
            shifted_position=alphabet.index(letter)+shift_amount  # 0->3
            shifted_position%=len(alphabet)
            main+=alphabet[shifted_position]
    print(f"Here is the {direction}d Result:{main}")

continue_=True
while continue_:
    print(f"\n{art.logo}\n")
    #chooseing...
    direction=input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
    if(direction != 'encode' and direction != 'decode'):
        print("Try again")
        continue
    text=input("Type Your Message:\n").lower()  #input...
    shift=int(input("Type the shift number:\n"))   #shifting
    caesar(original_text=text,shift_amount=shift,direction=direction)
    inp=input("Type 'yes' if you want to go again, OtherWise, type 'no'.").lower()
    if(inp=='no'):
        continue_=False
        print(f"\n{art.goodbye}\n")