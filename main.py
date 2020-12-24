from art import logo
from coding_words import alphabet


print(logo)

print("\n")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
print("\n")
text = input("Type your message:\n").lower()
print("\n")
shift = int(input("Type the shift number:\n"))
print("\n")




def Caesar(start_text,shift_amount,cipher_direction):
  if shift_amount>=25:
    shift_amount = shift_amount%25
  cipher_text = ""
  for char in start_text:
    if char  in alphabet:
      position = alphabet.index(char)
      if direction.lower() == "encode":
        new_position = position + shift_amount
      elif direction.lower() == "decode":
        new_position = position - shift_amount
      new_letter = alphabet[new_position]
      cipher_text += new_letter
    else:
      cipher_text += char
  print(f"The {direction}d text is {cipher_text}")
  print("\n")


Caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
user_choice = input("Type 'yes' if you want to go again.Otherwise type 'no'")

if user_choice == "yes":
  while user_choice.lower() == "yes":

    print("\n")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    print("\n")
    text = input("Type your message:\n").lower()
    print("\n")
    shift = int(input("Type the shift number:\n"))
    Caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    user_choice = input("Type 'yes' if you want to go again.Otherwise type 'no'\n")
else:
  print("\n")
  print("Good bye")
 

  

  





  


