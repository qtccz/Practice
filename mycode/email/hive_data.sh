#!/usr/bin/env bash
source ~/.bash_profile

start_time=$(date "+%Y-%m-%d %H:%M:%S")
echo "开始统计时间：$start_time"
# Hive读取数据
time=$(date "+%Y-%m-%d" -d "-1day")
beeline -u 'jdbc:hive2://10.1.5.15:10000/default' --verbose=true --outputformat=csv2 -e "SELECT search_source,count(search_source) AS count_num from sk_spider.spider_news where crawler_time LIKE '%$time%' GROUP BY search_source" > /home/dongzhaorui/send_email/data.csv

# Python 发送邮件
nohup python /home/dongzhaorui/send_email/post_email_new.py > /home/dongzhaorui/logs/post_email.log 2>&1 & 

end_time=$(date "+%Y-%m-%d %H:%M:%S")
echo "结束统计时间：$end_time"
