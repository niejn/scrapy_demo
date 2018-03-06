import re


def check(str):
    # my_re = re.compile(r'[A-Za-z]', re.S)
    # res = re.findall(my_re, str)
    pattern = re.compile(r'[A-Za-z]', re.S)
    res = pattern.match(str)
    if res:
        return True
    else:
        return False
def main():
    file = './instruments.txt'
    with open(file, 'r') as srcFile:

        text = srcFile.readlines()
        print(text)
        with open("./douban.txt", "w") as f:
            f.write("这是个测试！")
            for row in text:
                if "#"in row:
                    f.write(row)
                    print(row.strip())
                # if row.strip().isalpha():
                #     print(row.strip())
                if check(row):
                    f.write(row)
                    print(row.strip())

    return
if __name__ == '__main__':
    main()