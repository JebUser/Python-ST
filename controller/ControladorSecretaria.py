from abc import ABC

from controller.Controlador import Controlador
from datetime import datetime


class Control_Secretaria(Controlador, ABC):
    def __init__(self) -> None:
        Controlador.__init__(self)
        super().__init__()

    def view_modificar_carta(self, st):
        st.title("Modificar información de la carta")
        # Se modifica la carta
        fecha = st.date_input('Digite la nueva fecha de reunión aquí')
        hora = st.time_input('Digite la nueva hora de reunión aquí')

        ubicacion = st.text_input('Digite la nueva ubicación de la reunión aquí', self.ubicacion)
        enlace_zoom = st.text_input('Digite el nuevo enlace de zoom.', self.enlace_zoom)

        if st.button("Actualizar"):
            induccion = datetime(fecha.year, fecha.month, fecha.day, hora.hour, hora.minute, 0)
            self.modificar_carta(induccion, ubicacion, enlace_zoom)
            st.balloons()
            st.success("Datos actualizados correctamente")

    def generar_concepto_entrevista(self, st):
        st.title("Generar concepto de entrevista")
        # La secretaria solo rechaza, por lo que solo se pide el motivo de rechazo y le da al boton
        selec = st.selectbox('Selecciona el aspirante entrevistado',
                             [(self.entrevistas[key].aspirante.nombre, key) for key in
                              self.entrevistas])
        st.header("Evaluar aspirante")
        info_admision = st.text_area("Motivo de rechazo")
        if st.button("Rechazar") and info_admision != "":
            self.entrevistas[selec[1]].infoadmitido = info_admision
            self.entrevistas[selec[1]].admitido = "No admitido"
            st.success("Información registrada correctamente")
        else:
            st.info("Porfavor llenar todos los campos")


