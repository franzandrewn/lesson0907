from PIL import Image, ImageEnhance

image = Image.open("logo.png")
# image.show()
print(image)

enh = ImageEnhance.Contrast(image)
image = enh.enhance(3)
image.show()

outname = "logo_enchanced.png"
image.save(outname)

# 1. (Опционально, если нет своей папки) Создать папку, открыть её через File -> Open folder
# 2. Создать виртуальное окружение: py -m venv .venv
# 3. С помощью автодополнения (клавиша tab) запустить .\.venv\Scripts\Activate.ps1
# 4. (При ошибке п.3) Запустить команду Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process 
# (найти можно через google статья "Using Python environments in VS Code")
# 5. Запустить команду "pip list" для просмотра модулей в виртуальном окружении, там должны быть pip и setuptools
# 6. Запустить команду "pip install Pillow", для установки Pillow и проверить результат через "pip list" 
# (в списке должен появится Pillow)
# 7. Скачать/скопировать любое изображение в папку рядом с .py файлами, поменять имя на простое
# 8. Открыть картинку
# 9. Увеличить/уменьшить один из параметров через ImageEnchance
# 10. Сохранить измененную картинку под новым названием