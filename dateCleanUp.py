f = open('C:/Users/Nandita/Desktop/finefoods/files/foods.txt','r',encoding="utf8")
filedata = f.read()
f.close()
#tab space is used as the column separator 
new = filedata.replace("product/productId:","")
new = new.replace("review/userId:","	")
new = new.replace("review/profileName:","	")
new = new.replace("review/helpfulness:","	")
new = new.replace("review/score:","	")
new = new.replace("review/time:","		")
new = new.replace("review/summary:","	")
new = new.replace("review/text:","	")
#using any delimiter that is not present in the file
new = new.replace("\n\n","@#$%")
new = new.replace("\n","	")
# ‘\n’ is used as  the record delimiter
new = new.replace("!@#$%","\n")
#writing the modified data back to the file
f = open('C:/Users/Nandita/Desktop/finefoods/foodsColBased.txt','w')
#first row is the column header
f.write(" product/productId review/userId   review/profileName  review/helpfulness  review/score    review/time review/summary  review/text\n")
f.write(new)
f.close()
