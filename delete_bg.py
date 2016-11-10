from PIL import Image

rr = [-1,0,1,0]
cc = [0,1,0,-1]
im = None
img = None
width, height = None, None

def valid(c,r):
    return (0 <= r and r < height and 0 <= c and c < width)

def dodfs(c,r):
    img[c,r]=(0,0,0)
    for i in range(4):
        if valid(c+cc[i],r+rr[i]) and img[c+cc[i],r+rr[i]] == (255,255,255):
            dodfs(c+cc[i],r+rr[i])

for ii in range(0,7000):
    global im, img, width, height
    #im.show()
    im = Image.open("datas/output" + str(ii) + ".png")
    img = im.load()
    (width, height) = im.size
    ori_im = Image.new("RGB", (width, height))
    ori_img = ori_im.load()
    for i in range(0,width):
        for j in range(0,height):
            ori_img[i,j] = img[i,j]
    ccnt = 0
    for i in range(0,width):
        for j in range(0,height):
            (red,green,blue) = img[i,j]
            if max(max(red,green),blue) - min(min(red,green),blue) <= 5 and (red+green+blue<=384):
                img[i,j] = (255,255,255)
                ccnt += 1
            elif max(max(red,green),blue) - min(min(red,green),blue) <= 5:
                img[i,j] = (127,127,127)
            else:
                img[i,j] = (0,0,0)
    print(str(ii) + " " + str(width) + " " + str(height) + " " + str(ccnt))
    if(ccnt > 1200):
        for i in range(0, width):
            for j in range(0, height):
                if img[i,j] == (255,255,255):
                    img[i, j] = (0, 0, 0)
                    ccnt += 1
                elif img[i,j] == (127,127,127):
                    img[i, j] = (255, 255, 255)
                else:
                    img[i, j] = (0, 0, 0)
        nnew_im = Image.new("RGB", (width, height))
        nnew_img = nnew_im.load()
        for i in range(0,width):
            for j in range(0,height):
                nnew_img[i,j] = (0,0,0)
                if img[i,j] == (255,255,255):
                    nnew_img[i,j] = (255,255,255)
                else:
                    if valid(i,j-1):
                        if img[i,j-1] == (255,255,255):
                            nnew_img[i,j] = (255,255,255)
        new_im = Image.new("RGB", (width,height))
        new_img = new_im.load()
        for i in range(0, width):
            for j in range(0, height):
                new_img[i, j] = nnew_img[i,j]
    else:
        for i in range(0,width):
            for j in range(0,3):
                if img[i,j] == (255,255,255):
                    dodfs(i,j)
            for j in range(height-3,height):
                if img[i,j] == (255,255,255):
                    dodfs(i,j)
        for i in range(0, 2):
            for j in range(0, height):
                if img[i, j] == (255, 255, 255):
                    dodfs(i, j)
        for i in range(width-2, width):
            for j in range(0, height):
                if img[i, j] == (255, 255, 255):
                    dodfs(i, j)
        new_im = Image.new("RGB",(width,height))
        new_img = new_im.load()
        for i in range(0,width):
            for j in range(0,height):
                new_img[i,j] = img[i,j]
    all_new_im = Image.new("RGB",(width,height))
    all_new_img = all_new_im.load()
    for i in range(0,width):
        for j in range(0,height):
            all_new_img[i,j]=new_img[i,j]
            if all_new_img[i,j] != (0,0,0):
                all_new_img[i,j] = ori_img[i,j]
                continue
            for k in range(4):
                if valid(i+cc[k],j+rr[k]) and new_img[i+cc[k],j+rr[k]] == (255,255,255):
                    all_new_img[i,j] = (ori_img[i,j][0]//2+18, ori_img[i,j][1]//2+61, ori_img[i,j][2]//2+21)
                    break
            if all_new_img[i,j] == (0,0,0):
                all_new_img[i,j] = (35,122,41)
    all_new_im.save("green/result"+str(ii)+".bmp")
