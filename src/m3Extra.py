def find_object_counterclockwise():

        pixy = ev3.Sensor(driver_name="pixy-lego")
        pixy.mode = "SIG1"
        X = pixy.value(1)  # X, int value 0 to 319 (320 pixels wide)
        Y = pixy.value(2)  # Y, int value 0 to 199 (200 pixels wide)
        W = pixy.value(3)  # Width, int value 0 to 320
        H = pixy.value(4)  # Height, int value 0 to 200
        Object = (X, Y, W, H)
        if X < 0:
            self.spin_counterclockwise_until_sees_object(speed, area)
            print(Object)