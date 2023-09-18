import pyray as pr

pr.init_window(800, 450, "Hello")
while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)
    pr.draw_text("Hello world", 360, 215, 20, pr.VIOLET)
    pr.end_drawing()
pr.close_window()