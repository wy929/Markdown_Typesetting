import mdTypesetting as md
import os.path as path

# change the file_name and file_path
file_name = 'report.md'
file_path = 'E:\Documents\Github\DDL\CAN202\Report'


def case1(file_path_org, file_path_new, titleFont='Times New Roman', bodyFont='Cambria'):
    """
    Reformatting the source file includes: replacing the body font, changing the title, and adding captions to charts
    :param file_path_org: input path
    :param file_path_new: output path
    :param titleFont:
    :param bodyFont:
    :return:
    """
    with open(file_path_org, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        titleIndex = md.isTitle(lines)
        md.replaceChart(lines)
        md.replaceChart(lines, type='tab')
        md.replaceTitle(lines, titleIndex, titleFont)
        bodyIndex = md.isBody(lines)
        md.replaceBody(lines, bodyIndex, bodyFont)
    with open(file_path_new, 'w', encoding='utf-8') as f:
         f.writelines(lines)

if __name__ == '__main__':
    file_path_org = path.join(file_path, file_name)
    file_name_new = file_name[:-3] + '_new' + '.md'
    fiel_path_new = path.join(file_path,file_name_new)
    case1(file_path_org, fiel_path_new)
    print('Success!')