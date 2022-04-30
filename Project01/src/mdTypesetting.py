import re
file_path = 'E:\\Documents\\Github\\Markdown_Typesetting\\Project01\\file\\demo.md'
file_path2 = 'E:\\Documents\\Github\\Markdown_Typesetting\\Project01\\file\\demo01.md'
def titleRank(line):
    str1 = '#'
    counter = 0
    strTitle = str1
    while True:
        flag = line.startswith(strTitle)
        if flag == False:
            return counter
        counter+=1
        strTitle = strTitle + str1
def isTitle(lines):
    """
    Detect the position of title and record the rank and label
    :param lines:
    :return: titleIndex [[index, rank, 'label'],]
    """
    titleIndex = []
    for i in range(len(lines)):
        rank = titleRank(lines[i])
        if rank > 0:
            temp = [i, rank]
            titleIndex.append(temp)
    rank = [0]
    preRank = 0
    for i in range(len(titleIndex)):
        print(i)
        print('preRank = ', preRank)
        tempRank = titleIndex[i][1] # rank
        print('tempRank = ',tempRank)
        if preRank == tempRank:
            rank[tempRank] += 1
        elif preRank < tempRank:
            if tempRank >= len(rank):
                rank.append(0)
            rank[tempRank] += 1
            preRank = tempRank
        elif preRank > tempRank:
            for j in range(len(rank)):
                if j > tempRank:
                    rank[j] = 0
            rank[tempRank] += 1
            preRank = tempRank

        print('preRank = ', preRank)
        print(rank)
        strT = ''
        for k in range(len(rank)):
            if rank[k] == 0:
                pass
            else:
                str1 = str(rank[k])
                strT = strT + '.' +str1
        strT = 't' + strT[1:]
        print(strT)
        titleIndex[i].append(strT)

    return  titleIndex

def replaceTitle(lines, titleIndex, fontName='Times New Roman'):
    str1 = '<a name=""><font face=""></font></a>'
    for i in range(len(titleIndex)):
        str2 = lines[titleIndex[i][0]]
        title = str2[(titleIndex[i][1]+1):-1]
        title = '#'*(titleIndex[i][1]) + ' ' + str1[:9] + titleIndex[i][2] + str1[9:23] + fontName + str1[23:25] + title + str1[25:]+'\n'
        print(title)
        lines[titleIndex[i][0]] = title
    return lines

def replaceChart(lines, type='fig'):
    str3 = '<center style="color:#C0C0C0;text-decoration:underline"><font face="Cambria"><a name=""></a>: </font></center>\n'
    TYPE = '<FIG>'
    TYPENAME = 'Figure'
    if type == 'tab':
        TYPE = '<TAB>'
        TYPENAME = 'Table'
    rank = 0
    counter = 0
    for i in range(len(lines)):
        str1 = lines[i]
        if (str1[0:1] ==  '#') & (str1[1:2] == ' '):
            rank += 1
            counter = 0
        if str1[0:5] == TYPE:
            counter += 1
            chartName = str1[6:-1]
            chartFlag = str(rank) + '.' + str(counter)
            chartPin = type + chartFlag
            typeName = TYPENAME + '[' + chartFlag + ']'
            chartName = str3[:86] + chartPin + str3[86:88]+ typeName + str3[88:94] + chartName + str3[94:]
            lines[i] = chartName
    return lines

def isNormal(lines):
    """

    :param lines: list of markdown file in lines
    :return: normalIndex [index,]
    """
    normalIndex = []
    FLAG = 0     # 0 is do, -1 is continue
    mathFLAG = 0 # 0 is do, -1 is continue
    codeFLAG = 0 # 0 is do, -1 is continue
    marks = ['|', '<FIG>', '<TAB>', '#', '<img', '![image', '<center']
    for i in range(len(lines)):
        temp = 0
        if (codeFLAG == -1) | (mathFLAG == -1): temp = -1
        # jump empty
        if lines[i] == '\n':
            FLAG = -1
        # jump math
        if (lines[i][0:2] == '$$') & (mathFLAG == 0) :
            mathFLAG = -1
            continue

        if (lines[i][0:2] == '$$') & (mathFLAG == -1) :
            mathFLAG = 0
            continue
        # jump code
        if (lines[i][0:3] == '```') & (codeFLAG == 0):
            codeFLAG = -1
            continue
        if (lines[i][0:3] == '```') & (codeFLAG == -1):
            codeFLAG = 0
            continue

        for j in range(len(marks)):
            markLen = len(marks[j])
            if lines[i][:markLen] == marks[j]:
                FLAG = -1

        if (FLAG == 0) & (codeFLAG == 0) & (mathFLAG == 0) & (temp == 0):
            normalIndex.append(i)
            print(lines[i])
        FLAG = 0
    return normalIndex

def replaceNormal(lines, normalIndex, fontName='Cambria'):
    str1 = '<font face=""></font>\n'
    for i in range(len(normalIndex)):
        lines[normalIndex[i]] = str1[:12] + fontName + str1[12:14] + lines[normalIndex[i]][:-1] + str1[14:]

def test01():
    # codeFLAG = 0
    # mathFLAG = 0
    # print((codeFLAG == -1) | (mathFLAG == -1))
    str1 = '$$\n'
    print(str1[0:2])
def test02():
    lines = []
    with open(file_path, 'r',encoding='utf-8') as f:
        lines = f.readlines()
        normalIndex = isNormal(lines)
        replaceNormal(lines,normalIndex)
        # print(lines)
    with open(file_path2, 'w',encoding='utf-8') as f:
         f.writelines(lines)
if __name__ == '__main__':
    test01()

