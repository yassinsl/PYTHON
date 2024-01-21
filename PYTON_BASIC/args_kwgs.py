def add(*number):
    c = 0
    for i in number:
        c = c + i
    print("addition is %d" % c)

add(100,200,300)
def adress(**adss):
    print("Address is {}".format(adss.get('address', 'No address provided')))

adress(address="TEFLET")
