def main():
    with open('image.ppm', 'a') as file_:
        file_.write('P3 500 500 255\n')
        for i in xrange(500):
            for j in xrange(500):
                red = (i + j) % 256
                green = j % 256
                blue = 255
                file_.write('%d %d %d\n' % (red, green, blue))

if '__main__' == __name__:
    main()
