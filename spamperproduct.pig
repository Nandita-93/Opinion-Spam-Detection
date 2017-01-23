reviews = load 'ProjectText' as (productid, userid, profilename, helpfulness, score, time, summary, review);
grpd = group reviews by productid;
perproductp = foreach grpd generate group, AVG(reviews.score) as avgscore;
joinp = JOIN reviews BY productid, perproductp BY group;
Filtered = FILTER joinp BY (score > avgscore + 1) OR (score < avgscore - 1);
Avgesupsect = FOREACH Filtered GENERATE review;
store Avgesupsect into 'avgesupsect.txt';