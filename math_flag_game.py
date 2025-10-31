import pygame
import sys
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()
mixer.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Flag Challenge - Professional Edition")

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
title_font = pygame.font.SysFont('arial', 48, bold=True)
question_font = pygame.font.SysFont('arial', 36)
option_font = pygame.font.SysFont('arial', 28)
score_font = pygame.font.SysFont('arial', 32, bold=True)
feedback_font = pygame.font.SysFont('arial', 42, bold=True)

# Country flags data (100 countries)
countries = [
    {"name": "United States", "flag_color": (60, 59, 110)},
    {"name": "China", "flag_color": (238, 28, 37)},
    {"name": "Japan", "flag_color": (188, 0, 45)},
    {"name": "Germany", "flag_color": (0, 0, 0)},
    {"name": "France", "flag_color": (0, 85, 164)},
    {"name": "United Kingdom", "flag_color": (1, 33, 105)},
    {"name": "India", "flag_color": (255, 153, 51)},
    {"name": "Brazil", "flag_color": (0, 156, 59)},
    {"name": "Italy", "flag_color": (0, 146, 70)},
    {"name": "Canada", "flag_color": (255, 0, 0)},
    {"name": "Australia", "flag_color": (1, 33, 105)},
    {"name": "Russia", "flag_color": (213, 43, 30)},
    {"name": "South Korea", "flag_color": (0, 71, 160)},
    {"name": "Spain", "flag_color": (241, 191, 0)},
    {"name": "Mexico", "flag_color": (0, 104, 71)},
    {"name": "Indonesia", "flag_color": (255, 0, 0)},
    {"name": "Turkey", "flag_color": (227, 10, 23)},
    {"name": "Netherlands", "flag_color": (174, 28, 40)},
    {"name": "Saudi Arabia", "flag_color": (0, 84, 48)},
    {"name": "Switzerland", "flag_color": (255, 0, 0)},
    {"name": "Argentina", "flag_color": (116, 172, 223)},
    {"name": "Sweden", "flag_color": (0, 106, 167)},
    {"name": "Norway", "flag_color": (239, 43, 45)},
    {"name": "Denmark", "flag_color": (239, 43, 45)},
    {"name": "Finland", "flag_color": (0, 53, 128)},
    {"name": "Poland", "flag_color": (220, 20, 60)},
    {"name": "Ukraine", "flag_color": (0, 87, 184)},
    {"name": "Egypt", "flag_color": (206, 17, 38)},
    {"name": "South Africa", "flag_color": (0, 119, 73)},
    {"name": "Nigeria", "flag_color": (0, 135, 81)},
    {"name": "Kenya", "flag_color": (0, 0, 0)},
    {"name": "Thailand", "flag_color": (237, 28, 36)},
    {"name": "Vietnam", "flag_color": (218, 37, 29)},
    {"name": "Malaysia", "flag_color": (0, 0, 128)},
    {"name": "Singapore", "flag_color": (255, 0, 0)},
    {"name": "Philippines", "flag_color": (0, 56, 168)},
    {"name": "Israel", "flag_color": (0, 56, 184)},
    {"name": "UAE", "flag_color": (0, 0, 0)},
    {"name": "Qatar", "flag_color": (138, 21, 56)},
    {"name": "Iran", "flag_color": (218, 0, 0)},
    {"name": "Pakistan", "flag_color": (0, 64, 26)},
    {"name": "Bangladesh", "flag_color": (0, 106, 78)},
    {"name": "Sri Lanka", "flag_color": (251, 128, 8)},
    {"name": "Nepal", "flag_color": (221, 12, 39)},
    {"name": "Afghanistan", "flag_color": (0, 0, 0)},
    {"name": "Iraq", "flag_color": (206, 17, 38)},
    {"name": "Syria", "flag_color": (206, 17, 38)},
    {"name": "Lebanon", "flag_color": (237, 28, 36)},
    {"name": "Jordan", "flag_color": (0, 0, 0)},
    {"name": "Kuwait", "flag_color": (0, 0, 0)},
    {"name": "Oman", "flag_color": (0, 0, 0)},
    {"name": "Yemen", "flag_color": (255, 255, 255)},
    {"name": "Greece", "flag_color": (13, 94, 175)},
    {"name": "Portugal", "flag_color": (0, 102, 0)},
    {"name": "Ireland", "flag_color": (0, 155, 72)},
    {"name": "Austria", "flag_color": (237, 41, 57)},
    {"name": "Belgium", "flag_color": (237, 41, 57)},
    {"name": "Czech Republic", "flag_color": (215, 20, 26)},
    {"name": "Hungary", "flag_color": (205, 42, 62)},
    {"name": "Romania", "flag_color": (0, 43, 127)},
    {"name": "Bulgaria", "flag_color": (0, 150, 110)},
    {"name": "Serbia", "flag_color": (198, 54, 60)},
    {"name": "Croatia", "flag_color": (255, 0, 0)},
    {"name": "Slovakia", "flag_color": (0, 56, 147)},
    {"name": "Slovenia", "flag_color": (0, 92, 185)},
    {"name": "Lithuania", "flag_color": (253, 185, 19)},
    {"name": "Latvia", "flag_color": (158, 48, 57)},
    {"name": "Estonia", "flag_color": (0, 114, 206)},
    {"name": "Belarus", "flag_color": (255, 0, 0)},
    {"name": "Georgia", "flag_color": (255, 0, 0)},
    {"name": "Azerbaijan", "flag_color": (0, 0, 0)},
    {"name": "Armenia", "flag_color": (217, 0, 18)},
    {"name": "Kazakhstan", "flag_color": (0, 166, 80)},
    {"name": "Uzbekistan", "flag_color": (0, 153, 76)},
    {"name": "Turkmenistan", "flag_color": (0, 0, 0)},
    {"name": "Tajikistan", "flag_color": (255, 0, 0)},
    {"name": "Kyrgyzstan", "flag_color": (255, 0, 0)},
    {"name": "Mongolia", "flag_color": (196, 31, 58)},
    {"name": "North Korea", "flag_color": (0, 45, 98)},
    {"name": "Taiwan", "flag_color": (0, 0, 149)},
    {"name": "Hong Kong", "flag_color": (255, 0, 0)},
    {"name": "Macau", "flag_color": (255, 0, 0)},
    {"name": "Cambodia", "flag_color": (224, 0, 37)},
    {"name": "Laos", "flag_color": (224, 0, 37)},
    {"name": "Myanmar", "flag_color": (254, 203, 0)},
    {"name": "Bhutan", "flag_color": (255, 153, 0)},
    {"name": "Maldives", "flag_color": (220, 20, 60)},
    {"name": "Brunei", "flag_color": (255, 209, 0)},
    {"name": "Timor-Leste", "flag_color": (255, 0, 0)},
    {"name": "Papua New Guinea", "flag_color": (0, 0, 0)},
    {"name": "Fiji", "flag_color": (200, 16, 46)},
    {"name": "Solomon Islands", "flag_color": (0, 71, 171)},
    {"name": "Vanuatu", "flag_color": (200, 16, 46)},
    {"name": "Samoa", "flag_color": (255, 0, 0)},
    {"name": "Tonga", "flag_color": (193, 39, 45)},
    {"name": "Kiribati", "flag_color": (0, 0, 0)},
    {"name": "Micronesia", "flag_color": (0, 56, 147)},
    {"name": "Palau", "flag_color": (0, 0, 128)},
    {"name": "Marshall Islands", "flag_color": (0, 56, 147)},
    {"name": "Nauru", "flag_color": (0, 56, 147)},
    {"name": "Tuvalu", "flag_color": (0, 56, 147)}
]

