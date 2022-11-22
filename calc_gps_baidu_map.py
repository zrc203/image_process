# 经度116.4721063°，纬度40.0289314°
# 2.六十进制
# 东经116°28'19.583"，北纬40°1'44.153"
#106.632627,26.685781
def calc(source):
    degree = int(source)
    t = ((source - degree) * 3600 / 60)
    minute = int(t)
    sec = (t - minute) * 60
    sec = str(sec).replace('.', '')[:8]
    print(f'(({degree}, 1), ({minute}, 1), ({sec}, 1000000))')

def pra(a,b):
    print("exif_dic['GPS'][2] = ", end='')
    calc(b)
    print("exif_dic['GPS'][4] = ", end='')
    calc(a)

pra(106.645689,26.377698)