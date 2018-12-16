from skimage.measure import _structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

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
    s = ssim(imageA, imageB)

    # настроить фигуру
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

    # показать первое изображение
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")

    # показать второе изображение
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")

    # показать изображения
    plt.show()


# загрузка изображений - оригинал, оригинал + контраст,
# и оригинал + фотошоп
original = cv2.imread("photo1/1.jpg")
contrast = cv2.imread("photo1/2.jpg")
shopped = cv2.imread("photo1/3.jpg")

# конвертировать изображения в оттенки серого
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

# инициализировать фигуру
fig = plt.figure("Images")
images = ("Original", original), ("Contrast", contrast), ("Photoshopped", shopped)

# цикл по изображениям
for (i, (name, image)) in enumerate(images):
    # show the image
    ax = fig.add_subplot(1, 3, i + 1)
    ax.set_title(name)
    plt.imshow(image, cmap=plt.cm.gray)
    plt.axis("off")

# show the figure
plt.show()

# сравнить изображения
compare_images(original, original, "Original vs. Original")
compare_images(original, contrast, "Original vs. Contrast")
compare_images(original, shopped, "Original vs. Photoshopped")