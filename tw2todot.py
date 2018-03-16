#!/usr/bin/python

# by mauvedeity and leren1098

from __future__ import print_function

import sys

ignore_passages = ['::StoryTitle', '::StoryIFID[twee2]','::StoryCSS [stylesheet]', '::StoryIncludes', '::Twee2Settings [twee2]]']

def usage():
    print('usage: tw2dot.py <filename.tw2>')

def header():
    print('digraph G {')
    print('  rankdir=LR;')

def footer():
    print('}')

def stripspaces(pstrsrc):
    result = pstrsrc.replace(' ','')
    result = result.split('<')[0]
    if(result[0].isdigit()):
        result = 'n'+result
    return(result)

def process(fname):
    with open(fname, 'rt') as f:
        lines = f.read().splitlines()
        nodename = '**none**'
        for l in lines:
            if((l[0:2] == '::') & (l not in ignore_passages)):  # it's a new passage
                nodename = l[2:]
            else:
                if('[[' in l):
                    l2 = l.split('[[')
                    for link in l2:
                        if(']]') in link:
                            thislink =(link.split('->')[1])[:-2]    # check full range of delimiters here
                            thislink = thislink.split(']')[0]
                            print('  ',stripspaces(nodename),'->',stripspaces(thislink),';')



if __name__ == "__main__":
    if(len(sys.argv) == 2):
        header()
        process(sys.argv[1])
        footer()
    else:
        usage()