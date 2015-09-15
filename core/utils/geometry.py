__author__ = 'Serhii Kashuba kashubasv@gmail.com'



def line_intersection(a, b, c, d):
    """
    Returns point of intersection for two lines AB and CD
    False if no intersection
    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    """

    # y = k_1*x + b_1

    d_x_1 = b.get('x') - a.get('x')
    d_y_1 = b.get('y') - a.get('y')

    d_x_2 = d.get('x') - c.get('x')
    d_y_2 = d.get('y') - c.get('y')

    if d_x_1 != 0:
        k_1 = 1.0 * d_y_1 / d_x_1
        b_1 = a.get('y') - k_1 * a.get('x')
    if d_x_2 != 0:
        k_2 = 1.0 * d_y_2 / d_x_2
        b_2 = c.get('y') - k_2 * c.get('x')

    if d_x_1 == 0 and d_x_2 == 0:
        # two vertical lines
        return False

    elif d_x_1 != 0 and d_x_2 != 0:
        """
        y = k_1*x + b_1
        x = (y - b_2)/k_2

        y = k_1/k_2(y - b_2) + b_1
        y = (b_1 - b_2*k_1/k_2) / (1 - k_1/k_2)

        """
        if k_1 == k_2:
            # parallel
            return False

        if k_2 == 0:
            y = c.get('y')
            x = (y - b_1) / k_1
        else:
            y = (b_1 - b_2 * k_1 / k_2) / (1 - k_1 / k_2)
            x = (y - b_2) / k_2

    elif d_x_1 == 0:
        x = a.get('x')
        y = k_2 * x + b_2

    elif d_x_2 == 0:
        x = c.get('x')
        y = k_1 * x + b_1

    else:
        return False

    return (x, y)
