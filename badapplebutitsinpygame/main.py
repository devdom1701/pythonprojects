# :Dominik Rosman
# 12/24/24
import os
import pygame
from PIL import Image

# Pygame initialization
pygame.init()

# constants

WINDOW_SIZE = 800  # window size (can be larger than the image to add padding
IMAGE_WIDTH = 480  # width of the original image
IMAGE_HEIGHT = 360  # height of the original image

SCALE_FACTOR = 2 # scale factor: 2 original image pixels from the frames folder = 1 pygame pixel
# set this to 32 for fun low-quality image generation

PRIMARY_COLOR = (255, 255, 255) # these are the primary and secondary colors used in the animation, defaulted to white and black to avoid potential errors
SECONDARY_COLOR = (0, 0, 0)

BGCOLOR = SECONDARY_COLOR  # sets the background to the secondary color
FPS = 30  # the frames per second at which the animation will be displayed

# brightness thresholds
PRIMARY_THRESHOLD = 50  # below this sum() is black, (the secondary color)
SECONDARY_THRESHOLD = 200  # above this sum() is white, (the primary color)

# dicitonary of colors to choose from and their corresponding RGB values
COLORSASKING = True
COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "alabaster": (242, 240, 230),
    "amaranth": (229, 43, 80),
    "amber": (255, 191, 0),
    "antique_white": (250, 235, 215),
    "apple_green": (141, 182, 0),
    "apricot": (251, 206, 177),
    "aqua_marine": (127, 255, 212),
    "azure": (240, 255, 255),
    "beau_blue": (188, 212, 230),
    "beige": (245, 245, 220),
    "bistre": (61, 43, 31),
    "bittersweet": (254, 111, 94),
    "black_olive": (59, 60, 54),
    "blanched_almond": (255, 235, 205),
    "blue_violet": (138, 43, 226),
    "blush": (222, 93, 131),
    "bondi_blue": (0, 149, 182),
    "brass": (181, 166, 66),
    "bright_azure": (0, 191, 255),
    "bright_turquoise": (8, 232, 222),
    "brown_sugar": (200, 128, 51),
    "bubblegum": (255, 193, 204),
    "cadet_blue": (95, 158, 160),
    "camel": (193, 154, 107),
    "caribbean_green": (0, 204, 153),
    "celadon": (172, 225, 175),
    "cerulean": (42, 82, 190),
    "champagne": (247, 231, 204),
    "charcoal": (54, 69, 79),
    "cherry_blossom": (255, 183, 197),
    "chestnut": (205, 92, 92),
    "chocolate": (123, 63, 0),
    "cinnabar": (233, 36, 36),
    "cobalt": (0, 71, 171),
    "coffee": (111, 78, 55),
    "copper": (184, 115, 51),
    "cornflower_blue": (100, 149, 237),
    "cream": (255, 253, 208),
    "crimson": (220, 20, 60),
    "cultured": (241, 241, 241),
    "khaki": (195, 176, 145),
    "cyan_ray": (102, 255, 255),
    "dark_brown": (101, 67, 33),
    "dark_cyan": (0, 139, 139),
    "dark_gold": (204, 204, 0),
    "dark_olive_green": (85, 107, 47),
    "dark_orchid": (153, 50, 204),
    "dark_sea_green": (143, 188, 143),
    "dark_slate_blue": (72, 61, 139),
    "dark_slate_gray": (47, 79, 79),
    "dark_turquoise": (0, 206, 209),
    "dark_violet": (148, 0, 211),
    "deep_pink": (255, 20, 147),
    "deep_sky_blue": (0, 191, 255),
    "denim": (21, 96, 189),
    "emerald": (80, 200, 120),
    "flame": (226, 85, 34),
    "flax": (238, 220, 130),
    "fuchsia": (255, 0, 255),
    "ghost_white": (248, 248, 255),
    "goldenrod": (218, 165, 32),
    "green_yellow": (173, 255, 47),
    "heliotrope": (223, 115, 255),
    "honeydew": (240, 255, 240),
    "hot_pink": (255, 105, 180),
    "indian_red": (205, 92, 92),
    "indigo": (75, 0, 130),
    "ivory": (255, 255, 240),
    "jade": (0, 168, 107),
    "jasmine": (248, 222, 126),
    "jazzberry_jam": (186, 59, 94),
    "lavender_blush": (255, 240, 245),
    "lemon_chiffon": (255, 250, 205),
    "light_coral": (240, 128, 128),
    "light_cyan": (224, 255, 255),
    "light_goldenrod_yellow": (250, 250, 210),
    "light_gray": (211, 211, 211),
    "light_green": (144, 238, 144),
    "light_pink": (255, 182, 193),
    "light_salmon": (255, 160, 122),
    "light_sea_green": (32, 178, 170),
    "light_sky_blue": (135, 206, 250),
    "light_slate_gray": (119, 136, 153),
    "light_steel_blue": (176, 224, 230),
    "light_yellow": (255, 255, 224),
    "lilac": (200, 162, 200),
    "lime_green": (50, 205, 50),
    "linen": (250, 240, 230),
    "malachite": (11, 218, 81),
    "manatee": (151, 154, 170),
    "midnight_blue": (25, 25, 112),
    "mint_cream": (245, 255, 250),
    "misty_rose": (255, 228, 225),
    "moss_green": (138, 154, 91),
    "mulberry": (197, 75, 140),
    "navajo_white": (255, 222, 173),
    "olive_drab": (107, 142, 35),
    "orange_red": (255, 69, 0),
    "orchid": (218, 112, 214),
    "papaya_whip": (255, 239, 150),
    "peach": (255, 229, 180),
    "periwinkle": (204, 204, 255),
    "persian_blue": (28, 57, 187),
    "plum": (221, 160, 221),
    "powder_blue": (176, 224, 230),
    "raspberry": (227, 11, 93),
    "rose": (255, 0, 127),
    "rosewood": (101, 0, 11),
    "royal_blue": (65, 105, 225),
    "saddle_brown": (139, 69, 19),
    "seashell": (255, 245, 238),
    "shadow": (138, 121, 93),
    "silver": (192, 192, 192),
    "snow": (255, 250, 250),
    "spring_green": (0, 255, 127),
    "sunset": (250, 214, 165),
    "thistle": (216, 191, 216),
    "tomato": (255, 99, 71),
    "turquoise": (64, 224, 208),
    "vermilion": (227, 66, 52),
    "violet": (238, 130, 238),
    "wheat": (245, 222, 179),
    "white_smoke": (245, 245, 245),
    "yellow_green": (154, 205, 50)
}

