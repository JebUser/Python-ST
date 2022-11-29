from abc import ABC

from controller.Controlador import Controlador


class Control_Director_Pos(Controlador, ABC):
    def __init__(self) -> None:
        Controlador.__init__(self)

    def cambiar_firma_firmante(self, st):
        # Se piden los nuevos datos junto a una nueva imagen
        st.title("Cambiar Firma & Firmante")
        st.header("Bienvenido Director/a de posgrado")
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
        info_admision = st.text_area("Motivo de respuesta", '(Sin Condiciones)')
        if st.button("Enviar") and info_admision != "":
            self.entrevistas[selec[1]].infoadmitido = info_admision
            self.entrevistas[selec[1]].admitido = admitido
            self.entrevistas[selec[1]].semestre = periodo
            st.success("Información registrada correctamente")
        else:
            st.info("Porfavor llenar todos los campos")