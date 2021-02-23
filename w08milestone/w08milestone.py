from PIL import Image

image_original = Image.open(f"beach.jpg")

cactus_image = Image.open(f"penguin.jpg")

pixels_original = image_original.load()

cactus_pixel = cactus_image.load()

image_new = Image.new("RGB", image_original.size)

pixels_new = image_new.load()

for x in range(0, 800):   

    for y in range(0, 600):

        (r, g, b) = cactus_pixel[x , y]

        if r <= 120 and g >= 170 and b <= 120:

            (r, g, b) = pixels_original[x,y]

            new_red = r + 50

            pixels_new[x,y] = (new_red, g, b)
        else:
            (r, g, b) = cactus_pixel[x , y]

            pixels_new[x,y] = (r, g, b)

image_new.show()

image_new.save("the_new_image.jpg")

question = input("\nWhat did you see? ")

print(f"\nYou saw {question}")

print("\nThank for your participation!")