from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

myUrl = 'https://www.newegg.com/global/in/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+cards&N=-1&isNodeId=1'

uClient = uReq(myUrl)

pageHtml = uClient.read()

uClient.close()

#Html Parsing 
pageSoup = soup(pageHtml, "html.parser")

containersNewEgg = pageSoup.findAll("div", {"class" : "item-container"})

container = containersNewEgg[0]

fileName = "products.csv"
f = open(fileName, "w")
headers = "Brand, Product Name, Product Price \n"
f.write(headers)
for container in containersNewEgg:

        brandName = container.div.div.a.img["title"]

        titleContainer = container.findAll("a", {"class" : "item-title"})

        productName = titleContainer[0].text

        productPricingContainer = container.findAll("li", {"class" : "price-current"})

        productPricing = productPricingContainer[0].text.replace("," , "")
    
        print("Brand name: " + brandName)

        print("Product name: " + productName)

        print("Product Price:" + productPricing)



        f.write(brandName + "," + productName.replace(",", "||") + "," + productPricing.replace("\u20b9", "Rs") + "\n")

f.close()


