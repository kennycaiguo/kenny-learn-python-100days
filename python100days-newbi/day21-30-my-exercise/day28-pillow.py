"""pip install pillow
   after the installation,the package name PIL
"""
from PIL import Image

def load_img(path):
    image = Image.open(path)
    # the pic format
    print(image.format) # JPEG
    # size,property not function
    print(image.size) # (736, 1104)
    # show the image
    # image.show()
    return image
def crop_image():
    img = load_img("resources/arbolgold.jpg")
    # crop the pic
    cropped = img.crop((80, 20, 310, 360))
    cropped.save("./resources/cropped.jpg")

def create_thumdnail(img):
    img.thumbnail((50,50))  
    img.show()
    img.save("./resources/thumd.jpg")

# img = load_img("resources/arbolgold.jpg")
# create_thumdnail(img)
def paste_test():
    # load one pic and paste to another
    thumd = load_img("./resources/thumd.jpg")
    img = load_img("./resources/couple.jpg")
    width,height = thumd.size
    img.paste(thumd,(300,50))
    img.show()

def rotate_flip():
    # rotation and flip
    horse = load_img("./resources/msfc.jpg")    
    rotated = horse.rotate(90)
    # rotated.show()
    # transpose()
    # Image.FLIP_LEFT_RIGHT - 水平翻转
    # Image.FLIP_TOP_BOTTOM - 垂直翻转
    # flip = horse.transpose(Image.FLIP_LEFT_RIGHT)
    flip = horse.transpose(Image.FLIP_TOP_BOTTOM)
    flip.show()
    # flip.save("./resources/msfcr.jpg")

def pixel_op():
    img = load_img("./resources/couple.jpg")
    for i in range(120):
        for j in range(80):
            img.putpixel((i,j),(200,100,300))
    img.show()

# pixel_op()

def filter_effect():
    from PIL import ImageFilter
    img = load_img("./resources/guido.jpg")
    # img.filter(ImageFilter.CONTOUR).show()
    # img.filter(ImageFilter.BLUR).show()
    # img.filter(ImageFilter.BoxBlur(radius=5)).show()
    # img.filter(ImageFilter.DETAIL).show() # no effect
    # img.filter(ImageFilter.EDGE_ENHANCE).show() 
    # img.filter(ImageFilter.EDGE_ENHANCE_MORE).show() 
    # img.filter(ImageFilter.EMBOSS).show()  # 浮雕效果
    # img.filter(ImageFilter.FIND_EDGES).show() #边缘查找效果
    # img.filter(ImageFilter.SHARPEN).show() 
    # img.filter(ImageFilter.SMOOTH).show() 
    # img.filter(ImageFilter.SMOOTH_MORE).show() 
   

# filter_effect()

def do_img_draw():
    import random

    from PIL import Image, ImageDraw, ImageFont


    def random_color():
        """生成随机颜色"""
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return red, green, blue


    width, height = 800, 600
    # 创建一个800*600的图像，背景色为白色
    image = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    # 创建一个ImageDraw对象
    drawer = ImageDraw.Draw(image)
    # 通过指定字体和大小获得ImageFont对象
    font = ImageFont.truetype('./resources/fonts/KongXinSongKai-2.ttf', 32)
    # 通过ImageDraw对象的text方法绘制文字
    drawer.text((300, 50), 'Hello, world!', fill=(255, 0, 0), font=font)
    # 通过ImageDraw对象的line方法绘制两条对角直线
    drawer.line((0, 0, width, height), fill=(0, 0, 255), width=2)
    drawer.line((width, 0, 0, height), fill=(0, 0, 255), width=2)
    xy = width // 2 - 60, height // 2 - 60, width // 2 + 60, height // 2 + 60
    # 通过ImageDraw对象的rectangle方法绘制矩形
    drawer.rectangle(xy, outline=(255, 0, 0), width=2)
    # 通过ImageDraw对象的ellipse方法绘制椭圆
    for i in range(4):
        left, top, right, bottom = 150 + i * 120, 220, 310 + i * 120, 380
        drawer.ellipse((left, top, right, bottom), outline=random_color(), width=8)
    # 显示图像
    image.show()
    # 保存图像
    image.save('./resources/result.png')


do_img_draw()