>>> x = {'fix_info': ['product_requested_info', 'platform_requested_info']}  (old)
>>> y = {'fix_info': ['product_provided_info', 'attribute_requested_info']}   (new)
>>> z = x['fix_info'] + y['fix_info']
>>> z
['product_requested_info', 'platform_requested_info', 'product_provided_info', 'attribute_requested_info']
>>> p = list(filter(lambda l: 'product_' in l, z))
>>> p
['product_requested_info', 'product_provided_info']
>>> q = list(set(z) - set(p))
>>> q
['attribute_requested_info', 'platform_requested_info']
>>> q.append(p[-1])
>>> q
['attribute_requested_info', 'platform_requested_info', 'product_provided_info']

