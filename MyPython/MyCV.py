
import cv2 as cv

DEFAULT_TITLE = 'show_img'
def show_img(img, title=DEFAULT_TITLE):
    cv.imshow(title, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def show_imgs(imgs, title=DEFAULT_TITLE):
    for img in imgs: show_img(img, title)

