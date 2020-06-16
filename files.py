# python 3ado l imkaniya bach isyab file o im7ih o izid

# kifach n9dr nsyab file
myfile = open('myfile.txt','w')

# kifach na5od des informations 3la l file 
print('Name : ',myfile.name)
print('Is Closed : ',myfile.closed)
print('Opening Mode : ',myfile.mode)

# kifach nktbo fih 
myfile.write('hello i am zakaria')
myfile.write('i am a developer')

# ILA BGHINA NZIDO 3LIH
myfile = open('myfile.txt','a')
myfile.write(' and i am desinger')
myfile.close()

# ila bghina n9raw mn file
myfile = open('myfile.txt','r+')
text = myfile.read(100)
print(text)