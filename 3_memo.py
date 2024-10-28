# 공은 4종류가 있으며, 크기, 속도 등이 다르다.
# 공은 일정 높이에서 포물선을 그리며 떨어지고, 벽이나 바닥에 닿았을 때 튕긴다.

ball0 = {"img": pygame.image.load(os.path.join(image_path, "ball0.png")),
         "pos_x": 50, 
         "pos_y": 50, 
         "to_x": 3,
         "to_y": -6,
         "init_spd": -18}

balls = [ball0]

for ball_idx, ball in enumerate(balls):
    ball_img = ball["img"]
    ball_size = ball_img.get_rect().size
    ball_width = ball_size[0]
    ball_height = ball_size[1]
    ball_pos_x = ball["pos_x"]
    ball_pos_y = ball["pos_y"]
    ball_to_x = ball["to_x"]
    ball_to_y = ball["to_y"]
    ball_init_spd = ball["init_spd"]

    # 벽에 닿았을 때 튕김
    if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
        ball_to_x *= -1
    
    # 바닥에 닿았을 때 튕기고, 속도 감소
    if ball_pos_y >= screen_height - stage_height - ball_height:
        ball_to_y = ball_init_spd
    else:
        ball_to_y += 0.5
    
    ball_pos_x += ball_to_x
    ball_pos_y += ball_to_y

    # 그리기
    screen.blit(ball_img, (ball_pos_x, ball_pos_y))