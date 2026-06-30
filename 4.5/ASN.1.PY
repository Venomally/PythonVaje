import pyasn1 
print(pyasn1.__version__)
from pyasn1.type import univ, namedval, constraint
from pyasn1.type import  namedtype, tag, char
from pyasn1.type import useful
from pyasn1.codec.ber import encoder, decoder



char.UTF8String('Zivjo')

univ.Boolean(True)
univ.Real(1.23123)

char.UTF8String.subtype


# Define the ASN.1 type for a list of REAL numbers
ListOfReals = univ.SequenceOf(componentType=univ.Real())

# Define the ASN.1 type for the MeasurementData SEQUENCE
class MeasurementData(univ.Sequence):
    componentType = namedtype.NamedTypes(
        # Define the 'firstArray' component, which is a ListOfReals
        namedtype.NamedType('firstArray', ListOfReals),

        # Define the 'secondArray' component, which is also a ListOfReals
        namedtype.NamedType('secondArray', ListOfReals)
    )
    
stvar = MeasurementData()

# Initialize the sequence and populate it
reals = univ.SequenceOf(componentType=univ.Real())
reals.extend([1.0, 2.0, 3.0]) # Use floats to be safe

stvar['firstArray'] = reals

print(stvar.prettyPrint())


stvar['firstArray'] = ListOfReals.setComponents(1.0*2, 2.0*2, 3.0*2)
print(stvar.prettyPrint())
