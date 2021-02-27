from PIL import Image

print("\nScenarios: BEACH - DESERT - EARTH - FIELD - FOREST - SNOWSCAPE - SUNSET")

scenario = input("\nChoose a scenario among that: ").lower()

print("\nObjects: BOAT - CACTUS - CAT - HARVESTER - HIKER - PENGUIN - SPACESHUTTLE")

item = input("\nChoose a object among that: ").lower()

print("\nFilters: RED - BLUE - GREEN - NONE")

filter = input("\nChoose a filter among that: ").lower()

image_original = Image.open(f"{scenario}.jpg")

cactus_image = Image.open(f"{item}.jpg")

pixels_original = image_original.load()

cactus_pixel = cactus_image.load()

image_new = Image.new("RGB", image_original.size)

pixels_new = image_new.load()

for x in range(0, 800):   

    for y in range(0, 600):

        (r, g, b) = cactus_pixel[x , y]        

        if r <= 150 and g >= 170 and b <= 150:

            if filter == "red":

                (r, g, b) = pixels_original[x,y]

                r = r + 100         

                pixels_new[x,y] = (r, g, b)

            elif filter == "blue":
                
                (r, g, b) = pixels_original[x,y]

                b = b + 100         

                pixels_new[x,y] = (r, g, b)
            
            elif filter == "green":
                
                (r, g, b) = pixels_original[x,y]

                g = g + 100         

                pixels_new[x,y] = (r, g, b)
            
            else:

                (r, g, b) = pixels_original[x,y]        

                pixels_new[x,y] = (r, g, b)

        else:
            (r, g, b) = cactus_pixel[x , y]

            pixels_new[x,y] = (r, g, b)

image_new.show()

image_new.save("the_new_image.jpg")

print("\nThank for your participation!")