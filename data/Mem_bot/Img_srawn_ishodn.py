import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

def mse(imageA, imageB):
    # средняя квадратическая ошибка между двумя изображениями
    # сумма квадратов разности между двумя изображениями;
    # ПРИМЕЧАНИЕ: два изображения должны иметь одинаковый размер

    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # верните MSE, чем меньше ошибка, тем больше «похоже»
    # два изображения

    return err



def compare_images(imageA, imageB, title):
    # вычислить среднеквадратическую ошибку и структурное сходство
    # индекс для изображений
    m = mse(imageA, imageB)

    # настроить фигуру
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f" % (m))

    # показать первое изображение
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")

    # показать второе изображение
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")

    return m
    # показать изображения
    #plt.show()


def sravnenie(original_mem, mem):
        # конвертировать изображения в оттенки серого
        original_mem = cv2.cvtColor(original_mem, cv2.COLOR_BGR2GRAY)
        mem = cv2.cvtColor(mem, cv2.COLOR_BGR2GRAY)

        # инициализировать фигуру
        fig = plt.figure("Images")
        images = ("original_mem", original_mem), ("mem", mem)

        # цикл по изображениям
        for (i, (name, image)) in enumerate(images):
            # show the image
            ax = fig.add_subplot(1, 3, i + 1)
            ax.set_title(name)
            # plt.imshow(image, cmap=plt.cm.gray)
            # plt.axis("off")

        # show the figure

        # сравнить изображения
        delta = compare_images(original_mem, mem, "original_mem vs. mem")
        if int(delta) < 1000:
            plt.show()

# загрузка изображений - оригинал, оригинал + контраст,
# и оригинал + фотошоп
path = 'photo2'
a = os.listdir(path=path)
for i in range(len(a)):
    print(str(int(i/len(a)*100)) + '%')
    original_mem_name = a[i]
    for i2 in range(len(a)):
        mem_name = a[i2]
        original_mem = cv2.imread(path + '/' + original_mem_name)
        mem = cv2.imread(path + '/' + mem_name)
        if original_mem_name != mem_name:
            if original_mem.shape == mem.shape:
                sravnenie(original_mem, mem)
            elif original_mem.shape[0]/original_mem.shape[1] == mem.shape[0]/mem.shape[1]:
                x = original_mem.shape[0] / mem.shape[0]
                mem = cv2.resize(mem, (0,0), fx=x, fy=x)
                sravnenie(original_mem, mem)
            '''
            else:
                x = original_mem.shape[0] / mem.shape[0]
                mem = cv2.resize(mem, (0, 0), fx=x, fy=x)
                x = original_mem.shape[0] - mem.shape[0]
                y = original_mem.shape[1] - mem.shape[1]

                if y != 0:
                    if y > 0:
                        original_mem_crop = original_mem[0:0+mem.shape[0], 0:0+mem.shape[1]]
                print('hi')
            '''