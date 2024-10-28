import pygame
import os

####################################################################
# 기본 초기화 과정: 반드시 필요
pygame.init() 

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("팡")

# FPS(Frame Per Second)
clock = pygame.time.Clock()
####################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기(히트박스 필요)
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이

# 캐릭터 만들기(히트박스, 위치변수, 이동방향, 이동속도 필요)
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0] # 캐릭터 가로 사이즈
character_height = character_size[1] # 캐릭터 세로 사이즈
character_x_pos = (screen_width / 2) - (character_width / 2) # 캐릭터 가로 위치
character_y_pos = screen_height - character_height - stage_height # 캐릭터 세로 위치
character_to_x = 0 # 캐릭터 이동 방향
character_speed = 5 # 캐릭터 이동 속도

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0] # 무기 가로 사이즈

weapons = [] # 무기는 한 번에 여러발 발사 가능
weapon_speed = 10



# 게임 루프
running = True
while running:
    dt = clock.tick(60)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 캐릭터 좌측이동
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터 우측이동
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # 무기 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2) # 캐릭터 중간에서 발사
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
        
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 무기 위치 조정
    # 예: (100,200) -> (100,200-v) -> (100,200-2v) -> ...
    # 가로 좌표(0) 그대로, 세로 좌표(1)는 위로
    weapons = [ [weapon[0], weapon[1] - weapon_speed] for weapon in weapons]
    # 천장에 닿은 무기는 사라지도록 만들기(세로 좌표가 0보다 큰 것만 리스트에 담는다)
    weapons = [ [weapon[0], weapon[1]] for weapon in weapons if weapon[1] > 0]

    # 4. 충돌 처리

    # 5. 화면에 그리기(배경, 무기, 스테이지, 캐릭터 순서로 덮는다)
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()