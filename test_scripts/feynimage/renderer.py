import cv2 as cv
import sys
import numpy as np

img = cv.imread("mona.jpg")

if img is None:
    sys.exit("Could not read the image.")

grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def get_vec_field(gray, radius, size, g_const=1):
    ret = np.zeros((size, size, 2))
    ret2 = np.zeros((size, size))

    for x in range(size):

        for y in range(size):
            # print(x,y)
            fx, fy = 0, 0
            for dx in range(-radius, radius + 1):
                for dy in range(-radius, radius + 1):
                    if size > (x + dx) > 0  and 0 != dx and size > (y + dy) > 0 and 0 != dy:
                        fx = fx + g_const * gray[x+dx][y+dy]/(dx**2 + dy**2) * np.cos(dx/np.sqrt((dx**2 + dy**2)))
                        fy = fy + g_const * gray[x+dx][y+dy]/(dx**2 + dy**2) * np.sin(dy/np.sqrt((dx**2 + dy**2)))
                    # else:
                        # print(x, dx, size > x + dx > 0)
                        # print(y, dy, size > y + dy > 0)

            ret[x][y][0] = fx
            ret[x][y][0] = fy

            ret2[x][y] = np.sqrt(fx**2 + fy**2)

    print(ret2, np.max(ret2), np.min(ret2))
    return ret, 1*ret2/np.max(ret2)


vf, r = get_vec_field(grayimg, 3, 256)

print(vf)
print(r)




cv.imshow("Display window", r)
cv.imwrite("mona_gray.jpg", r)
k = cv.waitKey(0)

