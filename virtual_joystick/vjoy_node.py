import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy
from std_msgs.msg import Header
#from PyQt5 import QtGui


class virtualJoystick(Node):

    def __init__(self, ui):
        super().__init__('virtual_joystick')
        self.ui = ui # Qt GUI
        self.joy_publisher_ = self.create_publisher(Joy, 'joy', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('virtual joystick node started')
        
        # define buttons
        self.btn_cross = 0
        self.btn_star = 0
        self.btn_square = 0
        self.btn_triangle = 0
        self.btn_share = 0
        self.btn_ps = 0
        self.btn_options = 0
        self.btn_left_click = 0
        self.btn_right_click = 0
        self.btn_lb = 0
        self.btn_rb = 0
        self.btn_up = 0
        self.btn_down = 0
        self.btn_left = 0
        self.btn_right= 0
        self.btn_touch = 0
        
        # define GUI event handler
        self.ui.btn_cross.pressed.connect(self.button_cross_press_callback)
        self.ui.btn_cross.released.connect(self.button_cross_release_callback)
        self.ui.btn_star.pressed.connect(self.button_star_press_callback)
        self.ui.btn_star.released.connect(self.button_star_release_callback)
        self.ui.btn_square.pressed.connect(self.button_square_press_callback)
        self.ui.btn_square.released.connect(self.button_square_release_callback)
        self.ui.btn_triangle.pressed.connect(self.button_triangle_press_callback)
        self.ui.btn_triangle.released.connect(self.button_triangle_release_callback)
        self.ui.btn_share.pressed.connect(self.button_share_press_callback)
        self.ui.btn_share.released.connect(self.button_share_release_callback)
        self.ui.btn_ps.pressed.connect(self.button_ps_press_callback)
        self.ui.btn_ps.released.connect(self.button_ps_release_callback)
        self.ui.btn_options.pressed.connect(self.button_options_press_callback)
        self.ui.btn_options.released.connect(self.button_options_release_callback)
        self.ui.btn_left_click.pressed.connect(self.button_left_click_press_callback)
        self.ui.btn_left_click.released.connect(self.button_left_click_release_callback)
        self.ui.btn_right_click.pressed.connect(self.button_right_click_press_callback)
        self.ui.btn_right_click.released.connect(self.button_right_click_release_callback)             
        self.ui.btn_up.pressed.connect(self.button_up_press_callback)
        self.ui.btn_up.released.connect(self.button_up_release_callback)
        self.ui.btn_down.pressed.connect(self.button_down_press_callback)
        self.ui.btn_down.released.connect(self.button_down_release_callback)
        self.ui.btn_left.pressed.connect(self.button_left_press_callback)
        self.ui.btn_left.released.connect(self.button_left_release_callback)
        self.ui.btn_right.pressed.connect(self.button_right_press_callback)
        self.ui.btn_right.released.connect(self.button_right_release_callback)
        self.ui.btn_touch.pressed.connect(self.button_touch_press_callback)
        self.ui.btn_touch.released.connect(self.button_touch_release_callback)
        
        
    def timer_callback(self):
        
        if self.ui.btn_lb.isChecked():
            self.btn_lb = 1
        else:
            self.btn_lb = 0
            
        if self.ui.btn_rb.isChecked():
            self.btn_rb = 1
        else:
            self.btn_rb = 0
            
        msg = Joy()
        msg_header = Header()
        msg_header.frame_id = "joy"
        msg_header.stamp = self.get_clock().now().to_msg()
        msg.header = msg_header
        msg.buttons.append(self.btn_cross) # 0 - cross
        msg.buttons.append(self.btn_star) # 1 - star
        msg.buttons.append(self.btn_square) # 2 - square
        msg.buttons.append(self.btn_triangle) # 3 - triangle
        msg.buttons.append(self.btn_share) # 4 - share
        msg.buttons.append(self.btn_ps) # 5 - PS
        msg.buttons.append(self.btn_options) # 6 - options
        msg.buttons.append(self.btn_left_click) # 7 - left click
        msg.buttons.append(self.btn_right_click) # 8 - right click
        msg.buttons.append(self.btn_lb) # 9 - left button LB
        msg.buttons.append(self.btn_rb) # 10 - right button RB
        msg.buttons.append(self.btn_up) # 11 - up
        msg.buttons.append(self.btn_down) # 12 - down
        msg.buttons.append(self.btn_left) # 13 - left
        msg.buttons.append(self.btn_right) # 14 - right
        msg.buttons.append(self.btn_touch) # 15 - touch
        self.joy_publisher_.publish(msg)

    def button_cross_press_callback(self):
        self.btn_cross = 1

    def button_cross_release_callback(self):
        self.btn_cross = 0

    def button_star_press_callback(self):
        self.btn_star = 1

    def button_star_release_callback(self):
        self.btn_star = 0

    def button_square_press_callback(self):
        self.btn_square = 1

    def button_square_release_callback(self):
        self.btn_square = 0        
 
    def button_triangle_press_callback(self):
        self.btn_triangle = 1

    def button_triangle_release_callback(self):
        self.btn_triangle = 0 
        
    def button_share_press_callback(self):
        self.btn_share = 1

    def button_share_release_callback(self):
        self.btn_share = 0 
        
    def button_ps_press_callback(self):
        self.btn_ps = 1

    def button_ps_release_callback(self):
        self.btn_ps = 0 
        
    def button_options_press_callback(self):
        self.btn_options = 1

    def button_options_release_callback(self):
        self.btn_options = 0 
        
    def button_left_click_press_callback(self):
        self.btn_left_click = 1

    def button_left_click_release_callback(self):
        self.btn_left_click = 0 
        
    def button_right_click_press_callback(self):
        self.btn_right_click = 1

    def button_right_click_release_callback(self):
        self.btn_right_click = 0 
        
    def button_up_press_callback(self):
        self.btn_up = 1

    def button_up_release_callback(self):
        self.btn_up = 0 
        
    def button_down_press_callback(self):
        self.btn_down = 1

    def button_down_release_callback(self):
        self.btn_down = 0 
        
    def button_left_press_callback(self):
        self.btn_left = 1

    def button_left_release_callback(self):
        self.btn_left = 0 
        
    def button_right_press_callback(self):
        self.btn_right = 1

    def button_right_release_callback(self):
        self.btn_right = 0         
        
    def button_touch_press_callback(self):
        self.btn_touch = 1

    def button_touch_release_callback(self):
        self.btn_touch = 0         
                                        