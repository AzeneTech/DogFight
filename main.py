from controller.controller import Controller
from model.model import Model
from view.viewtkinter import ViewTkinter

controller = Controller(ViewTkinter(), Model())
controller.start()
