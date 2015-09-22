#! /usr/bin/env python
# coding: utf-8

import xlwt
book = xlwt.Workbook(encoding = 'utf-8',style_compression = 0)
sheet = book.add_sheet('sheet1',cell_overwrite_ok = True)

tree=[{"text":"病史记录","id":"001","children":[{"text":"个人史","id":"005","children":[{"text":"肺活量","id":"007","children":[]},{"text":"体重","id":"008","children":[]}]},{"text":"既往史","id":"006","children":[]}]}]

tree[0]['text']
tree[0]['children'][0]['text']
tree[0]['children'][1]['text']
tree[0]['children'][0]['children'][0]['text']
print '-------------------------------'
len1 = len(tree)
ha,le = 0,0
for i in range(len1):
    a = 0
    len2 = len(tree[i]['children'])
    if len2 ==0:
        a = 1
        #continue若没有项则不会生成记录(可能2或3没项)
        #continue
        print '-------------------------------'
        print "================"
    for j in range(len2):
        b = 0
        len3 = len(tree[i]['children'][j]['children'])
        if len3 == 0:
            b = 1
            #continue
        if a == 0 and b ==0:
            for m in range(len3):
                sheet.write(ha,le,tree[i]['text'])
                sheet.write(ha,le+1,tree[i]['children'][j]['text'])
                sheet.write(ha,le+2,tree[i]['children'][j]['children'][m]['text'])
                ha+=1
        elif a == 1:
            sheet.write(ha,le,tree[i]['text'])
            sheet.write(ha,le+1,tree[i]['text'])
            sheet.write(ha,le+2,tree[i]['text'])
            ha+=1
        elif b == 1:
            sheet.write(ha,le,tree[i]['text'])
            sheet.write(ha,le+1,tree[i]['children'][j]['text'])
            sheet.write(ha,le+2,tree[i]['children'][j]['text'])
            ha+=1
        else:
            print 'wrong'
            ha+=1
                            

                
             
                
book.save('d:/jilu.xls')
        

