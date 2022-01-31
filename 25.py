import random
email = []
num = int(input("How many emails do you want to generate? "))
for i in range(1,num+1):
    value = str(input("Enter email_id = "))
    email.append(value+'\n')
print("Email_id :",email)
fp = open("email.txt","w")
fp.writelines(email)
fp.close()