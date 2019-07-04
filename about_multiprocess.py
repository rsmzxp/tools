from multiprocessing import Pool
from functools import partial

def to_bam(name,my_dir):
	subprocess.run('to_bam.sh '+name+' '+my_dir, shell=True)
	
if __name__=='__main__':
	#n是进程数
	pool=Pool(int(n))
	#names是一个list,my_dir是一个相对固定参数
	pool.map(partial(to_bam,my_dir=my_dir),names)
	pool.close()
	pool.join()
	
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

from multiprocessing import Pool
from functools import partial


def multi_wrapper(args):
   return my_func(*args)

def my_func(x,y):
    # to_bam.sh是一个shell脚本
    print(x*y)


if __name__ == '__main__':
    # n是进程数
    pool = Pool(5)
    # names是一个list,my_dir是一个相对固定参数
    a = [x for x in range(100)]
    b = [x for x in range(100,0,-1)]
    a_b=zip(a,b)
    pool.map(multi_wrapper,list(a_b))
    pool.close()

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def my_func(x,y):
    print(x*y)


if __name__ == '__main__':
    # n是进程数
    pool = Pool(5)
    # names是一个list,my_dir是一个相对固定参数
    a = [x for x in range(100)]
    b = [x for x in range(100,0,-1)]
    # z = 10
    a_b=zip(a,b)
    pool.starmap(my_func,list(a_b))
    pool.close()
    pool.join()
