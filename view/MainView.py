import streamlit as st
import pickle
import streamlit_authenticator as stauth
from pathlib import Path

from streamlit_option_menu import option_menu
from controller.ControladorSecretaria import Control_Secretaria
from controller.ControladorDirectorProg import Control_Director_Prog
from controller.ControladorDirectorPos import Control_Director_Pos


class MainView:

    # Constructor
    def __init__(self, controlador, name) -> None:
        super().__init__()

        # Estrategia para manejar el "estado" del controlador y del modelo entre cada cambio de ventana
        if 'main_view' not in st.session_state:
            self.menu_actual = "Inicio"
            # Conexión con el controlador
            self.controller = controlador

            st.session_state['main_view'] = self
        else:
            # Al existir en la sesión entonces se actualizan los valores
            self.menu_actual = st.session_state.main_view.menu_actual
            self.controller = st.session_state.main_view.controller

        self._dibujar_layout(name)

    def _dibujar_layout(self, name):

        # Definimos lo que abra en la barra de menu
        if name == "Secretaria":
            with st.sidebar:
                st.image("img/logoPUJCali.jpg", width=200, use_column_width=True)
                self.menu_actual = option_menu("Menu", ["Inicio", "Agregar aspirante",
                                                        "Ver aspirantes", "Agregar entrevista",
                                                        "Ver entrevistas", "Modificar información de aspirantes",
                                                        "Generar Carta de Admisión/No Admisión",
                                                        "Agregar Concepto de entrevista",
                                                        "Modificar información carta de admisión", "Estadísticas"])
        elif name == "Director_Pos":
            with st.sidebar:
                st.image("img/logoPUJCali.jpg", width=200, use_column_width=True)
                self.menu_actual = option_menu("Menu", ["Inicio", "Agregar aspirante",
                                                        "Ver aspirantes", "Agregar entrevista",
                                                        "Ver entrevistas", "Modificar información de aspirantes",
                                                        "Generar Carta de Admisión/No Admisión",
                                                        "Agregar Concepto de entrevista",
                                                        "Modificar firma y firmante", "Estadísticas"])
        elif name == "Director_Prog":
            with st.sidebar:
                st.image("img/logoPUJCali.jpg", width=200, use_column_width=True)
                self.menu_actual = option_menu("Menu", ["Inicio", "Agregar aspirante",
                                                        "Ver aspirantes", "Agregar entrevista",
                                                        "Ver entrevistas", "Modificar información de aspirantes",
                                                        "Generar Carta de Admisión/No Admisión",
                                                        "Agregar Concepto de entrevista",
                                                        "Descargar información de aspirantes",
                                                        "Modificar firma y firmante",
                                                        "Modificar información carta de admisión", "Estadísticas"])

    def mostrar_inicio(self):
        return """
            ## Bienvenid@ a nuestro proyecto de gestión de admisiones\n
            ### El proyecto fue elaborado por:
            * Juan Esteban Becerra Gutiérrez
            *  * juanesbecerra04@javerianacali.edu.co
            * Alejandro Sarmiento
            *  * alesansarive@javerianacali.edu.co
            """


    def controlar_menu(self):
        if self.menu_actual == "Inicio":
            # Se llama con self pq en metodo de la clase MainView
            st.write(self.mostrar_inicio())
        elif self.menu_actual == "Agregar aspirante":
            # Llama al metodo para agregar aspirantes
            self.controller.view_agregar_aspirante(st)
        elif self.menu_actual == "Ver aspirantes":

            self.controller.mostrar_aspirantes(st)
        elif self.menu_actual == "Agregar entrevista":

            self.controller.crear_entrevista(st)
        elif self.menu_actual == "Ver entrevistas":

            self.controller.mostrar_entrevistas(st)
        elif self.menu_actual == "Modificar información de aspirantes":

            if len(self.controller.entrevistas) != 0:
                self.controller.editar_info_aspirantes(st)
            else:
                st.info("No hay aspirantes registrados con entrevistas")
        elif self.menu_actual == "Generar Carta de Admisión/No Admisión":
            if len(self.controller.entrevistas) != 0:
                self.controller.generar_carta(st)
            else:
                st.info("No hay aspirantes registrados con entrevistas")
        elif self.menu_actual == "Agregar Concepto de entrevista":
            if len(self.controller.entrevistas) != 0:
                self.controller.generar_concepto_entrevista(st)
            else:
                st.info("No hay aspirantes registrados con entrevistas")
        elif self.menu_actual == "Modificar información carta de admisión":
            self.controller.view_modificar_carta(st)
        elif self.menu_actual == "Modificar firma y firmante":
            self.controller.cambiar_firma_firmante(st)
        elif self.menu_actual == "Descargar información de aspirantes":

            self.controller.generar_excel(st)
        elif self.menu_actual == "Estadísticas":
            self.controller.estadisticas(st)


# Main call
def ingreso_usuario():
    # Autenticación del usuario
    st.set_page_config(page_title="Gestionador de admisiones", page_icon=':)', layout="wide",
                       initial_sidebar_state="expanded")
    names = ["Secretaria", "Director_Pos", "Director_Prog"]
    usernames = ["Secretaria", "Director_Pos", "Director_Prog"]

    # Recoge las contraseñas y los usuarios del archivo pkl
    file_path = Path(__file__).parent / "../authentication/hashed_pw.pkl"
    with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)

    # Revisa si se ingresaron las credenciales. Es decir, que automatiza el sistema de seleccion de entrada
    authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "proyecto", "abcedf", cookie_expiry_days=30)
    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status:
        # Se selecciona cual usuario va entrar
        st.title(f"Bienvenid@    {name}")
        if name == "Secretaria":
            controlador = Control_Secretaria()
        elif name == "Director_Pos":
            controlador = Control_Director_Pos()
        elif name == "Director_Prog":
            controlador = Control_Director_Prog()
        authenticator.logout("Salir", "sidebar")
        gui = MainView(controlador, name)
        gui.controlar_menu()
    elif authentication_status is None:
        st.warning("Porfavor ingrese su usuario y/o contraseña")
    elif not authentication_status:
        st.error("Usuario y/o contraseña erroneos")

if __name__ == "__main__":
    ingreso_usuario()
