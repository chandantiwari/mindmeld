import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex -shell-escape ast_mbti.tex")
    os.system("evince ast_mbti.pdf")
    exit()
       
if len(sys.argv) == 1 or sys.argv[1] == 'dep':
    os.system("scp -r *.py burak@host2:/home/burak/Downloads/mindmeld/")
    exit()
