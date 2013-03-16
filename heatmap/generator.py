# coding=utf-8
import Image
from heatmap.colorscheme import ColorScheme
from heatmap.dot import Dot


class HeatMap():
    def __init__(self, size=(256, 256), scheme='classic', dotsize=50, pointgrid_size=1):
        if pointgrid_size < 1 or pointgrid_size >= min(size):
            raise ValueError("pointgrid_size must be >= 1 and <= {0}!".format(min(size)))
        self.size = size
        self.pointgrid_size = pointgrid_size
        self.colors = ColorScheme(scheme).get()
        self.img = Image.new('RGBA', size=size, color=(0, 0, 0, 0))
        self.points = []
        self.dot = Dot(size=dotsize)
        self.dots = {}
        self.dot_offset = float(self.dot.size) / 2

    def add_points(self, points, data_bounds=None):
        if not data_bounds:
            _points = points

            _points = map(
                lambda p: self._snap_to_grid(p),
                _points
            )
        else:
            ((xmin, ymin), (xmax, ymax)) = data_bounds
            rangex, rangey = xmax - xmin, ymax - ymin
            xmod, ymod = float(self.size[0]) / float(rangex), float(self.size[1]) / float(rangey)
            _points = []
            for point in points:
                p = ((point[0] - xmin) * xmod, (point[1] - ymin) * ymod)
                _points.append(self._snap_to_grid(p))
        _points = map(lambda p: (p[0] - self.dot_offset, p[1] - self.dot_offset), _points)
        self._normalize_points(_points)

    def _snap_to_grid(self, point):
        if self.pointgrid_size == 1:
            return point
        s = self.pointgrid_size
        x, y = point
        x = x - x % s + round(x % s / float(s)) * s
        y = y - y % s + round(y % s / float(s)) * s
        return x, y

    def _normalize_points(self, points):
        self.dots = {}
        values = {}
        self.points = []
        max_value = 1
        for point in points:
            x, y = round(point[0]), round(point[1])
            newpoint = (int(x - x % self.pointgrid_size), int(y - y % self.pointgrid_size))

            if not newpoint in self.points:
                self.points.append(newpoint)
                values[newpoint] = 1
            else:
                values[newpoint] += 1
                max_value = max(max_value, values[newpoint])

        for key, value in values.iteritems():
            percent = value * 100.0 / float(max_value)
            self.dots[key] = self.dot.get_image(percent)

    def _colorize(self):
        _computed_opacities = {}
        pix = self.img.load()
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                # Get color for this intensity
                # ============================
                # is a value

                val = self.colors[0, pix[x, y][3]]
                try:
                    pix_alpha = val[3]  # the color image has transparency
                except IndexError:
                    pix_alpha = 255  # it doesn't


                # Blend the opacities
                # ===================

                conf, pixel = 255, pix_alpha
                if (conf, pixel) not in _computed_opacities:
                    opacity = int(( (conf/255.0)    # from configuration
                                    * (pixel/255.0)   # from per-pixel alpha
                                  ) * 255)
                    _computed_opacities[(conf, pixel)] = opacity

                if pix[x, y][3] > 0:
                    pix[x, y] = val[:3] + (_computed_opacities[(conf, pixel)],)

    def generate(self):
        for point, dot in self.dots.iteritems():
            self.img.paste(dot, point, dot)
        self._colorize()

    def save(self, out, outformat=None):
        if outformat is None:
            self.img.save(out)
        else:
            self.img.save(out, outformat)