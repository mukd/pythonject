
def pysim_bar():
    import PySimpleGUI as sg
    import time
    count = range(100)
    for i,item in enumerate(count):
        sg.one_line_progress_meter('实时进度',i + 1,len(count),'-key-')
        time.sleep(0.05)


if __name__ == '__main__':
    pysim_bar()







