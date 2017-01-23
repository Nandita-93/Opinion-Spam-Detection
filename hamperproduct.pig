reviews = load 'ProjectText' as (productid, userid, profilename, helpfulness, score, time, summary, review);
grpd = group reviews by productid;
perproductp = foreach grpd generate group, AVG(reviews.score) as avgscore;
joinp = JOIN reviews BY productid, perproductp BY group;
hamFiltered = FILTER joinp BY (score <= avgscore + 1) AND (score >= avgscore - 1);
hamavgnew= FOREACH hamFiltered GENERATE review;
store hamavgnew into 'hamavgnew.txt';