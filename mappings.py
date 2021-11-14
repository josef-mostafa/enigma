from collections import namedtuple
from enum import Enum
from typing import Any

from datastructs import Map


class Mapping:
    def __init__(self) -> None:
        self.characters: str

    def forward(self, character: Any) -> Any:
        return self.forward_mappings.get(character)

    def reverse(self, character: Any) -> Any:
        return self.reverse_mappings.get(character)


class CharacterMap(Mapping):
    """
        This class is used to map characters to their number equivalent and vice versa.
    """
    def __init__(self) -> None:
        self.characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ,./;'[]-=!@#$%^&*()"
        self.size = len(self.characters)
        self.forward_mappings: Map = Map(self.size)
        self.reverse_mappings: Map = Map(self.size)
        for i, c in enumerate(self.characters):
            self.forward_mappings.insert(c, str(i + 1))
            self.reverse_mappings.insert(str(i + 1), c)

    def get_characters(self) -> str:
        return self.characters


class RotorMap(Mapping):
    """
        This class is used to represent a rotor mapping.
    """
    def __init__(self, mapping_string) -> None:
        chars = CharacterMap()
        self.forward_mappings: Map = Map(chars.size)
        self.reverse_mappings: Map = Map(chars.size)
        for i, c in enumerate(chars.get_characters()):
            self.forward_mappings.insert(int(chars.forward(c)), int(
                chars.forward(mapping_string[i])))
            self.reverse_mappings.insert(int(chars.forward(mapping_string[i])), int(
                chars.forward(c)))


class ReflectorMap(Mapping):
    """
        This class is used to represent a reflector mapping.
    """
    def __init__(self, mapping_string) -> None:
        chars = CharacterMap()
        self.forward_mappings: Map = Map(chars.size)
        for i, c in enumerate(chars.get_characters()):
            self.forward_mappings.insert(int(chars.forward(c)), int(
                chars.forward(mapping_string[i])))

    def reverse(self, character: int) -> int:
        return self.forward.get(character, character)


RotorDefinition = namedtuple("RotorDefinition", ["name", "mapping", "notch"])
ReflectorDefinition = namedtuple("ReflectorDefinition", ["name", "mapping"])


class RotorTypes(Enum):
    """
        These are the default rotors used in the Enigma machine.
    """
    I = RotorDefinition(
        "I", "%MluQF^a4$xXH3RWf,pb6N/[YKcIq(i*CtLh5s;Oe&zT1w7PU@d !rBSVmj=J]o#G'E.8gAZ2v09nky-D)", "Q")
    II = RotorDefinition(
        "II", "JLoAC3q/%(wrT&d ue*i)t=18z$VN^KcnpMh9#DWkb5lmR-Q4YsU0]BHPSEf62v@GI![y7ax,X;'jOF.Zg", "E")
    III = RotorDefinition(
        "III", ";Z@UE%Q#]OtCfXGra$v14x3yd)sPkBcIwh9R^j6Nl87&[uL0(2Y=H!gqWSJ'eViF ,oK5*zApT.mM-/Dnb", "V")
    IV = RotorDefinition(
        "IV", "uAGQx6YjSr@ev4g'&N*-wC%10K2yU#J;hFb] [9kWsz/qp5RL!c=m,oBMDH$dTXVPn.t^8(iOlEf73ZaI)", "J")
    V = RotorDefinition(
        "V", "V!g;u%i^Ej&3805Cdtr4Pqv$/#yc'@koD-N6UKp7aZ)mw A]xs,nIReb9XG=lB(H1SYLQhWT*z[.fOJM2F", "Z")


class ReflectorTypes(Enum):
    """
        These are the default reflectors used in the Enigma machine.
    """
    A = ReflectorDefinition(
        "A", "&f0%Q7xPvwObM9KHEtcgu/;o@,6LSp5BT .jlk$zXd=2(RUIJG)n1r-'eaF8NChZiVW43q^YmD!Asy")
    B = ReflectorDefinition(
        "B", "9BCsA3TVwSMPE!K(bIFQR^8j50d m/N$;@GnaxX%-6f.Dy7cULvi2Y)JZr1lHeWpzhO,'k4ut=&ogq")
    C = ReflectorDefinition(
        "C", "t1KHs%(e /oig,&6IvBQcEkUTAzF*7yG3wVxfnl)Yjp$-^q[OauZ;WRS89JXmNPh'=@0C]!LM5d2r.D4b#")
