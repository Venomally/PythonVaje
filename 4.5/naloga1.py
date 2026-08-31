import pyasn1
print(pyasn1.__version__)
from pyasn1.type import univ, namedval, constraint, namedtype, tag, char,useful
from pyasn1.codec.ber import encoder, decoder


#vrste spremenljivk
#string
char.UTF8String('Živjo!')
#boolean
univ.Boolean(True)
#real number (float)
univ.Real(1.23123)


char.UTF8String.subtypeSpec

class DanVTednu(char.UTF8String):
    subtypeSpec = char.UTF8String.subtypeSpec + constraint.SingleValueConstraint('ponedeljek', 'torek', 'sreda', 'četrtek', 'petek', 'sobota', 'nedelja')

print(DanVTednu('petek').prettyPrint())


#b

class Datum(univ.Sequence):
    componentType = namedtype.NamedTypes(namedtype.NamedType('leto', univ.Integer()), namedtype.NamedType('mesec', univ.Integer()), namedtype.NamedType('dan', univ.Integer()))

date = Datum()

date.setComponentByName('leto', 2023)
date.setComponentByName('mesec',11)
date.setComponentByName('dan', 20)

print(date['leto'].prettyPrint(), date['mesec'].prettyPrint(), date['dan'].prettyPrint())

