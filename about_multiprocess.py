from multiprocessing import Pool

def to_bam():
	#to_bam.sh是一个shell脚本
	subprocess.run('to_bam.sh '+name, shell=True)
	
if __name__=='__main__':
	#n是进程数
	pool=Pool(int(n))
	#name是一个list
	pool.map(to_bam,names)
	pool.close()
	pool.join()
