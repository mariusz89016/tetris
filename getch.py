class Getch:
    def __call__(self, x=1):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(sys.stdin.fileno())
            ch = sys.stdin.read(x)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
