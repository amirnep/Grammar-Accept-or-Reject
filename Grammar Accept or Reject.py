from nltk import CFG
import nltk

n = int(input("How many Production Rules Do You Want to add: "))

string_list = []
null_dict = {}

for i in range(n):
    string_list.append("\n")

    print("\nWe are adding Production Rules by input. For lambda enter:'null' and for or enter: | ")
    
    start = input("\nEnter start Variable(Example:S) with capital: ")
    string_list.append(start)

    string_list.append(" -> ")

    end = input("Enter production rule(Example:'a' S 'a' | 'b' S 'b' | 'null'): ")

    if start == 'S' and 'null' in end:
        null_dict['n'] = 'null'
        
    string_list.append(end)
    string_list.append(" ")

string = ""
string = string.join(string_list)

grammar = CFG.fromstring(string)

parser = nltk.RecursiveDescentParser(grammar)

print("\nProgram started. For Finished Enter 0 as string.")
while(True):
    print("\nEnter a string by space after every terminal(For lambda don't Enter any string.): ")
    string = [x for x in input().split()]
    
    flag = False

    if null_dict['n'] == 'null' and len(string) == 0:
        print("Accepted.")
        flag = True
    try:
        if string[0] == '0':
            print("The program is end press Enter to exit.")
            break

    except IndexError:
        pass
    
    length = len(string)
    length1 = length + 1
    str1 = [''] * length1
    m = 0

    for i in range(1,length+1):
        for j in range(i):
            str1[j] = string[j]
        
        str1[i] = 'null'

        for k in range(m,length-1):
            str1[k+2] = string[k+1]

        try:
            l1 = parser.parse_all(str1)
            if l1[0][0] == string[0]:
                print("\nAccepted.")
                flag = True
                
        except IndexError:
            pass
        
        except ValueError:
            print("\nRejected.")
            flag = True
            break
        
        str1.clear()
        str1 = [''] * length1
        m += 1

    if flag is False:
        print("\nRejected.")

quit = input()
