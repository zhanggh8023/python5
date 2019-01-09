import cx_Oracle

# 注：设置环境编码方式，可解决读取数据库乱码问题
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'



#机构信息表
YJPT_JGXXB_sql = "INSERT INTO YJPT_JGXXB(YXJGDM,NBJGH,JRXKZH,YXJGMC,JGLB,YZBM,WDH,YYZT,CLSJ,JGGZKSSJ,JGGZZZSJ,JGDZ,FZRXM,FZRZW,FZRLXDH,CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16)"
YJPT_JGXXB = [(313340000010, 9010, 'B0151B233090001', '杭州银行股份有限公司舟山分行', '基础网店', 316000, 9010, '营业', 20010701,'083000', '173000', '舟山市定海区临城街道定沈路619号舟山港航国际大厦B座', '张晓燕', '行长', '0580-3807915', '20171027'),
              (313340000010, 9011, 'B0151B233090001', '杭州银行股份有限公司杭州分行', '基础网点', 316001, 9010, '营业', 20010702,'083000', '173000', '舟山市定海区临城街道定沈路620号舟山港航国际大厦A座', '袁华', '科长', '0580-3807916', '20171027'),
              (313340000010, 9012, 'B0151B233090001', '杭州银行股份有限公司上海分行', '基础网点', 316002, 9010, '营业', 20010703, '083000', '173000', '舟山市定海区临城街道定沈路621号舟山港航国际大厦C座', '秋雅', '副科长', '0580-3807917', '20171027'),
              (313340000010, 9013, 'B0151B233090001', '杭州银行股份有限公司北京分行', '基础网点', 316003, 9010, '营业', 20010704,'083000', '173000', '舟山市定海区临城街道定沈路622号舟山港航国际大厦F座', '夏洛', '科长', '0580-3807918', '20171027'),
              (313340000010, 9014, 'B0151B233090001', '杭州银行股份有限公司舟山分行', '基础网点', 316004, 9010, '营业', 20010705,'083000', '173000', '舟山市定海区临城街道定沈路623号舟山港航国际大厦G座', '冬梅', '主任', '0580-3807919', '20171027'),
              (313340000011, 660000, 'B0151B233090001', '杭州银行股份有限公司金融事业部', '一级分行(虚拟)', 316005, 9010, '营业',20010705, '083000', '173000', '杭州市庆春路46号', '无	', '无', '无', '20171027')]


# 员工表
YJPT_YGB_sql = "INSERT INTO YJPT_YGB(GH,YXJGDM,NBJGH,JRXKZH,YXJGMC,XM,SFZH,LXDH,WDH,SSBM,ZW,YGZT,GWBH,CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14)"
YJPT_YGB = [('001', 313340000010, 9010, 'B0151B233090001', '杭州银行股份有限公司舟山分行', '张晓燕', 110101199003078000, 15824196565,9010, '营业部', '员工', '在职', '000001','20171028'),
            ('002', 313340000010, 9011, 'B0151B233090001', '杭州银行股份有限公司杭州分行', '袁华', 110101199003078000, 15824196566,9010, '营业部', '员工', '在职', '000002','20171028'),
            ('003', 313340000010, 9012, 'B0151B233090001', '杭州银行股份有限公司上海分行', '秋雅	', 110101199003078000,15824196567, 9010, '营业部', '员工', '在职', '000003','20171028'),
            ('004', 313340000010, 9013, 'B0151B233090001', '杭州银行股份有限公司北京分行', '夏洛', 110101199003078000, 15824196568,9010, '营业部', '员工', '在职', '000004','20171028'),
            ('005', 313340000010, 9014, 'B0151B233090001', '杭州银行股份有限公司舟山分行', '冬梅', 110101199003078000, 15824196569,9010, '营业部', '员工', '在职', '000005','20171028'),
            ('006', 313340000011, 660000, 'B0151B233090001', '杭州银行股份有限公司金融事业部', '无', '无', '无', 9010, '营业部', '无', '无', '无','20171028')]


