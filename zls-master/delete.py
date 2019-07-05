import glob
import os
def __for_bib():
    '''
    for transactions on signal, audio.
    '''

    src_filename = 'refer.bib'
    dst_filename = 'refer_output.bib'

    fp = open(dst_filename,'w')
    for line in open(src_filename, encoding='gb18030', errors='ignore'):
        #print (line)
        linex = line.lstrip()
        if 'month' in linex:
            linex = linex.replace('{','').replace(' ','')
            if linex.count('}')>=2:
                linex = linex.replace('}}','}')
            if ',' in linex:
                linex = linex[:linex.index('=')+4]+linex[linex.index(','):]
            else:
                pass
        if 'url' in linex.lower():
            do_temp = ['acm','aes','doi','science','arxiv','abstract','hal','index']
            for ele in do_temp:
                if ele in linex:
                    linex = ''
                    break
        if 'pages' in linex:
            linex = linex.replace(' - ','-')

        fp.write(linex)

    fp.close()

def cleanTex(name):
    for ele_file in glob.glob('.\%s.*'%name):
        if not 'tex' in ele_file and not 'pdf' in ele_file:
            os.remove(ele_file)

    if os.path.exists(name+'.synctex.gz'):
        os.remove(name+'.synctex.gz')
    if os.path.exists('xresult.txt'):
        os.remove('xresult.txt')

__for_bib()
cleanTex( name = 'conference' )

