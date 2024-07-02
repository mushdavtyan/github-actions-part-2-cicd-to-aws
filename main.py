import json
from yobi import Yobi


print("Starting Yobi API")
print("Loading Yobi")
print(Yobi.keys())


product_list = []
for product in Yobi['products']:
    product_info = {}
    for category in Yobi['categories']:
        for product_id in category['product_ids']:
            if product['id'] == product_id:
                product_info['category'] = category['name']
    product_info['name'] = product['name']
    product_info['protein'] = product['protein']
    product_info['fat'] = product['fat']
    product_info['carbs'] = product['carbs']
    product_info['energy'] = product['energy']
    product_info['weight'] = product['weight']
    product_info['description'] = product['description']
    product_info['image'] = {}
    product_info['image']['large'] = product['image']['large']
    product_info['image']['medium'] = product['image']['medium']
    product_info['image']['thumbnail'] = product['image']['thumbnail']
    product_info['badges'] = []
    if len(product['badge_ids']) > 0:
        for badge_ids in product['badge_ids']:
            for badge in Yobi['badges']:
                if badge['id'] == badge_ids:
                    product_info['badges'].append(badge['name'])
    product_info['tags'] = product['tags']
    product_list.append(product_info)

with open('products.json', 'w', encoding='utf-8') as json_file:
    json.dump(product_list, json_file, ensure_ascii=False, indent=4)
