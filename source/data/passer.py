import optparse
import os




def main():
    parser=optparse.OptionParser('usage %prog'+\
                                 '-f <zipfile> -d <dictionary>')
    parser.add_option('-f',dest='zname',type='string',\
                      help='specify zip file')
    parser.add_option('-d',dest='dname',type='string',\
                      help='specify dictionary file')
    (options,arg)=parser.parse_args()
    print options.zname
    f=open('data.py','r')
    data=f.read()
    f.close()
    f=open('seq_data.py','w')
    f.write("ip='"+options.zname+"'")
    f.write('\n')
    f.write(data)
    f.close()

    """uncomment while building
    os.system('make.exe attack.py')"""

    os.system('makeExploit.py')
    return None
    
    
    

main()
