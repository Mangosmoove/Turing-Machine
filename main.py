import pygame


def divisible_by_2(num):
    return num % 2


def divisible_by_3(num):
    return num % 3


# for drawing circles and using labels for the states
def draw_circle(screen, x, y, radius, color, text, label_text):
    pygame.draw.circle(screen, color, (x, y), radius)
    font = pygame.font.SysFont("comicsansms", 45)
    t = font.render(text, True, (255, 255, 255))
    screen.blit(t, (x - 20, y - 10))
    font = pygame.font.SysFont("comicsansms", 25)
    t = font.render(label_text, True, (255, 255, 255))
    screen.blit(t, (x - 55, y + 50))


def main():
    pygame.init()

    screen_width = 500
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))

    font = pygame.font.SysFont("comicsansms", 30)

    problem = input("Which machine do you want to try?\n1. Divisible by 2\n2. Divisible by 3\nPrompt #: ")
    num = input("Enter a number to check: ")
    storage = num
    if problem == "1":
        state_count = 2
        divisible_by_n = divisible_by_2
    elif problem == "2":
        state_count = 3
        divisible_by_n = divisible_by_3
    else:
        print("Invalid input. Please enter 2 or 3.")
        return

    state = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")
        if state_count == 2:
            draw_circle(screen, 100, 90, 50, (255, 255, 255), "S-0", "Divisible by 2")
            draw_circle(screen, 370, 90, 50, (255, 255, 255), "S-1", "Not Divisible by 2")
        else:
            draw_circle(screen, 100, 90, 50, (255, 255, 255), "S-0", "Remainder 0")
            draw_circle(screen, 370, 90, 50, (255, 255, 255), "S-1", "Remainder 1")
            draw_circle(screen, 235, 150, 50, (255, 255, 255), "S-2", "Remainder 2")

        # using red to identify current state
        if state_count == 2:
            if state == 0:
                draw_circle(screen, 100, 90, 50, (255, 0, 0), "S-0", "Divisible by 2")
            else:
                draw_circle(screen, 370, 90, 50, (255, 0, 0), "S-1", "Not Divisible by 2")
        else:
            if state == 0:
                draw_circle(screen, 100, 90, 50, (255, 0, 0), "S-0", "Remainder 0")
            elif state == 1:
                draw_circle(screen, 370, 90, 50, (255, 0, 0), "S-1", "Remainder 1")
            else:
                draw_circle(screen, 235, 150, 50, (255, 0, 0), "S-2", "Remainder 2")

        # for info visualization
        input_num = font.render(f"Inputted Number: {storage}", True, (255, 255, 255))
        screen.blit(input_num, (120, 250))
        text = font.render(f"Current state: {state}", True, (255, 255, 255))
        screen.blit(text, (120, 275))
        input_text = font.render(f"Current number: {num[0] if num else ''}", True, (255, 255, 255))
        screen.blit(input_text, (120, 300))

        pygame.display.update()

        # allow for state change to be visually processed
        pygame.time.wait(1000)

        # process next input
        if num:
            digit = int(num[0])
            num = num[1:]
            remainder = divisible_by_n(digit)
            if state == 0:
                if remainder == 0:
                    state = 0
                else:
                    state = 1
            elif state == 1:
                if remainder == 0:
                    state = 0
                else:
                    state = 2
            elif state == 2:
                if remainder == 0:
                    state = 1
                else:
                    state = 0
        else:
            # end of string
            font = pygame.font.SysFont("comicsansms", 40)
            text = font.render("Finished Reading Tape!", True, (255, 255, 255))
            screen.blit(text, (100, 350))
            pygame.display.update()
            pygame.time.wait(5000)  # Wait for 2 seconds
            running = False

    pygame.quit()


if __name__ == "__main__":
    main()
