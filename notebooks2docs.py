import os
import shutil
import glob
import datetime
import sys

if os.path.isdir('docs'):
    shutil.rmtree('docs')
os.mkdir('docs')

shutil.copytree(os.path.join('static','js'),os.path.join('docs','js'))
shutil.copytree(os.path.join('static','css'),os.path.join('docs','css'))
shutil.copytree(os.path.join('notebooks','img'),os.path.join('docs','img'))
    
for item in glob.glob(os.path.join('notebooks','*')):
    if os.path.isdir(item):
        directory = os.path.basename(item)
        for notebook in glob.glob(os.path.join(item,'*.ipynb')):
            output_dir = os.path.join('docs',directory)
            os.system('jupyter nbconvert --to markdown {notebook} --output-dir {output_dir} --NbConvertApp.output_files_dir="img";'.format(notebook=notebook,output_dir=output_dir))

shutil.copy(os.path.join('notebooks','index.md'),'docs')
now = datetime.datetime.now().strftime('%B %d %Y %H:%M PST')
with open(os.path.join('docs','index.md'),'a') as f:
    f.write('\n```\n{}\n```'.format(now))

os.system('mkdocs build')