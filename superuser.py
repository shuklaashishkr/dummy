import os

def superuser():
    # print(os.system("net localgroup administrators"))
    l = os.system("net localgroup administrators > super_user.txt")
    #m = os.system("net accounts > net_accounts.txt")

    dir_path = os.path.dirname(os.path.realpath(__file__))
    #print(dir_path)
    # ln = sum(1 for line in open('super_user.txt'))
    # print(ln)
    with open('super_user.txt') as f:
        content = f.readlines()

    #with open('net_accounts.txt') as f1:
    #    content1 = f1.read()

    #with open('net_accounts.txt') as f2:
    #    content2 = f2.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    #content2 = [x.strip() for x in content2]
    #h = int(content2[2].split(" ")[-1])
    #j = int(content2[3].split(" ")[-1])
    #print(content)
    ln = len(content)
    super_u = content[6:ln - 2]
    #print(super_u)
    #print(content1)
    success = 0
    return super_u