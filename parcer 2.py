# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd


def dannie(link):
    url = f'{link}'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'cookie': 'detmir_feature_subscriptions=0; ab2_90=ab2_90old90; ab2_33=ab2_33old34; ab2_50=33; ab3_75=ab3_75old75; ab3_33=ab3_33new33; ab3_20=ab3_20_20_3; cc=0; _ym_d=1635512483; _ym_uid=1635512483665798581; _gcl_au=1.1.6086262.1635512483; rrpvid=205495571825617; advcake_track_id=7f85771b-9c44-bf58-f5a3-d24fb1c1a8c2; advcake_session_id=8984f69a-cedb-8ce7-e9be-9b970c2621f5; _ga=GA1.2.1723963057.1635512484; _gid=GA1.2.201445372.1635512484; transactionId=19f5bcb6-e4e5-4d3f-873f-9f52a7de5170.0; transactionSubId=0b0c053d-2e85-44a8-8301-3ba34f34a534.0; geoCityDM=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C; geoCityDMIso=RU-MOW; geoCityDMCode=undefined; rcuid=617bf0a37e0f0b00011a7d93; auid=21e34d4d-994e-46f5-863e-3edb94afd685; flocktory-uuid=32b09c9d-801c-41f2-8ff0-35eda240c21b-8; dm.cookieMobileAppNotification=no; uid=X6OKmmF9KBJrcZPgBeLTAg==; JSESSIONID=9bceea0c-7125-44d0-a2ee-5b1c29d6ae75; detmir-cart=922be914-001c-478e-9026-a54bfe577b78; srv_id=cubic-front12-prod; _ym_isad=1; dm_s=L-9bceea0c-7125-44d0-a2ee-5b1c29d6ae75|kH922be914-001c-478e-9026-a54bfe577b78|Vj21e34d4d-994e-46f5-863e-3edb94afd685|gqcubic-front12-prod|qab3584ae9-d62c-4b4e-b5f8-4394ad64589c|118ac5d8cb-b6b7-4d15-ac87-755385dac988#jHozMG5JyYkiFSk2rwWDDMs7SOsxeI6VvM-0YYSFR70; listingLink=https://www.detmir.ru/catalog/index/name/lego/page/3/; _fbp=fb.1.1635605033022.1366026479; mindboxDeviceUUID=8478bf50-3576-42f3-b677-480beca6516a; directCrm-session=%7B%22deviceGuid%22%3A%228478bf50-3576-42f3-b677-480beca6516a%22%7D; _gat=1; qrator_msid=1635603510.545.FSa9X5Equr41he1O-v7p2e5u25h9e7tb1623talobb7d790n7; _gat_test=1'
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    # print(soup)
    quotes = soup.find_all('h1', class_='rQ rR')
    promo = soup.find_all('div', class_='Cj')
    cena = soup.find_all('span', class_='Cl')
    for quote in quotes:
        id = ''.join([i for i in quote.text if i.isdigit()])
        naim = ''.join([i for i in quote.text if not i.isdigit()])
    for prom in promo:
        promo = ''.join([i for i in prom.text if i.isdigit()])
    for cen in cena:
        money = ''.join([i for i in cen.text if i.isdigit()])

    # print(id, naim, money, promo, link)

    bd(id, naim, money, promo, link)


def bd(id, naim, money, promo, link):
    global df
    df.loc[len(df)] = [id, str(naim), money, promo, link]




df = pd.DataFrame([], columns=["id", "title", "price", "promo_price", "url"], )
for i in range(1,61):
    url = f'https://www.detmir.ru/catalog/index/name/lego/page/1/'
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': 'detmir_feature_subscriptions=0; ab2_90=ab2_90old90; ab2_33=ab2_33old34; ab2_50=33; ab3_75=ab3_75old75; ab3_33=ab3_33new33; ab3_20=ab3_20_20_3; cc=0; _ym_d=1635512483; _ym_uid=1635512483665798581; _gcl_au=1.1.6086262.1635512483; rrpvid=205495571825617; advcake_track_id=7f85771b-9c44-bf58-f5a3-d24fb1c1a8c2; advcake_session_id=8984f69a-cedb-8ce7-e9be-9b970c2621f5; _ga=GA1.2.1723963057.1635512484; _gid=GA1.2.201445372.1635512484; transactionId=19f5bcb6-e4e5-4d3f-873f-9f52a7de5170.0; transactionSubId=0b0c053d-2e85-44a8-8301-3ba34f34a534.0; geoCityDM=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C; geoCityDMCode=undefined; geoCityDMIso=RU-MOW; rcuid=617bf0a37e0f0b00011a7d93; auid=21e34d4d-994e-46f5-863e-3edb94afd685; flocktory-uuid=32b09c9d-801c-41f2-8ff0-35eda240c21b-8; dm.cookieMobileAppNotification=no; uid=X6OKmmF9KBJrcZPgBeLTAg==; JSESSIONID=9bceea0c-7125-44d0-a2ee-5b1c29d6ae75; detmir-cart=922be914-001c-478e-9026-a54bfe577b78; srv_id=cubic-front12-prod; _ym_isad=1; dm_s=L-9bceea0c-7125-44d0-a2ee-5b1c29d6ae75|kH922be914-001c-478e-9026-a54bfe577b78|Vj21e34d4d-994e-46f5-863e-3edb94afd685|gqcubic-front12-prod|qab3584ae9-d62c-4b4e-b5f8-4394ad64589c|118ac5d8cb-b6b7-4d15-ac87-755385dac988#jHozMG5JyYkiFSk2rwWDDMs7SOsxeI6VvM-0YYSFR70; qrator_msid=1635603510.545.FSa9X5Equr41he1O-87vd5eorcgdvei2d84c3su3i6f5qh808; _ym_visorc=w; _gat=1; _gat_test=1; listingLink=https://www.detmir.ru/catalog/index/name/lego/; mindboxDeviceUUID=8478bf50-3576-42f3-b677-480beca6516a; directCrm-session=%7B%22deviceGuid%22%3A%228478bf50-3576-42f3-b677-480beca6516a%22%7'
}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    quotes = soup.find_all('a', class_='Lv LX')
    for quote in quotes:
        a = quote.get('href')
        print(a)
        dannie(a)
# print(df)
df.to_csv("price.csv", sep='|', encoding='cp1251',index=False, header=0, )