# asking of primary and secondary colors for the animation
if COLORSASKING:
    # getting a primary color from the user
    userprimaryselection = input("What should the primary color of the animation be? ").lower()
    if userprimaryselection in COLORS:
        PRIMARY_COLOR = COLORS[userprimaryselection]
    else:
        print(f"not supported color '{userprimaryselection}'. choose a valid color (red, green, blue, yellow, cyan, magenta, black, white, orange, purple).")
    # getting a secondary color from the user
    if COLORSASKING:
        usersecondaryselection = input("What should the secondary color of the animation be? ").lower()
        if usersecondaryselection in COLORS:
            SECONDARY_COLOR = COLORS[usersecondaryselection]
        else:
            print(f"not supported color '{usersecondaryselection}'. choose a valid color (red, green, blue, yellow, cyan, magenta, black, white, orange, purple).")
    if COLORSASKING:
        hunkypccheck = input("do you have a pc with >8 gigabytes of ram (this option disables loading-time, but costs more cpu power) (Y)es or (N)o").lower()
        if hunkypccheck == "y" or hunkypccheck ==  "yes":
            hunkypc = True
        else:
            hunkypc = False
    if COLORSASKING:
        ASKTERTIARY_COLOR = input("Do you want a tertiary color? (Y)es or (N)o ").lower()
        if ASKTERTIARY_COLOR == "y" or ASKTERTIARY_COLOR ==  "yes":
            TERTIARY_COLOR = input("What should be the terriary color?").lower()
            if TERTIARY_COLOR in COLORS:
                TERTIARY_COLOR = COLORS[TERTIARY_COLOR]
                COLORSASKING = False
                ISTERTIARY_COLOR = True
            else:
                print(f"not supported color '{usersecondaryselection}'. choose a valid color (red, green, blue, yellow, cyan, magenta, black, white, orange, purple).")
        else:
            ISTERTIARY_COLOR = False
            COLORSASKING = False

if COLORSASKING:
    print(f"Primary color set to {userprimaryselection.capitalize()}: {PRIMARY_COLOR}")
    print(f"Secondary color set to {usersecondaryselection.capitalize()}: {SECONDARY_COLOR}")
else:
    print("Color selection process was not successful.")

