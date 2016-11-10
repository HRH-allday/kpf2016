import numpy
from PIL import Image

test_im = None
test_img = None

def prob(fr,to):
    # 영규님 캐리 부탁드려요
    return (None, 1.000000)


def find_number():
    m = 36
    n = 96

    split = []
    value = numpy.zeros((n, 8), dtype = float)
    previ = numpy.zeros((n, 8), dtype = int)
    what_is_it = numpy.zeros((n,8), dtype = int)

    value[0][0] = 1
    #for j in range(1, 8):
    #    value[0][j] = 0

    for i in range(1, n):
        for j in range(1, 9):
            maxval = -1.0
            savedk = 0
            whatnum = 0
            for k in range(i-m+1):
                if i - k < 5: continue
                func_res = prob(k+1, i)
                val = value[k][j - 1] * func_res[1]
                if val > maxval:
                    maxval = val
                    savedk = k
                    whatnum = func_res[0]
            value[i][j] = maxval
            previ[i][j] = savedk
            what_is_it[i][j] = whatnum

    found_answer = 0
    line = n
    jari = 1
    for i in range(8,0,-1):
        if i > 1 and i < 8:
            found_answer += jari * what_is_it[line][i]
            jari *= 10
        line = previ[line][i]

        #split.insert(0, line)
    #split.insert(0, 0)
    # split = [0, ..., 96]
    return found_answer

def compare_with_answer():
    global test_im,test_img
    correct_counter = 0
    test_num = 7000
    iFile = open("sol.txt","r")
    for i in range(test_num):
        test_im = Image.open("datas/output" + str(ii) + ".png")
        test_img = test_im.load()
        if find_number() == int(iFile.readline().strip()):
            correct_counter += 1
    print("Result : %f%% Correct" % (100.0 * correct_counter / test_num))
