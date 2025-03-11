from unittest import mock

from requests import Response
from starlette import status

from app.schemas.word_model import WordModel
from app.services.rae.get_word import parse_response_into_word
from unittest.mock import Mock

from app.shared.utils import read_file


def test_parse_response_into_word():
    """
    Tests transformation from Response to Word format.
    """
    mock_response = Mock(spec=Response)
    mock_response.text = read_file("./perro_definition.html")

    mock_response.status_code = status.HTTP_200_OK
    mock_word: WordModel = parse_response_into_word(response=mock_response, name="test", url="test")

    real_word: WordModel = WordModel(
        name="perro",
        definitions=['adj. col. Muy malo, indigno:mentira perra.', 'm. y f. Mamífero carnívoro doméstico de la familia de los cánidos, de tamaño, forma y pelaje muy diversos, producto de las distintas razas obtenidas por hibridación, que está adaptado a todas las regiones de la tierra y que se caracteriza por su fidelidad al hombre.  desp. Nombre que se dio despectivamente a los fieles de otras religiones:perro judío; perra infiel.  Persona despreciable.  f. Rabieta de niño.  Deseo muy grande, manía u obsesión:qué perra le ha dado con ir al cine.  col. Dinero, riqueza. Más en pl.:tiene muchas perras.  desp. Ramera, prostituta.  perra chica col. Moneda de cobre o aluminio que valía cinco céntimos de peseta.  perra gorda o grande col. Moneda de cobre o aluminio que valía diez céntimos de peseta.  perro caliente Véase perrito caliente.  perro faldero El pequeño, que se tiene como animal de compañía.  perro policía El adiestrado para descubrir y perseguir aquello que se desea capturar.  perro pastor alemán Véase pastor.  a otro perro con ese hueso loc. Se emplea para rechazar una proposición o mostrar desconfianza.  como el perro y el gato loc. adv. col. Expresión con que se explica el aborrecimiento mutuo que se tienen algunos. Más con el verbo llevarse: estos hermanos se llevan como el perro y el gato.  de perro o perros loc. Que es sumamente molesto y desagradable:día de perros.  echar o soltar los perros a alguien loc. col. Regañarlo, echarle una bronca:mi madre me echó los perros en cuanto abrí la puerta.  morir uno como un perro loc. Morir sin dar señales de arrepentimiento.  loc. Morir solo, abandonado, sin ayuda alguna.  muerto el perro, se acabó la rabia loc. Cuando acaba la causa de algo, también lo hacen sus efectos.  tratar a alguien como a un perro loc. col. Maltratarlo, despreciarlo:lo trataron como a un perro y lo echaron de allí.'],
        url="test")
    assert mock_word.name == real_word.name, "name wronk"
    assert mock_word.definitions == real_word.definitions, "definition wronk"