class Visualizer:
    def __init__(self, screen):
        self.screen = screen
        self.imagepixels = []  # storage of pixel data

        self.imagewidth = IMAGE_WIDTH
        self.imageheight = IMAGE_HEIGHT

        self.scaled_width = IMAGE_WIDTH // SCALE_FACTOR # the scaled height and width that the animation screen will eventually have
        self.scaled_height = IMAGE_HEIGHT // SCALE_FACTOR

    def get_image_pixels(self, imagepath):
        im = Image.open(imagepath).convert("RGB")  # converting the image to RGB values
        pixels = list(im.getdata())  # converting the original image to a list of pixels

        for pixel in pixels:
            brightness = sum(pixel) / 3  # this gets the average brightness pixels, a way i found to distinguish the pixels
            # the sum() function adds up all the values of the pixels, ex: sum(0,2,1) = 3
            if brightness <= PRIMARY_THRESHOLD:
                self.imagepixels.append(SECONDARY_COLOR)
            elif brightness >= SECONDARY_THRESHOLD:
                self.imagepixels.append(PRIMARY_COLOR)
            else:
                # default to the primary color if its still in between thresholds
                if ISTERTIARY_COLOR == True:
                    self.imagepixels.append(TERTIARY_COLOR)
                else:
                    self.imagepixels.append(PRIMARY_COLOR)

    def reprocessimage(self, imagepath):
         # this is to avoid the lists getting exponentially larger, 
         # because the frames generate after one another and keep the previous frames data; which i do NOT want
        self.imagepixels = []
        self.get_image_pixels(imagepath)

    def render_frame(self):
        # Starting coordinates from top-left corner (We are in quadrant IV in pygame so its weird)
        x = 150
        y =  200
        # lopping through each row and column in the scaled image height
        for row in range(self.scaled_height):
            for col in range(self.scaled_width):

                # this finds the original x coordinates and y coordinates of pixels in the original image
                original_x = col * SCALE_FACTOR
                
                original_y = row * SCALE_FACTOR
                
                # calculates the index of the single pixel, by treating the pixel list like a spreadsheet
                # the original_y is the columns, the image width how many columns, 
                # and the original x is how far down the spreadsheet we're going

                index = original_y * self.imagewidth + original_x
                
                # getting the color of the individual pixel from the list of imagepixels
                color = self.imagepixels[index]

                # drawing a rectagle to represent the pixel
                pygame.draw.rect(self.screen, color, (x, y, SCALE_FACTOR, SCALE_FACTOR))
                
                # incrimenting the x-coordinate for the next pixel to be created
                x += SCALE_FACTOR

            x = 150  # resetting x to start of the row
            y += SCALE_FACTOR

def main():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE)) # these lines define the window size, caption, and clock constants
    pygame.display.set_caption("Bad Apple!")
    clock = pygame.time.Clock()

    pygame.mixer.init()

    folder_path = "frames" # this is getting every file in the frames folder with the .png ending
    image_files = sorted(
        [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".png")]
    )

    visualizer = Visualizer(screen)
    frames = []

    for image_file in image_files: # loops for every file in the frames directory
        visualizer.reprocessimage(image_file)

    running = True
    current_frame = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if the window is exited, then the program quits the animation
                running = False

        screen.fill(BGCOLOR) # creates the solid background

        if current_frame == 10: # this adds delay to the music so it starts earlier to avoid music de-sync due to cpu lag
            music_file = "badapple.mp3"
            pygame.mixer.music.load(music_file)

            pygame.mixer.music.play()  # start the music

        if frames:
            visualizer.imagepixels = frames[current_frame]
            visualizer.render_frame()

            pygame.display.flip()

            current_frame = (current_frame + 1) % 6572
            print(current_frame)

        clock.tick(FPS)

    pygame.mixer.music.stop()
    pygame.quit()

def dothisifugotabigpc():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE)) # these lines define the window size, caption, and clock constants
    pygame.display.set_caption("Bad Apple! ")
    clock = pygame.time.Clock()

    pygame.mixer.init()
    running = True

    def videogen():
        global running
        CURRENT_FRAME = 0
        folder_path = "frames" # this is getting every file in the frames folder with the .png ending
        image_files = sorted(
            [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".png")]
        )

        visualizer = Visualizer(screen)
        frames = []

        for image_file in image_files: # loops for every file in the frames directory
            visualizer.reprocessimage(image_file)
            print(f"\n processing... \n {len(frames)} / {len(image_files)} frames processed")
            frames.append(visualizer.imagepixels) # this is taking the image pixels that were converted and adding them to the frames list, where large groups of images (pixel lists) will be stored and eventually read
                
            if CURRENT_FRAME == 10: # this adds delay to the music so it starts earlier to avoid music de-sync due to cpu lag
                music_file = "badapple.mp3"
                pygame.mixer.music.load(music_file)

                pygame.mixer.music.play()  # start the music

            if frames:
                visualizer.imagepixels = frames[CURRENT_FRAME]
                visualizer.render_frame()

                pygame.display.flip()

                CURRENT_FRAME = (CURRENT_FRAME + 1)
                print(CURRENT_FRAME)

            clock.tick(FPS)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if the window is exited, then the program quits the animation
                running = False

        videogen()
        screen.fill(BGCOLOR) # creates the solid background that isnt the animation


    pygame.mixer.music.stop()
    pygame.quit()


if __name__ == "__main__":
    if hunkypc == True:
        dothisifugotabigpc()
    else:
        main()