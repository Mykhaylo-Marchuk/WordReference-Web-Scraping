from app.schemas.word_model import WordModel
from app.services.rae.router import router_get_word


def test_parse_response_into_word():
    """
    Tests router's transformation from Response to Word format.
    """
    response: WordModel = router_get_word(name="perro")

    name="perro"
    definitions: set = {
            'adj. col. Muy malo, indigno:mentira perra.',
            'm. y f. Mamífero carnívoro doméstico de la familia de los cánidos, de tamaño, forma y pelaje muy diversos, producto de las distintas razas obtenidas por hibridación, que está adaptado a todas las regiones de la tierra y que se caracteriza por su fidelidad al hombre.  desp. Nombre que se dio despectivamente a los fieles de otras religiones:perro judío; perra infiel.  Persona despreciable.  f. Rabieta de niño.  Deseo muy grande, manía u obsesión:qué perra le ha dado con ir al cine.  col. Dinero, riqueza. Más en pl.:tiene muchas perras.  desp. Ramera, prostituta.  perra chica col. Moneda de cobre o aluminio que valía cinco céntimos de peseta.  perra gorda o grande col. Moneda de cobre o aluminio que valía diez céntimos de peseta.  perro caliente Véase perrito caliente.  perro faldero El pequeño, que se tiene como animal de compañía.  perro policía El adiestrado para descubrir y perseguir aquello que se desea capturar.  perro pastor alemán Véase pastor.  a otro perro con ese hueso loc. Se emplea para rechazar una proposición o mostrar desconfianza.  como el perro y el gato loc. adv. col. Expresión con que se explica el aborrecimiento mutuo que se tienen algunos. Más con el verbo llevarse: estos hermanos se llevan como el perro y el gato.  de perro o perros loc. Que es sumamente molesto y desagradable:día de perros.  echar o soltar los perros a alguien loc. col. Regañarlo, echarle una bronca:mi madre me echó los perros en cuanto abrí la puerta.  morir uno como un perro loc. Morir sin dar señales de arrepentimiento.  loc. Morir solo, abandonado, sin ayuda alguna.  muerto el perro, se acabó la rabia loc. Cuando acaba la causa de algo, también lo hacen sus efectos.  tratar a alguien como a un perro loc. col. Maltratarlo, despreciarlo:lo trataron como a un perro y lo echaron de allí.'}
    assert response.name == name, "name wronk"
    response_definitions: set = set(response.definitions)
    assert definitions.issubset(response_definitions), "definition wronk"