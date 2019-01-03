def digitsProduct(product):
    """Given an integer product, find the smallest positive (i.e. greater than 
    0) integer the product of whose digits is equal to product. If there is no 
    such integer, return -1 instead."""

    if product == 0:
        return 10
    
    new_product = product
    divs = []
    
    while new_product > 9:
        new = new_product
        for num in [9, 8, 7, 6, 5, 4, 3, 2]:
            if new_product % num == 0:
                divs.append(str(num))
                new_product = int(new_product/num)
                break
        else:
            return -1
    
    divs.append(str(new_product))
    
    
    return int(''.join(sorted(divs)))


    # if product == 0:
    #     return 10
    
    # new_product = product
    # divs = []
    
    # while new_product > 9:
    #     new = new_product
    #     for num in [9, 8, 7, 6, 5, 4, 3, 2]:
    #         if new_product % num == 0:
    #             divs.append(str(num))
    #             new = int(new_product/num)
    #             break
    #     if new == new_product:
    #         return -1
    #     else:
    #         new_product = new
    
    # divs.append(str(new_product))
    
    
    # return int(''.join(sorted(divs)))