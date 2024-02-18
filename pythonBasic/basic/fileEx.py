# fh = open('kucing.txt','w')

# for i in range(1,11):
#     fh.write(f'{i} \n')

# fh.close()

# with open('kucing.txt','a') as fh:
#     for i in range(11,21):
#         fh.write(f'{i} \n')
        
with open('kucing.txt') as fh:
    content = fh.read()

print(content)