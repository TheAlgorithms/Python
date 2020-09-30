import argparse
import csv
import json
import os
import time
import urllib.request
from urllib.error import HTTPError

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)' \
             ' AppleWebKit/537.36 (KHTML, like Gecko)' \
             ' Chrome/35.0.1916.47 Safari/537.36'


def get_page(url, page, collection_handle=None):
    """
    Get page contents
    """
    full_url = url
    if collection_handle:
        full_url += '/collections/{}'.format(collection_handle)
    full_url += '/products.json'
    req = urllib.request.Request(
        full_url + '?page={}'.format(page),
        data=None,
        headers={
            'User-Agent': USER_AGENT
        }
    )
    while True:
        try:
            data = urllib.request.urlopen(req).read()
            break
        except HTTPError:
            print('Blocked! Sleeping...')
            time.sleep(180)
            print('Retrying')

    products = json.loads(data.decode())['products']
    return products


def get_page_collections(url):
    """
    Get Collections on the page using the json parsing
    """
    full_url = url + '/collections.json'
    page = 1
    while True:
        req = urllib.request.Request(
            full_url + '?page={}'.format(page),
            data=None,
            headers={
                'User-Agent': USER_AGENT
            }
        )
        while True:
            try:
                data = urllib.request.urlopen(req).read()
                break
            except HTTPError:
                print('Blocked! Sleeping...')
                time.sleep(180)
                print('Retrying')

        cols = json.loads(data.decode())['collections']
        if not cols:
            break
        for collection in cols:
            yield collection
        page += 1


def check_shopify(url):
    try:
        get_page(url, 1)
        return True
    except Exception:
        return False


def fix_url(url):
    fixed_url = url.strip()
    if not fixed_url.startswith('http://') and \
            not fixed_url.startswith('https://'):
        fixed_url = 'https://' + fixed_url

    return fixed_url.rstrip('/')


def extract_products_collection(url, col):
    page = 1
    products = get_page(url, page, col)
    while products:
        for product in products:
            title = product['title']
            print("Processing:", title)
            product_type = product['product_type']
            product_url = url + '/products/' + product['handle']
            product_handle = product['handle']

            def get_image(variant_id):
                images = product['images']
                for i in images:
                    k = [str(v) for v in i['variant_ids']]
                    if str(variant_id) in k:
                        return i['src']

                return ''

            for i, variant in enumerate(product['variants']):
                price = variant['price']
                option1_value = variant['option1'] or ''
                option2_value = variant['option2'] or ''
                option3_value = variant['option3'] or ''
                option_value = ' '.join([option1_value, option2_value,
                                         option3_value]).strip()
                sku = variant['sku']
                main_image_src = ''
                if product['images']:
                    main_image_src = [x['src'].strip() for x in product['images']]

                image_src = get_image(variant['id'])
                image_src_s = set()
                image_src_s.add(image_src.strip())
                image_src_s = image_src_s.union(main_image_src)
                image_src_l = list(image_src_s)
                if '' in image_src_l:
                    image_src_l.remove('')
                stock = 'Yes'
                if not variant['available']:
                    stock = 'No'

                row = {'sku': sku, 'product_type': product_type,
                       'title': title, 'option_value': option_value,
                       'price': price, 'stock': stock,
                       'body': str(product['body_html']),
                       'variant_id': product_handle + str(variant['id']),
                       'product_url': product_url, 'image_src': image_src_l}
                for k in row:
                    if type(row[k]) == str:
                        row[k] = str(row[k].strip()) if row[k] else ''
                yield row

        page += 1
        products = get_page(url, page, col)


def table_item(i):
    return f"<td> <pre> {i} </pre> </td>"


def img(link):
    return "<img src = \"" + link + '" height = 200px>'


def extract_products(url, path, collections=None, mkhtml=False):
    with open(path, 'w') as f:
        if mkhtml:
            htmlf = open(os.path.splitext(path)[0] + '.html', "w")
            htmlf.write("""<html> <head> <title> Summary </title>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>

</head> <body> <table> <tr>\
<th> SKU </th> <th> Collection\
 </th> <th> Category </th> <th>\
Name </th> <th> Variant Name </th>\
<th> Variant Price </th> <th> In Stock </th> <th> URL\
 </th> <th> Images </th> </tr>""")
        writer = csv.writer(f)
        writer.writerow(['sku', 'Collection', 'Type',
                         'Handle', 'Variant Name',
                         'Variant Price', 'In Stock', 'URL', 'Image Src', 'Body'])
        seen_variants = set()
        for col in get_page_collections(url):
            if collections and col['handle'] not in collections:
                continue
            handle = col['handle']
            title = col['title']
            for product in extract_products_collection(url, handle):
                variant_id = product['variant_id']
                if variant_id in seen_variants:
                    continue

                seen_variants.add(variant_id)
                print("Writing product:", product['title'])
                if mkhtml:
                    htmlf.write(f"<tr> {table_item(product['sku'])} \
{table_item(str(title))} {table_item(product['product_type'])}\
{table_item(product['title'])} {table_item(product['option_value'])}\
{table_item(product['price'])} {table_item(product['stock'])}\
<td> <a href = \"{product['product_url']}\" > \
{product['product_url']}</a> </td> <td>" + ' '.join(
                        [img(x) for x in product["image_src"]]) + "</td> </tr>")
                writer.writerow([product['sku'], str(title),
                                 product['product_type'],
                                 product['title'], product['option_value'],
                                 product['price'],
                                 product['stock'], product['product_url'],
                                 product['image_src'][0],
                                 product['body'].replace("\n", "")])
                for x in product['image_src'][1:]:
                    writer.writerow(['', '', '', product['title'], '', '', '',
                                     '', x, ''])
    if mkhtml:
        htmlf.write("</table> </body> </html>")
        htmlf.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser("shopify_web_scraper.py")
    parser.add_argument("--list-collections", action="store_true",
                        help="List collections in the site")
    parser.add_argument("--generate-html", action="store_true",
                        help="Make an extra HTML File which summarizes the extracted\
                         products")
    parser.add_argument("--collections", "-c", default="",
                        help="Download products only from the given collections\
                        (comma separated)")
    parser.add_argument("url", metavar="URL", help="Shopify URL")
    options = parser.parse_args()
    url = fix_url(options.url)
    if options.list_collections:
        for col in get_page_collections(url):
            print(col['handle'])
    else:
        collections = []
        if options.collections:
            collections = options.collections.split(',')
        extract_products(url, 'products.csv', collections, options.generate_html)
