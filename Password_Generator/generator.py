import random

user = input('User: ')
long = input('Password length: ')
choice = input(str('Use Symbols (@, #, $, %) ? (Y or N)'))
password = []

letter = list('1' '2' '3' '4' '5' '6' '7' '8' '9' '0'
              'q' 'w' 'e' 'r' 't' 'y' 'u' 'i' 'o' 'p'
              'a' 's' 'd' 'f' 'g' 'h' 'j' 'k' 'l' 'z'
              'x' 'c' 'v' 'b' 'n' 'm' 'Q' 'W' 'E' 'R'
              'T' 'Y' 'U' 'I' 'O' 'P' 'A' 'S' 'D' 'F'
              'G' 'H' 'J' 'K' 'L' 'Z' 'X' 'C' 'V' 'B'
              'N' 'M')
symbol = list('@' '#' '$' '%')

if choice == "n" "N":
     for i in (range(int(long))):
         r = (random.choice(letter))
         password.append(r)
else:
     for e in (range(int(long))):
         x = (random.choice(symbol + letter))
         password.append(x)

print(user + ':' + ' ' + ''.join(password))
