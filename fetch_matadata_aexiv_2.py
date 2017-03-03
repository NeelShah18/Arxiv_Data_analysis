'''
Neel Shah: neelknightme@gmail.com
'''

import os
import urllib
import re

start_num=0
end_num=10
loop_count = 0
file_count = 0
#file = open(r'/home/test_data.xml','w+')
#file.write('***** Start Here *****')
#file.close()

while loop_count<=2600:
    try:
        url = 'http://export.arxiv.org/api/query?search_query=cat:cs.CV%20OR%20cat:cs.AI%20OR%20cat:cs.LG%20OR%20cat:cs.CL%20OR%20cat:cs.NE%20OR%20cat:stat.ML&id_list=&start='+str(start_num)+'&max_results='+str(end_num)
        data = urllib.urlopen(url).read()
        file = open('/home/arvix_data.xml','a')
        file.write(data)
        file_count += 10
        print 'Total paper data appended is :'+str(file_count)
        start_num=end_num+1
        end_num=end_num+10
        file.close()
    except:
        print "Error :"
        file.close()
