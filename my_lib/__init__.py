from .HTMLChart import HTMLChart
from .DataProcessing import DataProcessing
from .start_app import start_app
from .referentiel import *


data_processing = DataProcessing()
chart = HTMLChart(data_processing)
