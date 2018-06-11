class Figure:
    """Parent class for all figures"""

    def __init__(self, name, line_color):
        self.name = name
        self.line_color = line_color # in hex, e.g. #ff1234

    type_name = 'Figure'  # type: str
    full_desc = type_name + ' - ' + __doc__


class Line(Figure):
    """Given by two points"""

    def __init__(self, name, line_color, coordinates): # coordinates = [{'x': 3, 'y': 4}, {'x': 6, 'y': 7}]
        super().__init__(name, line_color)
        self.line_start = coordinates[0]
        self.line_end = coordinates[1]

    type_name = 'Line'  # type: str


class BrokenLine(Figure):
    """Is defined by points greater than two"""

    # coordinates = [{'x': 3, 'y': 4}, {'x': 6, 'y': 7}, {'x': 9, 'y': 3}]
    def __init__(self, name, line_color, coordinates):
        super().__init__(name, line_color)
        self.coordinates = coordinates
        self.line_start = coordinates[0]
        self.line_end = coordinates[-1]

    type_name = 'Broken Line'  # type: str


class Circle(Figure):
    """Given by the location of the center and the radius"""

    def __init__(self, name, line_color, center, radius_length, fill_color):
        super().__init__(name, line_color)
        self.center = center
        self.radius_length = radius_length
        self.fill_color = fill_color

    type_name = 'Circle'  # type: str


class Rectangle(Figure):
    """Given by two pairs of points that are on the same axis"""

    def __init__(self, name, line_color, four_dots, fill_color):
        super().__init__(name, line_color)
        self.four_dots = four_dots
        self.fill_color = fill_color

    type_name = 'Rectangle'  # type: str


class Registrator:
    """Creating the list of figures"""

    def __init__(self):
        self.figures_list = []

    def register(self, figure):
        self.figures_list.append(figure)

    def show_list(self):
        for figure in self.figures_list:
            print("\n".join(figure.full_desc))


one_line = Line('One awesome Line', '#ff1234', [{'x': 3, 'y': 4}, {'x': 6, 'y': 7}])
broken_line = BrokenLine('One ugly broken Line', '#000000', [{'x': 3, 'y': 4}, {'x': 6, 'y': 7}, {'x': 9, 'y': 3}])
ideal_circle = Circle('Just circle', '#ff00ff', {'x': 3, 'y': 4}, 10, '#00ff00')

registrator_object = Registrator()
registrator_object.register(one_line)
registrator_object.register(broken_line)
registrator_object.register(ideal_circle)
registrator_object.show_list
