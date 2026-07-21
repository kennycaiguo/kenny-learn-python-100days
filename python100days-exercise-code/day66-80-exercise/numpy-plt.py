import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

pic = plt.imread('./cutegirl3.jpg')

# plt.imshow(pic)
# plt.imshow(pic[::-1]) # 图片上下翻转
# plt.imshow(pic[:,::-1]) # 图片左右翻转
# 图片马赛克
plt.imshow(pic[::5,::5])
plt.show()