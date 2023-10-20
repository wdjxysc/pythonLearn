#coding=utf8

from multiprocessing import Process #跨平台多进程模块
from multiprocessing import Pool #线程池模块
import os, time, random
import subprocess #子线程模块


# 子进程要执行的代码
def run_proc(name):
    print('Run child progress %s (%s)...' % (name, os.getpid()))

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p=Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close() #调用join之前必须调用close 调用close后就不能添加进程了
    p.join() #调用完毕等待
    print('All subprocesses done.')

    #subprocess
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)

    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('gbk'))
    print('Exit code:', p.returncode)
