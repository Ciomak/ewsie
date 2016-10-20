from statistica.models import *

class BarChart():
    pass

class LineChart():
    pass

class HistogramChart():
    pass

class PieChart():
    pass

class BoxChart():
    pass

class Chart():
    def __init__(self, typ):
        if typ == 'bar':
            return BarChart()
        elif typ == 'line':
            return LineChart()
        elif typ == 'hist':
            return HistogramChart()
        elif typ == 'pie':
            return PieChart()
        elif typ == 'box':
            return BoxChart()