# Game variables
score = 0
current_country = None
current_question = None
options = []
selected_option = None
feedback = None
feedback_timer = 0
particles = []

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(3, 8)
        self.speed_x = random.uniform(-3, 3)
        self.speed_y = random.uniform(-3, 3)
        self.life = 30
        
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.life -= 1
        self.size *= 0.95
        
    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

def generate_math_question():
    """Generate professional math questions with different types"""
    question_types = [
        "algebra", "trigonometry", "calculus", "geometry", "arithmetic"
    ]
    
    q_type = random.choice(question_types)
    
    if q_type == "algebra":
        a, b = random.randint(2, 15), random.randint(2, 15)
        c = random.randint(1, 10)
        question = f"Solve: {a}x + {b} = {a*c + b}"
        answer = c
        wrong_answers = [c + random.randint(1, 5), c - random.randint(1, 5), c * 2]
        
    elif q_type == "trigonometry":
        angles = [0, 30, 45, 60, 90]
        angle = random.choice(angles)
        func = random.choice(["sin", "cos", "tan"])
        
        if func == "sin":
            answer = round(math.sin(math.radians(angle)), 2)
            question = f"sin({angle}°) = ?"
        elif func == "cos":
            answer = round(math.cos(math.radians(angle)), 2)
            question = f"cos({angle}°) = ?"
        else:
            answer = round(math.tan(math.radians(angle)), 2)
            question = f"tan({angle}°) = ?"
            
        wrong_answers = [round(random.uniform(0, 1), 2) for _ in range(3)]
        
    elif q_type == "calculus":
        a, b = random.randint(1, 5), random.randint(1, 5)
        question = f"d/dx({a}x² + {b}x) at x=2 = ?"
        answer = 4*a + b
        wrong_answers = [answer + random.randint(1, 10), answer - random.randint(1, 10), answer * 2]
        
    elif q_type == "geometry":
        shapes = ["circle", "triangle", "rectangle"]
        shape = random.choice(shapes)
        
        if shape == "circle":
            r = random.randint(2, 10)
            question = f"Area of circle with r={r} (π=3.14) = ?"
            answer = round(3.14 * r * r, 2)
            wrong_answers = [round(3.14 * r * random.randint(1, 3), 2) for _ in range(3)]
            
        elif shape == "triangle":
            b, h = random.randint(3, 12), random.randint(3, 12)
            question = f"Area of triangle (b={b}, h={h}) = ?"
            answer = 0.5 * b * h
            wrong_answers = [b * h, b + h, (b + h) * 2]
            
        else:  # rectangle
            l, w = random.randint(3, 12), random.randint(3, 12)
            question = f"Area of rectangle ({l}×{w}) = ?"
            answer = l * w
            wrong_answers = [l + w, 2*(l + w), l * w + random.randint(1, 10)]
            
    else:  # arithmetic
        ops = ["+", "-", "*", "/"]
        op = random.choice(ops)
        if op == "+":
            a, b = random.randint(100, 500), random.randint(100, 500)
            answer = a + b
        elif op == "-":
            a, b = random.randint(500, 1000), random.randint(100, 500)
            answer = a - b
        elif op == "*":
            a, b = random.randint(10, 30), random.randint(2, 10)
            answer = a * b
        else:  # division
            b = random.randint(2, 10)
            a = b * random.randint(5, 20)
            answer = a // b
            
        question = f"{a} {op} {b} = ?"
        wrong_answers = [answer + random.randint(1, 20), answer - random.randint(1, 20), answer * 2]
    
    # Ensure wrong answers are different from correct answer
    wrong_answers = list(set([x for x in wrong_answers if x != answer]))[:3]
    while len(wrong_answers) < 3:
        new_wrong = answer + random.choice([-1, 1]) * random.randint(5, 20)
        if new_wrong != answer and new_wrong not in wrong_answers:
            wrong_answers.append(new_wrong)
    
    return question, answer, wrong_answers

