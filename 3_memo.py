# 공은 4종류가 있으며, 크기, 속도 등이 다르다.
# 공은 일정 높이에서 포물선을 그리며 떨어지고, 벽이나 바닥에 닿았을 때 튕긴다.

# 공 만들기(4종류)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# 공 크기에 따른 최초 속도
ball_speed_y = [-18, -15, -12, -9] # 올라갈 때 마이너스

# 공들
balls = []
balls.append({
   "pos_x": 50,
   "pos_y": 50,
   "img_idx": 0,
   "to_x": 3,
   "to_y": -6,
   "init_spd_y": ball_speed_y[0]})

# 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을 때 공 이동 위치 변경(튕겨 나오는 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * (-1)
        
        # 세로 위치(스테이지 닿았을 때 튕기고, 속도 감소)
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5
        
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))