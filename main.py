from bs4 import BeautifulSoup
import csv
import requests
import datetime

def grab_list(cate):
    html_site = requests.get('https://www.swiggy.com/restaurants/istah-shawarma-yelahanka-bangalore-498298').text
    html_site2 = requests.get(
        'https://www.swiggy.com/restaurants/sangam-sweets-yelahanka-vignana-kendra-bangalore-70002').text
    html_site3=requests.get('https://www.swiggy.com/restaurants/juice-pump-poonamallee-high-road-egmore-chennai-14052').text
    soup = BeautifulSoup(html_site, 'lxml')
    soup2 = BeautifulSoup(html_site2, 'lxml')
    soup3=BeautifulSoup(html_site3,'lxml')
    tag = soup.find_all('div', class_='styles_detailsContainer__22vh8')
    tag2 = soup2.find_all('div', class_='styles_detailsContainer__22vh8')
    tag3=soup3.find_all('div', class_='styles_detailsContainer__22vh8')
    fil = []
    fil2 = []
    fil3=[]
    x=datetime.datetime.now()
    for index, tags in enumerate(tag):
        name = tags.find('h3', class_='styles_itemNameText__3ZmZZ').text.replace('  ', '')
        price = tags.find('span', class_='rupee').text
        famous = tags.find('span', class_='styles_ribbon__3tZ21 styles_itemRibbon__353Fy')
        if(cate=='1'):
            veg = tags.find('i', class_='styles_icon__m6Ujp styles_itemIcon__1LXTw icon-Veg styles_iconVeg__shLxJ')
        else:
            veg = tags.find('i', class_='styles_icon__m6Ujp styles_itemIcon__1LXTw icon-NonVeg')
        if (veg):
            temp = []
            temp.append(name)
            temp.append(price)
            if (famous):
                temp.append('Bestseller')
            fil.append(temp)
    for index, tags in enumerate(tag2):
        name = tags.find('h3', class_='styles_itemNameText__3ZmZZ').text.replace('  ', '')
        price = tags.find('span', class_='rupee').text
        famous = tags.find('span', class_='styles_ribbon__I8tP9 styles_itemRibbon__2ib09')
        if(cate=='1'):
            veg = tags.find('i', class_='styles_icon__m6Ujp styles_itemIcon__1LXTw icon-Veg styles_iconVeg__shLxJ')
        else:
            veg = tags.find('i', class_='styles_icon__m6Ujp styles_itemIcon__1LXTw icon-NonVeg')
        if (veg):
            temp = []
            temp.append(name)
            temp.append(price)
            if (famous):
                temp.append('Bestseller')
            fil2.append(temp)
    for index, tags in enumerate(tag3):
        name = tags.find('h3', class_='styles_itemNameText__3ZmZZ').text.replace('  ', '')
        price = tags.find('span', class_='rupee').text
        famous = tags.find('span', class_='styles_ribbon__I8tP9 styles_itemRibbon__2ib09')
        if (cate=='1'):
            veg = tags.find('i', class_='styles_icon__m6Ujp styles_itemIcon__1LXTw icon-Veg styles_iconVeg__shLxJ')
        else:
            veg = tags.find('i', class_='styles_icon__m6Ujp styles_itemIcon__1LXTw icon-NonVeg')
        if(veg):
            temp = []
            temp.append(name)
            temp.append(price)
            if(famous):
                temp.append('Bestseller')
            fil3.append(temp)
    if(cate=='1'):
        with open(f'Swiggy Veg {x.date()} .csv', 'w') as csvfile:
            write = csv.writer(csvfile)
            header = ['Title', 'Price(Rs)','Recommendations']
            write.writerow(header)
            write.writerows(fil)
            write.writerows(fil2)
            write.writerows(fil3)
    else:
        with open(f'Swiggy Non-Veg {x.date()} .csv', 'w') as csvfile:
            write = csv.writer(csvfile)
            header = ['Title', 'Price(Rs)','Recommendations']
            write.writerow(header)
            write.writerows(fil)
            write.writerows(fil2)
            write.writerows(fil3)

if __name__=='__main__':
    filter=input("Enter 1 for veg and 2 for non-veg\n")
    grab_list(filter)
    print('Done')

