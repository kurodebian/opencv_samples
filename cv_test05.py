import cv2

def main():
    img = cv2.imread( 'apple.jpg', cv2.IMREAD_COLOR )

    out = cv2.cvtColor( img, cv2.COLOR_BGR2HSV )
    cv2.imwrite("gray2.jpg", out)

if __name__ == "__main__":
    main()