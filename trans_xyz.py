# -*- coding:utf-8 -*-
"""
Author : Ronghong Ji
Time   : 2022/10/17
E-mail : jironghong1998@gmail.com
Desc.  :
"""


import pandas as pd

def read_Au_x(filename):
    ''' Change the x-coordinate to the new location

    Args:
        content: read the contents of the file
        contact: split specific content by row
        atom: the row of data for each atom
        x: the x-coordinate of atom
        pos_x: the list of x-coordinate
        pos_num_x(first): str is converted to float
        l_x: the length of the x-direction box
        pos_num_x(second): the new x-coordinate after the translation transformation
    
    Return:
        pos_num_x(second): the new x-coordinate after the translation transformation
    '''
    pos_x = []

    with open(filename, 'r') as f:
        content = f.read()
        contact = content.split('\n')[2:]
        for line in contact:
            if line == '' or line.isdigit():
                continue
            else:
                atom = line.split()
                x = atom[1]
                pos_x.append(x)

        pos_num_x = [float(x) for x in pos_x]
        l_x = max(pos_num_x) - min(pos_num_x)
        pos_num_x = list(map(lambda x:float(x)-(0.5*l_x+min(pos_num_x)),pos_num_x))

    return pos_num_x


def read_Au_y(filename):

    pos_y = []
    with open(filename, 'r') as f:
        content = f.read()
        contact = content.split('\n')[2:]
        for line in contact:
            if line == '' or line.isdigit():
                continue
            else:
                atom = line.split()
                y = atom[2]
                pos_y.append(y)

        pos_num_y = [float(y) for y in pos_y]
        l_y = max(pos_num_y) - min(pos_num_y)
        pos_num_y = list(map(lambda y:float(y)-(0.5*l_y+min(pos_num_y)),pos_num_y))

    return pos_num_y


def read_Au_z(filename):

    pos_z = []
    with open(filename, 'r') as f:
        content = f.read()
        contact = content.split('\n')[2:]
        for line in contact:
            if line == '' or line.isdigit():
                continue
            else:
                atom = line.split()
                z = atom[3]
                pos_z.append(float(z))

        pos_num_z = pos_z
        l_z = max(pos_num_z) - min(pos_num_z)
        pos_num_z = [float(z)-(0.5*l_z+min(pos_num_z)) for z in pos_num_z]

    return pos_num_z


def read_Au_type(filename):

    type = []
    with open(filename, 'r') as f:
        content = f.read()
        contact = content.split('\n')[2:]
        for line in contact:
            if line == '' or line.isdigit():
                continue
            else:
                atom = line.split()
                t = atom[0]
                type.append(t)

    return type



if __name__ == '__main__':
    file = 'ILs_H2O_salt.xyz'
    newfile = 'new3.xyz'
    atom = read_Au_type(file)
    x = read_Au_x(file)
    y = read_Au_y(file)
    z = read_Au_z(file)
    df_atom = pd.Series(atom)
    df_x = pd.Series(x)
    df_y = pd.Series(y)
    df_z = pd.Series(z)
    df = pd.concat([df_atom, df_x, df_y, df_z], axis=1)
    df = round(df,6)
    df.to_csv(newfile, index=False, header=None, sep=' ')