import imageio
png_filenames = ['1.png', '2.png']
gif_filename = 'model.gif'

images = []
for png_filename in png_filenames:
    images.append(imageio.imread_v2(png_filename))
duration = 1000.0
imageio.mimwrite(gif_filename, images, duration=duration,
                 loop=100)