import pygame
import sys
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Flag Challenge - Professional")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 200, 100)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
PURPLE = (150, 50, 200)
BACKGROUND = (20, 25, 45)

# Fonts
title_font = pygame.font.SysFont('arial', 36, bold=True)
question_font = pygame.font.SysFont('arial', 24)
option_font = pygame.font.SysFont('arial', 20)
score_font = pygame.font.SysFont('arial', 28, bold=True)

# Countries data
countries = [
    {"name": "United States", "flag_color": (60, 59, 110)},
    {"name": "China", "flag_color": (238, 28, 37)},
    {"name": "Japan", "flag_color": (188, 0, 45)},
    {"name": "Germany", "flag_color": (0, 0, 0)},
    {"name": "France", "flag_color": (0, 85, 164)},
    {"name": "United Kingdom", "flag_color": (1, 33, 105)},
    {"name": "India", "flag_color": (255, 153, 51)},
    {"name": "Brazil", "flag_color": (0, 156, 59)},
]

def generate_math_question():
    """Generate math questions"""
    operation = random.choice(['+', '-', '*'])
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    
    if operation == '+':
        answer = a + b
        question = f"{a} + {b} = ?"
    elif operation == '-':
        answer = a - b
        question = f"{a} - {b} = ?"
    else:
        answer = a * b
        question = f"{a} × {b} = ?"
    
    wrong_answers = [
        answer + random.randint(1, 10),
        answer - random.randint(1, 10),
        answer + random.randint(-5, 5)
    ]
    
    options = wrong_answers + [answer]
    random.shuffle(options)
    
    return question, answer, options

def draw_button(surface, text, rect, color, hover=False):
    """Draw a button with hover effect"""
    button_color = (min(color[0] + 30, 255), min(color[1] + 30, 255), min(color[2] + 30, 255)) if hover else color
    pygame.draw.rect(surface, button_color, rect, border_radius=10)
    pygame.draw.rect(surface, WHITE, rect, 2, border_radius=10)
    
    text_surf = option_font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)

def main():
    score = 0
    current_country = random.choice(countries)
    current_question, correct_answer, options = generate_math_question()
    selected_option = None
    feedback = None
    feedback_timer = 0
    
    clock = pygame.time.Clock()
    
    # Button rectangles
    option_buttons = [pygame.Rect(200, 350 + i*70, 400, 50) for i in range(4)]
    
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN and feedback is None:
                for i, button in enumerate(option_buttons):
                    if button.collidepoint(mouse_pos):
                        selected_option = i
                        if options[i] == correct_answer:
                            score += 10
                            feedback = "Correct! +10 Points"
                            feedback_timer = 60
                        else:
                            score = max(0, score - 5)
                            feedback = "Wrong! -5 Points"
                            feedback_timer = 60
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and feedback is not None:
                    # Start new round
                    current_country = random.choice(countries)
                    current_question, correct_answer, options = generate_math_question()
                    selected_option = None
                    feedback = None
        
        # Update feedback timer
        if feedback_timer > 0:
            feedback_timer -= 1
            if feedback_timer == 0 and feedback is not None:
                # Auto continue after feedback
                current_country = random.choice(countries)
                current_question, correct_answer, options = generate_math_question()
                selected_option = None
                feedback = None
        
        # Draw everything
        screen.fill(BACKGROUND)
        
        # Draw title
        title_text = title_font.render("Math Flag Challenge", True, YELLOW)
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 20))
        
        # Draw score
        score_text = score_font.render(f"Score: {score}", True, GREEN)
        screen.blit(score_text, (WIDTH - score_text.get_width() - 20, 20))
        
        # Draw flag section
        flag_rect = pygame.Rect(WIDTH//2 - 75, 80, 150, 100)
        pygame.draw.rect(screen, current_country["flag_color"], flag_rect)
        pygame.draw.rect(screen, WHITE, flag_rect, 2)
        
        country_text = question_font.render(current_country["name"], True, WHITE)
        screen.blit(country_text, (WIDTH//2 - country_text.get_width()//2, 190))
        
        # Draw question
        question_text = question_font.render(current_question, True, YELLOW)
        screen.blit(question_text, (WIDTH//2 - question_text.get_width()//2, 250))
        
        # Draw options
        for i, button in enumerate(option_buttons):
            hover = button.collidepoint(mouse_pos) and feedback is None
            color = BLUE if i == selected_option and feedback else PURPLE
            draw_button(screen, str(options[i]), button, color, hover)
        
        # Draw feedback
        if feedback:
            feedback_color = GREEN if "Correct" in feedback else RED
            feedback_text = title_font.render(feedback, True, feedback_color)
            screen.blit(feedback_text, (WIDTH//2 - feedback_text.get_width()//2, 500))
            
            if feedback_timer < 30:  # Blinking text
                continue_text = option_font.render("Press SPACE to continue", True, WHITE)
                screen.blit(continue_text, (WIDTH//2 - continue_text.get_width()//2, 550))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