def new_round():
    global current_country, current_question, options, selected_option, feedback
    current_country = random.choice(countries)
    current_question, correct_answer, wrong_answers = generate_math_question()
    
    # Mix correct and wrong answers
    options = wrong_answers + [correct_answer]
    random.shuffle(options)
    
    selected_option = None
    feedback = None

def draw_flag(color):
    """Draw a simple flag representation"""
    flag_rect = pygame.Rect(WIDTH//2 - 100, 150, 200, 120)
    pygame.draw.rect(screen, color, flag_rect)
    pygame.draw.rect(screen, WHITE, flag_rect, 3)

def draw_button(text, rect, color, hover=False):
    """Draw a button with hover effect"""
    button_color = (min(color[0] + 30, 255), min(color[1] + 30, 255), min(color[2] + 30, 255)) if hover else color
    pygame.draw.rect(screen, button_color, rect, border_radius=15)
    pygame.draw.rect(screen, WHITE, rect, 3, border_radius=15)
    
    text_surf = option_font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

def create_particles(x, y, color, count=20):
    for _ in range(count):
        particles.append(Particle(x, y, color))

def draw_particles():
    for particle in particles[:]:
        particle.update()
        particle.draw()
        if particle.life <= 0:
            particles.remove(particle)

def main():
    global score, selected_option, feedback, feedback_timer, particles
    
    clock = pygame.time.Clock()
    new_round()
    
    # Button rectangles
    option_buttons = [
        pygame.Rect(WIDTH//2 - 200, 400 + i*80, 400, 60) for i in range(4)
    ]
    
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
                        if options[i] == current_question[1]:  # Correct answer
                            score += 10
                            feedback = "Correct! +10 Points"
                            feedback_timer = 60
                            create_particles(WIDTH//2, 300, GREEN, 30)
                            # Play success sound (you can add sound files)
                        else:
                            score = max(0, score - 5)
                            feedback = "Wrong! -5 Points"
                            feedback_timer = 60
                            create_particles(WIDTH//2, 300, RED, 30)
                            # Play error sound
                        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and feedback is not None:
                    new_round()
        
        # Update
        if feedback_timer > 0:
            feedback_timer -= 1
            if feedback_timer == 0:
                new_round()
        
        # Draw
        screen.fill(BACKGROUND)
        
        # Draw stars in background
        for i in range(50):
            x = (i * 73) % WIDTH
            y = (i * 37) % HEIGHT
            size = 1 + (i % 3)
            pygame.draw.circle(screen, WHITE, (x, y), size)
        
        # Draw title
        title_text = title_font.render("Math Flag Challenge", True, YELLOW)
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 30))
        
        # Draw score
        score_text = score_font.render(f"Score: {score}", True, GREEN)
        screen.blit(score_text, (WIDTH - score_text.get_width() - 20, 20))
        
        # Draw flag section
        pygame.draw.rect(screen, (40, 45, 65), (WIDTH//2 - 150, 120, 300, 170), border_radius=20)
        flag_title = question_font.render("Which country's flag?", True, WHITE)
        screen.blit(flag_title, (WIDTH//2 - flag_title.get_width()//2, 90))
        
        if current_country:
            draw_flag(current_country["flag_color"])
            country_text = question_font.render(current_country["name"], True, WHITE)
            screen.blit(country_text, (WIDTH//2 - country_text.get_width()//2, 290))
        
        # Draw math question
        math_bg = pygame.Rect(WIDTH//2 - 300, 320, 600, 70)
        pygame.draw.rect(screen, (50, 55, 85), math_bg, border_radius=15)
        question_text = question_font.render(current_question[0], True, YELLOW)
        screen.blit(question_text, (WIDTH//2 - question_text.get_width()//2, 340))
        
        # Draw options
        for i, button in enumerate(option_buttons):
            hover = button.collidepoint(mouse_pos) and feedback is None
            color = BLUE if i == selected_option and feedback else PURPLE
            draw_button(str(options[i]), button, color, hover)
        
        # Draw feedback
        if feedback:
            feedback_color = GREEN if "Correct" in feedback else RED
            feedback_text = feedback_font.render(feedback, True, feedback_color)
            screen.blit(feedback_text, (WIDTH//2 - feedback_text.get_width()//2, 550))
            
            continue_text = option_font.render("Press SPACE to continue", True, WHITE)
            screen.blit(continue_text, (WIDTH//2 - continue_text.get_width()//2, 600))
        
        # Draw particles
        draw_particles()
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
