from bs4 import BeautifulSoup
import cloudscraper 

def Data_Scraping(Targeted_Website):
    scraper = cloudscraper.create_scraper() 
    info = scraper.get(Targeted_Website) 
    soup = BeautifulSoup(info.text, 'html.parser')
    products = soup.find_all('div',class_="uk-panel uk-position-relative")
    product_List = []
    for product in products : 
        product_name = product.find('a',class_="product-item-link").text
        product__price = product.find('span',class_="uk-price").text.replace("\xa0", " ")
        product_brand = product.find('div', class_="uk-width-expand").text
        product_url = product.find('a',class_="product-item-link").get("href")
        image_url = product.find('img',class_="product-image-photo").get("data-amsrc")
        product_List.append({'product_name':product_name,'product__price':product__price,'product_brand':product_brand,'image_url':image_url,'product_url':product_url})         
        
    return product_List