import pymysql
import csv

def read_data():
    data=[]
    k=0
    csv_file=csv.reader(open('indexdata-v2.csv','r'))
    for line in csv_file:
        if '..' in line[4]:
            b_e_37=line[4].split('..')
            b_37=int(b_e_37[0])
            e_37=int(b_e_37[1])
            b_e_39 = line[5].split('..')
            b_39 = int(b_e_39[0])
            for i in range(e_37-b_37+1):
                k+=1
                data.append((line[0], line[1], line[3], str(b_37+i), str(b_39+i), line[6]))
        else:
            data.append((line[0],line[1],line[3],line[4],line[5],line[6]))
    return data

def put_in_mydatabase(data):
    #data是一个列表，列表中的每个元素是元组
    conn = pymysql.connect(
        host="localhost",
        user="root",password="123456",
        database="chry",
        charset="utf8")

    cursor = conn.cursor()
    """
    CREATE TABLE IF NOT EXISTS `name_type_2`(
   `gene_id` INT UNSIGNED AUTO_INCREMENT,
   `gene_name` VARCHAR(200),
   `gene_type` VARCHAR(200),
   `gene_rs` VARCHAR(200),
   `gene_pos_37` VARCHAR(200),
   `gene_pos_38` VARCHAR(200),
   `gene` VARCHAR(200),
    PRIMARY KEY ( `gene_id` )
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """

    sql='insert into name_type_2(gene_name,gene_type,gene_rs,gene_pos_37,gene_pos_38,gene) values(%s,%s,%s,%s,%s,%s);'
    cursor.executemany(sql, data)
    conn.commit()
    cursor.close()
    conn.close()

def get_type_from_databse(key,target):
    result=[]
    conn = pymysql.connect(
        host="localhost",
        user="root", password="123456",
        database="chry",
        charset="utf8")
    cursor = conn.cursor()
    sql=' select * from name_type where gene_+'target'+=%s;'
    cursor.execute(sql,key)
    infos = cursor.fetchall()
    for i in infos:
        result.append(i[2])
    cursor.close()
    conn.close()
    #print(result)
    return result

def get_update():
    #这个方法还是太慢了
    data=[]
    each_time=[]
    name='('
    with open('汇总表a-j.txt','r') as f:
        lines=f.readlines()
        for line in lines:
            temp=line.strip('\n').split('\t')
            if len(temp) > 2:
                if temp[2] != '':
                    # data += 'WHEN ' + temp[0] + ' THEN ' + temp[2] + '\n'
                    # name += temp[0]+','
                    each_time+=[temp[0],temp[2]]
            if len(each_time) == 6:
                    data.append((each_time[0],each_time[1],each_time[2],each_time[3],each_time[4],each_time[5]))
                    each_time = []
    # new_data=[(data,name)]

    conn = pymysql.connect(
        host="localhost",
        user="root", password="123456",
        database="chry",
        charset="utf8")
    cursor = conn.cursor()
    sql = 'UPDATE name_type SET gene_rs = CASE gene_name WHEN %s THEN %s WHEN %s THEN %s WHEN %s THEN %s END'
    cursor.executemany(sql,data)
    conn.commit()
    cursor.close()
    conn.close()

def get_update_2():
    #通过创建临时表的方法更新数据
    data=[]
    with open('汇总表a-j.txt','r') as f:
        lines=f.readlines()
        for line in lines:
            temp=line.strip('\n').split('\t')
            if len(temp) > 2:
                if temp[2] != '':
                    # data += 'WHEN ' + temp[0] + ' THEN ' + temp[2] + '\n'
                    # name += temp[0]+','
                    data.append((temp[0],temp[2]))
    # new_data=[(data,name)]
    conn = pymysql.connect(
        host="localhost",
        user="root", password="123456",
        database="chry",
        charset="utf8")
    cursor = conn.cursor()
    # sql0='create index index_name_2 on name_type_2 (gene_name) '
    sql1='create temporary table tmp(`id` INT UNSIGNED AUTO_INCREMENT,`name` varchar(200),`rs` varchar(200),primary key(`id`),INDEX index_name_tmp (name));'
    sql2='insert into tmp(name,rs) values(%s,%s);'
    sql3='update name_type_2,tmp set name_type_2.gene_rs=tmp.rs where name_type_2.gene_name=tmp.name'
    sql4='create index index_name_tmp on temp (name)'
    # cursor.execute(sql0)
    print('create index for name_type_2 success')
    cursor.execute(sql1)
    print('create tmp success')
    cursor.executemany(sql2,data)
    print('insert data to tmp success')
    cursor.execute(sql3)
    print('update successs')
    conn.commit()
    cursor.close()
    conn.close()


if __name__=='__main__':
    # put_in_mydatabase()
    get_update_2()
