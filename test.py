# -*- coding: utf-8 -*-
import pylab
import imageio
#视频的绝对路径
filename = '/Users/arbin/Desktop/python/zzknows/test.m'
#可以选择解码工具
vid = imageio.get_reader(filename,  'ffmpeg')

fps = vid.get_meta_data()['fps']

print vid.get_meta_data(0)

print vid.get_meta_data(1)

print fps
 
writer = imageio.get_writer('~/cockatoo_gray.mp4', fps=fps)
 
for im in vid:
    writer.append_data(im[:, :, 1])
writer.close()

# for im in enumerate(vid):
#     #image的类型是mageio.core.util.Image可用下面这一注释行转换为arrary
#     #image = skimage.img_as_float(im).astype(np.float32)
#     fig = pylab.figure()
#     fig.suptitle('image #{}'.format(num), fontsize=20)
#     pylab.imshow(image)
# pylab.show()