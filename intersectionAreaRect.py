from .isCollisionRect import isCollisionRect
class ValueError(Exception):
    pass
def intersectionAreaRect(list1,list2):
    rectangle_1,rectangle_2=list1,list2
    if not isCollisionRect(rectangle_1):
        raise ValueError("1й прямоугольник некорректный")
    if not isCollisionRect(rectangle_2):
        raise ValueError("2й прямоугольник некорректный")
    else:
        
        (x1, y1), (x2, y2) = rectangle_1
        (x3, y3), (x4, y4) = rectangle_2

        if (
            (x1> x4)
            or (y1 > y4)
            or (x2 < x3)
            or (y2 < y3)
        ):
            return "Площадь равна 0"

        xCross_left = max(x1, x3)
        yCross_bottom = max(y1, y3)
        xCross_right = min(x2, x4)
        yCross_top = min(y2, y4)

        crossWidth = xCross_right - xCross_left
        crossHeight = yCross_top - yCross_bottom

        square = crossWidth * crossHeight

        return f"Площадь равна {square}"