#柜员表
YJPT_GYB_sql = "INSERT INTO YJPT_GYB(GYH,GH,YXJGDM,NBJGH,ZXJGDM,JRXKZH,YXJGMC,GYLX,SFSTGY,KHJLBZ,JBZWBZ,QXGLBZ,YBGLBZ,XDYBZ,KGYBZ,ZHGYBZ,SQBZ,SQFW,GWBH,GYYHJB,GYQXJB,SGRQ,GWZT,CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24)"
YJPT_GYB = [('1', '001', 313340000010, 9010,'', 'B0151B233090001', '杭州银行股份有限公司舟山分行', '综合柜员', '是', '是', '是','是', '是', '是', '是', '是', '是','', '000001','1', '1', '20171102', '在岗', '20180213'),
            ('2', '002', 313340000010, 9011,'', 'B0151B233090001', '杭州银行股份有限公司杭州分行', '普通柜员', '是', '是', '否','否', '否', '否', '否', '否', '是','', '000002', '4', '4', '20171103', '在岗', '20180214'),
            ('3', '003', 313340000010, 9012,'', 'B0151B233090001', '杭州银行股份有限公司上海分行', '现金柜员', '是', '是', '否','否', '是', '否', '否', '是', '是','', '000003', '2', '2', '20171104', '在岗', '20180215'),
            ('4', '004', 313340000010, 9013,'', 'B0151B233090001', '杭州银行股份有限公司北京分行', '低柜柜员', '是', '是', '否','否', '否', '否', '否', '否', '是', '','000004', '3', '3', '20171105', '在岗', '20180216'),
            ('5', '005', 313340000010, 9014,'', 'B0151B233090001', '杭州银行股份有限公司舟山分行', '大堂经理', '是', '是','是', '是', '是', '否', '否', '是', '是', '','000005', '1', '1', '20171106', '在岗', '20180217'),
            ('6', '006',31334000001, 660000,'', 'B0151B233090001', '杭州银行股份有限公司金融事业部','无', '否', '否', '否', '否', '否', '否', '否', '否', '否', '','无', '1', '1', '', '', '20180218')]


#岗位信息表
YJPT_GWXXB_sql= "INSERT INTO YJPT_GWXXB(GWBH,YXJGDM,NBJGH,JRXKZH,GWZL	,GWMC,GWSM,GWZT,CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9)"
YJPT_GWXXB=[('000001', 313340000010, 9010, 'B0151B233090001', '行政', '管理人员', '无', '满员', '20171105'),
            ('000002', 313340000010, 9011,	'B0151B233090001',	'财务',	'柜员', '无',	'满员', '20171105'),
            ('000003', 313340000010, 9012,	'B0151B233090001',	'信贷', '客户经理', '无', '满员', '20171105'),
            ('000004', 313340000010, 9013,	'B0151B233090001',	'运营',	'柜员', '无',	'满员', '20171105'),
            ('000005', 313340000010, 9014,	'B0151B233090001',	'行政',	'管理人员', '无',	'满员', '20171105'),
            ('000006', '', 660000, 'B0151B233090001', '', '', '无', '缺编', '20171105')]


#机构关系表
YJPT_JGGXB_sql="INSERT INTO YJPT_JGGXB(YHJGDM,NBJGH,JRXKZH,YHJGMC	,YZBM,SJGLJGDM,SJGLJGMC,CJRQ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8)"
YJPT_JGGXB = [(313340000010, 9010, 'B0151B233090001', '杭州银行股份有限公司舟山分行', 316000, '', '', 20171027),
              (313340000010, 9011, 'B0151B233090001', '杭州银行股份有限公司杭州分行', 316001, '', '', 20171027),
              (313340000010, 9012, 'B0151B233090001', '杭州银行股份有限公司上海分行', 316002, '', '', 20171027),
              (313340000010, 9013, 'B0151B233090001', '杭州银行股份有限公司北京分行', 316003, '', '', 20171027),
              (313340000010, 9014, 'B0151B233090001', '杭州银行股份有限公司舟山分行	', 316004, '', '', 20171027),
              (313340000011, 660000, 'B0151B233090001', '杭州银行股份有限公司金融事业部', 316005, '', '', 20171027)]




# scott是数据用户名，tiger是登录密码（默认用户名和密码）
connection = cx_Oracle.connect("hg", "123456", '122.112.248.182:1521/CITYDO')
# 操作游标
cursor = connection.cursor()
for i in range(len(YJPT_JGGXB)):
    sql=YJPT_JGGXB_sql
    cursor.prepare(sql)
    cursor.execute(None,YJPT_JGGXB[i])
    # 切记一定要执行
    cursor.execute('commit')

# 关闭连接，释放资源
cursor.close()
connection.close()





