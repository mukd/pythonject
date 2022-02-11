from win32com.client import Dispatch
from os import walk
class Docxpdf:
    def __init__(self):
        self.wdFormatPDF=17
    def docx_pdf(self,input_file):
        self.word = Dispatch('Word.Application')
        doc = self.word.Documents.Open(input_file)
        doc.SaveAs(input_file.replace(".docx", ".pdf").replace('.doc', '.pdf'), FileFormat=self.wdFormatPDF)
        doc.Close()
        self.word.Quit()

def main(docxfile):
    doc_files = []
    count = 0
    directory = docxfile
    #directory = "C:\\Users\\mukd\\Desktop\\word"
    for root, dirs, filenames in walk(directory):
        for file in filenames:
            if file.endswith(".doc") or file.endswith(".docx"):
                count += 1
                df = Docxpdf()
                df.docx_pdf(str(root + "\\" + file))
                print('word转PDF中:%d' % (count))
        print('一共转换了%d个word文件' % (count))

