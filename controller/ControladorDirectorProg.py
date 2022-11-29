from abc import ABC

from controller.Controlador import Controlador
from controller.ControladorExcel import Controlador_excel
from datetime import datetime


class Control_Director_Prog(Controlador, ABC):
    def __init__(self) -> None:
        Controlador.__init__(self)

    def view_modificar_carta(self, st):
        st.title("Modificar información de la carta")
        # Se modifica la información de la carta
        fecha = st.date_input('Digite la nueva fecha de reunión aquí')
        hora = st.time_input('Digite la nueva hora de reunión aquí')

        ubicacion = st.text_input('Digite la nueva ubicación de la reunión aquí', self.ubicacion)
        enlace_zoom = st.text_input('Digite el nuevo enlace de zoom.', self.enlace_zoom)

        if st.button("Actualizar"):
            induccion = datetime(fecha.year, fecha.month, fecha.day, hora.hour, hora.minute, 0)
            self.modificar_carta(induccion, ubicacion, enlace_zoom)
            st.balloons()
            st.success("Datos actualizados correctamente")

    def generar_excel(self, st):
        st.title("Generar excel")
        st.info("Esta sección es para generar un excel depediendo del rango de los meses en que tuvieron su entrevista")
        # Se seleccionan los rangos
        f_inicial = st.date_input("Rango inicial")
        f_final = st.date_input("Rango final")
        if len(self.entrevistas) != 0:
            if st.button("Generar excel"):
                # Llama al controlador del excel para generarlo
                controlador_xl = Controlador_excel()
                controlador_xl.exportar_informacion(self, f_inicial, f_final)
                st.success("Excel generado en la carpeta del programa outputs")
        else:
            st.error("No hay entrevistados")

    def cambiar_firma_firmante(self, st):
        st.title("Cambiar Firma & Firmante")
        st.header("Bienvenido Director/a de programa")
        # Se piden los nuevos datos junto a una nueva imagen
        st.image(self.firma, caption='Firma actual')
        firma = st.file_uploader("Carga la nueva firma aquí")
        st.write("Firmante actual: ", self.firmante)
        firmante = st.text_input('Digite la nueva firma aquí')
        st.write("Rol actual: ", self.rol)
        rol = st.text_input('Digite el nuevo rol aquí')

        if st.button('Actualizar'):
            if firma and firmante != "" and rol != "":
                self.modificar_firma_firmante(firma, firmante, rol)
                st.balloons()
                st.success("Se han actualizado los credenciales correctamente.")
            else:
                st.warning("Por favor llenar todos los campos")
    def generar_concepto_entrevista(self, st):
        st.title("Generar concepto de entrevista")
        # Se selecciona una tupla que contiene la llave del aspirante junto a su nombre
        selec = st.selectbox('Selecciona el aspirante entrevistado',
                             [(self.entrevistas[key].aspirante.nombre, key) for key in
                              self.entrevistas])
        st.header("Evaluar aspirante")
        admitido = st.selectbox("Evaluar", ['Admitido', 'Admitido con Reserva', 'No admitido'])
        periodo = self.entrevistas[selec[1]].semestre
        if admitido != 'No admitido':
            periodo = st.selectbox("Seleccione el periodo de admision", [self.entrevistas[selec[1]].semestre, self.generar_periodo_posterior()])
        info_admision = st.text_area("Motivo de respuesta", '(Sin Condiciones)')
        if st.button("Enviar"):
            self.entrevistas[selec[1]].infoadmitido = info_admision
            self.entrevistas[selec[1]].admitido = admitido
            self.entrevistas[selec[1]].semestre = periodo
            st.success("Información registrada correctamente")
        else:
            st.info("Porfavor llenar todos los campos")