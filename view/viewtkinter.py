from tkinter import Tk, messagebox, Canvas, Event, NW, PhotoImage, E, W

from model.plane import Plane
from model.population import Population
from shared.action import Action
from shared.icontroller import IController
from shared.imodel import IModel
from shared.iview import IView
from model.cloud import Cloud

import json

class ViewTkinter(IView):
    __model: IModel
    __controller: IController
    __window: Tk
    __canvas: Canvas
    __population: Population
    __planes: [Plane]
    __plane1Image: int
    __plane2Image: int
    __plane1PhotoImage: PhotoImage
    __plane2PhotoImage: PhotoImage
    __missilePhotoImage: PhotoImage
    __missileImage: int = None
    __missileImage2: int = None
    __cloudPhotoImage: PhotoImage
    __cloudImage1: int = None
    __cloudImage2: int = None
    __cloudImage3: int = None
    __population: Population
    # __planeImage: PhotoImage

    def __init__(self):
        self.__window = None
        self.__Population = None
        # self.__planeImage = None

    def __createWindow(self, planes: [Plane]):

        self.__window = Tk()
        self.__window.title(self.__model.getFromKey("title"))
        self.__window.geometry(str(self.__model.getFromKey("width") * int(self.__model.getFromKey("zoom")))
                               + "x"
                               + str(self.__model.getFromKey("height") * int(self.__model.getFromKey("zoom"))))
        self.__canvas = Canvas(self.__window, bg=self.__model.getFromKey("background"))
        self.__canvas.pack(fill="both", expand=True)
        self.__window.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.__window.bind("<Key>", self.__manageKeyboard)
        self.__missilePhotoImage = PhotoImage(file="model/image/missile1.png")
        self.__missilePhotoImage2 = PhotoImage(file="model/image/missile2.png")
        self.__cloudPhotoImage = PhotoImage(file="model/image/cloud.png")

        self.__plane1PhotoImage = PhotoImage(file=planes[0].getSprite().getImage())
        # self.__plane1Canvas = Canvas(self.__canvas, width=100, height=100, bg="purple")
        self.__plane1Image = self.__canvas.create_image(planes[0].getX(), planes[0].getY(),
                                                        image=self.__plane1PhotoImage,
                                                        anchor=W)


        self.__plane2PhotoImage = PhotoImage(file=planes[1].getSprite().getImage())
        self.__plane2Image = self.__canvas.create_image(planes[1].getX(), planes[1].getY(),
                                                        image=self.__plane2PhotoImage,
                                                        anchor=E)

    def __onClosing(self):
        self.__controller.performAction(Action.CLOSE)

    def display(self, message) -> None:
        messagebox.showinfo(self.__model.getFromKey("title"), message)

    def setModel(self, model: IModel):
        self.__model = model

    def askYesNo(self, message: str) -> bool:
        return messagebox.askyesno(self.__model.getFromKey("title"), message)

    def setController(self, controller) -> None:
        self.__controller = controller

    def showGame(self, population: Population = None) -> None:
        with open("data/data.json") as jsonfile:
            __data = json.load(jsonfile)

        self.__population = population
        planes = self.__population.getPlane()
        missiles = self.__population.getMissile()
        clouds = self.__population.getCloud()

        if len(self.__population.getPlane()) == 1:
            self.gameOver()
            self.__controller.performAction(Action.PAUSE)
            return None

        if self.__window is None:
            self.__createWindow(planes)
            zoom = self.__model.getFromKey("zoom")

        # print(f'{planes[0].getSprite().getImage()} {planes[0].getX()} {planes[0].getY()} {planes[0].getAngle()}')
        self.__canvas.coords(self.__plane1Image, planes[0].getX(), planes[0].getY())
        self.__plane1PhotoImage = PhotoImage(file=planes[0].getSprite().getImage())
        self.__canvas.itemconfig(self.__plane1Image, image=self.__plane1PhotoImage)
        self.__canvas.coords(self.__plane2Image, planes[1].getX(), planes[1].getY())
        self.__plane2PhotoImage = PhotoImage(file=planes[1].getSprite().getImage())
        self.__canvas.itemconfig(self.__plane2Image, image=self.__plane2PhotoImage)

        if self.__cloudImage1 == None:

            self.__cloudImage1 = self.__canvas.create_image(clouds[0].getX(), clouds[1].getY(),
                                                            image=self.__cloudPhotoImage,
                                                            anchor=E)
            self.__cloudImage2 = self.__canvas.create_image(clouds[1].getX(), clouds[1].getY(),
                                                          image=self.__cloudPhotoImage,
                                                          anchor=E)
            self.__cloudImage3 = self.__canvas.create_image(clouds[2].getX(), clouds[1].getY(),
                                                          image=self.__cloudPhotoImage,
                                                          anchor=E)

        for cloud in clouds:
            if cloud.getX() < 10:
                cloud.randomizeY()
            print(cloud.getX())

        self.__canvas.coords(self.__cloudImage1, clouds[0].getX(), clouds[0].getY())
        self.__canvas.coords(self.__cloudImage2, clouds[1].getX(), clouds[1].getY())
        self.__canvas.coords(self.__cloudImage3, clouds[2].getX(), clouds[2].getY())

        # Création des missiles
        if missiles != []:

            for missile in missiles:
                print(missile.getDistanceFlew())

                #On regarde pour chaque missile à quel avion il est lié
                i = 0
                for plane in planes:
                    if missile in plane.getMissile():

                        #Si c'est le bon on regarde si l'a déja son sprite ou pas
                        #Ici le i correspond à l'index de l'avion
                        if i == 0:
                            if self.__missileImage != None:
                                #Set l'emplacement du missile
                                self.__canvas.coords(self.__missileImage, missile.getX(), missile.getY())
                                self.__canvas.itemconfig(self.__missileImage, image=self.__missilePhotoImage)
                                #Gère la distance que le missile parcours
                                __axis = "height"
                                #On change axis en fonction de l'axe principale de la direction du missile
                                if 45 >= missile.getAngle() >= -45:
                                    __axis = "width"

                                #Puis on regarde sa distance parcouru avec la taille de l'écran selon en x ou y
                                if missile.getDistanceFlew() >= 2 * __data[__axis]:
                                    #Puis on le détruit
                                    self.__population.delMobile(missile)
                                    self.__canvas.delete(self.__missileImage)
                                    self.__missileImage = None
                                    missile.explode()
                                    plane.delMissile(missile)

                            else:
                                #S'il n'est pas créé on cette ligne s'en occupe
                                self.__missilePhotoImage = PhotoImage(file="model/image/missile1.png")
                                self.__missileImage = self.__canvas.create_image(missile.getX(), missile.getY(),
                                                                            image=self.__missilePhotoImage,
                                                                            anchor=W)
                                self.__canvas.itemconfig(self.__missileImage, image=self.__missilePhotoImage)

                        else:
                            #Même principe qu'au dessus mais pour le second missile
                            if self.__missileImage2 != None:
                                self.__canvas.coords(self.__missileImage2, missile.getX(), missile.getY())
                                self.__canvas.itemconfig(self.__missileImage2, image=self.__missilePhotoImage2)

                                __axis = "height"
                                if 45 >= missile.getAngle() >= -45:
                                    __axis = "width"

                                if missile.getDistanceFlew() >= 2 * __data[__axis]:
                                    self.__population.delMobile(missile)
                                    self.__canvas.delete(self.__missileImage2)
                                    self.__missileImage2 = None
                                    missile.explode()
                                    plane.delMissile(missile)

                            else:
                                self.__missilePhotoImage2 = PhotoImage(file="model/image/missile2.png")
                                self.__missileImage2 = self.__canvas.create_image(missile.getX(), missile.getY(),
                                                                                 image=self.__missilePhotoImage2,
                                                                                 anchor=E)
                                self.__canvas.itemconfig(self.__missileImage2, image=self.__missilePhotoImage2)
                    i += 1 #On incrément i pour indiquer qu'on passe à l'avion d'après
            for plane in planes:
                # Récupérez les coordonnées de la hitbox de l'avion

                plane_hitbox = missile.getHitbox()
                for missile in missiles:
                    # Récupérez les coordonnées du missile
                    missile_coords = (plane.getX(), plane.getY())

                    # Vérifiez si le missile est à l'intérieur de la hitbox de l'avion
                    if plane.isOpposite() == -1:
                        if (
                                abs(missile.getX() - plane.getX()) < __data["planeSizeX"] and abs(missile.getY() - plane.getY()) < __data["planeSizeY"]
                        ):

                            population.delMobile(plane)
                    else:
                        if (
                                abs(missile.getX() - plane.getX()) < __data["planeSizeX"] and abs(
                            missile.getY() - plane.getY()) < __data["planeSizeY"]
                        ):

                            population.delMobile(plane)


                    # elif(
                    #         missile.getHitbox()[0] < missile_coords[0] < missile.getHitbox()[2] and
                    #         plane_hitbox[1] < missile_coords[1] < plane_hitbox[3]
                    # ):

        self.__window.update()


    def __manageKeyboard(self, event: Event):
        # Fichiers Window, plane1 et plane2 ? Séparer le fichier Data en 3 en gros
        if event.keysym == self.__model.getFromKey("keyPause"):
            self.__controller.performAction(Action.PAUSE)
        elif event.keysym == self.__model.getFromKey("plane1Right"):
            self.__population.getPlane(0).rotate(self.__model.getFromKey("rotateSpeed"))
        elif event.keysym == self.__model.getFromKey("plane1Left"):
            self.__population.getPlane(0).rotate(- self.__model.getFromKey("rotateSpeed"))
        elif event.keysym == self.__model.getFromKey("plane1Shoot"):
            if self.__population.getPlane(0).getMissile() == []:
                self.__controller.performAction(Action.FIRE)

        elif event.keysym == self.__model.getFromKey("plane2Right"):
            self.__population.getPlane(1).rotate(self.__model.getFromKey("rotateSpeed"))
        elif event.keysym == self.__model.getFromKey("plane2Left"):
            self.__population.getPlane(1).rotate(- self.__model.getFromKey("rotateSpeed"))
        elif event.keysym == self.__model.getFromKey("plane2Shoot"):
            if self.__population.getPlane(1).getMissile() == []:
                self.__controller.performAction(Action.FIRE2)


    def gameOver(self):
        if self.askYesNo(
                f'GG {self.__population.getPlane(0).getSprite().getImage().split("/")[-1].split(".")[0]} !\nVoulez-vous rejouer ?'):
            self.__controller.performAction(Action.RESTART)
        else:
            self.__controller.performAction(Action.CLOSE)