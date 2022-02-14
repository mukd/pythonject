"""
功能:Python实现实时显示进度条的六种方法
环境:Anaconda3.5.1,PyCharm2021,Windows10
"""
import sys
import time

#普通进度条
def pt():
    for i in range(1,101):
        print('\r',end='')
        print('进度:{}%:'.format(i),"▓" * (i // 2 ),end='')
        sys.stdout.flush()
        time.sleep(0.05)

#带时间的普通进度条
def time_pt():
    t = 60
    strt = time.perf_counter()
    for i in range(t+1):
        finsh = "▓" * i
        need_do = "-" * (t - i)
        progress = (i / t) * 100
        dur = time.perf_counter()
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finsh, need_do, dur), end="")
        time.sleep(0.05)

#tqdm库
def tqdm_bar():
    from tqdm import tqdm
    for i in tqdm(range(1,102)):
        time.sleep(0.05)

#alive_progress库
def live_progress_bar():
    from alive_progress import alive_bar
    # 假设需要执行100个任务
    with alive_bar(len(range(100))) as bar:
        for item in range(100):  # 遍历任务
            bar()  # 显示进度
            """
            代码
            """
            # 假设这代码部分需要0.05s
            time.sleep(0.05)

#PySimpleGUI库
def pysim_bar():
    import PySimpleGUI as sg
    count = range(100)
    for i,item in enumerate(count):
        sg.one_line_progress_meter('实时进度',i + 1,len(count),'-key-')
        time.sleep(0.05)

#progressbar库
def prg_bar():
    import progressbar
    p = progressbar.ProgressBar()
    for i in p(range(100)):
        time.sleep(0.05)
if __name__ == '__main__':
    prg_bar()
