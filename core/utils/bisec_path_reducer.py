__author__ = 'Serhii Kashuba kashubasv@gmail.com'

from core.utils.path_reducer import PathReducer

class BisecPathReducer(PathReducer):

    def move_in_range(self, a, b, c, r):
        min_d = a.planar_distance_to(b)
        #print  min_d

        max_d = a.planar_distance_to(c) + c.planar_distance_to(b)
        #print max_d
        best_position = c


        a_direction = c.azimuth(a)
        b_direction = c.azimuth(b)

        if b_direction < a_direction:
            b_direction, a_direction = a_direction, b_direction

        optimal_line_direction = 1.0 *(a_direction + b_direction) / 2

        if b_direction - a_direction > 180:
            optimal_line_direction += 180

        optimal_line_direction = math.floor(optimal_line_direction) % 360





        angles = range(0, 360)
        for angle in angles:
            rad = 1.0 * angle/180 * math.pi
            d_x = math.sin(rad) * r
            d_y = math.cos(rad) * r

            candidate = c.clone()

            candidate.move(d_x, d_y)
            dist = a.planar_distance_to(candidate) + candidate.planar_distance_to(b)
            #print dist, candidate.get_position()

            if dist < max_d:
                max_d = dist
                best_position = candidate

        print a.get_position(), b.get_position(), c.get_position()






        #print c.azimuth(b)
        print c.azimuth(best_position), optimal_line_direction
        print '='*20
        return best_position