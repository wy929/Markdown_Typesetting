import mdTypesetting as md
import os.path as path

# change the file_name and file_path
file_name = 'report.md'
file_path = 'E:\\Documents\\Github\\Markdown_Typesetting\\Project01\\file\\'


def tp1(file_path_org, file_path_new):
    lines = []
    with open(file_path_org, 'r',encoding='utf-8') as f:
        lines = f.readlines()
        titleIndex = md.isTitle(lines)
        print(titleIndex)
        md.replaceChart(lines)
        md.replaceChart(lines, type='tab')
        md.replaceTitle(lines, titleIndex)
        normalIndex = md.isNormal(lines)
        md.replaceNormal(lines,normalIndex)
    with open(file_path_new, 'w',encoding='utf-8') as f:
         f.writelines(lines)

if __name__ == '__main__':
    print(file_name[:-3])
    file_path_org = path.join(file_path, file_name)
    file_name_new = file_name[:-3] + '_new' + '.md'
    fiel_path_new = path.join(file_path,file_name_new)
    tp1(file_path_org, fiel_path_new)