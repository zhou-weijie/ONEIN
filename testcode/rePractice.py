import re


def main():
    content = 'Hello, I am Jerry, from Chongqing, a montain city, nice to meet you……'
    regex = re.compile('\w*o\w*')
    x = regex.findall(content)
    print(x)


def second():
    pattern = re.compile(r'[a-zA-Z]')
    result = pattern.findall('as3SiOP')
    print(result)


if __name__ == '__main__':
    second()
    main()
