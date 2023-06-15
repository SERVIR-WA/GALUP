from typing import Tuple, Sequence, Dict, Any

LAND_USES = {
    0: "border",
    1: "agriculture",
    2: "conservation",
    3: "urban",
    4: "water",
    5: "herbaceous",
}

LAND_USES_ABBR = {
    "border": "border",
    "agriculture": "ag",
    "conservation": "con",
    "urban": "urb",
    "water": "water",
    "herbaceous": "herb",
}


class LandUse:
    """Land use class for GA analysis."""

    def __init__(self, landuse):
        try:
            self.lu_name = LAND_USES[landuse]
            self.lu_abbr = LAND_USES_ABBR[self.lu_name]
            self.lu_code = landuse
        except KeyError:
            try:
                self.lu_abbr = LAND_USES_ABBR[landuse]
                self.lu_code = list(LAND_USES.values()).index(landuse)
                self.lu_name = landuse
            except KeyError:
                try:
                    self.lu_code = list(LAND_USES_ABBR.values()).index(landuse)
                    self.lu_name = LAND_USES[self.lu_code]
                    self.lu_abbr = LAND_USES_ABBR[self.lu_name]
                except ValueError:
                    raise ValueError("Invalid land use.")

    def __str__(self):
        return self.lu_name

    def is_border(self):
        return self.lu_code == 0

    def is_water(self):
        return self.lu_code == 4

    def is_herb(self):
        return self.lu_code == 5

    def is_core(self):
        if self.is_herb() or self.is_water() or self.is_border():
            return False
        return True


class LandUsePreference:
    def __init__(self, lu_code: int, preference: int):
        if LandUse(lu_code).is_core():
            self.landuse = LandUse(lu_code)
        else:
            raise ValueError("Only ag, con, and urb can have a preference.")
        self.preference = preference

    @staticmethod
    def check_preference(value):
        if value not in (1, 2, 3):
            raise ValueError("Preference must be 1, 2, or 3.")
        return value

    @property
    def preference(self):
        return self._preference

    @preference.setter
    def preference(self, value):
        self._preference = self.check_preference(value)


class LandUseConflict:
    def __init__(self, ag_pref, con_pref, urb_pref):
        self.ag_pref = LandUsePreference(1, ag_pref)  # ag: lu_code=1
        self.con_pref = LandUsePreference(2, con_pref)  # con: lu_code=2
        self.urb_pref = LandUsePreference(3, urb_pref)  # urb: lu_code=3
        self.preferences = [
            self.ag_pref.preference,
            self.con_pref.preference,
            self.urb_pref.preference,
        ]
        self.conflict_freq = None
        self.conflict_uses = None

    @property
    def preferred_uses(self) -> Tuple:
        preferred_val = max(self.preferences)
        return tuple([k for k, v in self.as_dict().items() if v == preferred_val])

    @property
    def isinconflict(self) -> bool:
        if len(set(self.preferences)) != 3:  # if there's repetitive preference
            return True
        else:
            return False

    def as_dict(self) -> Dict:
        return dict(zip([1, 2, 3], self.preferences))

    def overall_conflict(self) -> float:
        if self.isinconflict:
            # most occurrences preference value reveals land-use conflict
            conflict_val = max(self.preferences, key=self.preferences.count)
            self.conflict_uses = tuple(
                [k for k, v in self.as_dict().items() if v == conflict_val]
            )
            # count the number of occurrences with the conflict value
            self.conflict_freq = self.preferences.count(conflict_val)
            return self.conflict_freq * np.sqrt(
                np.einsum("i,i->", self.preferences, self.preferences)
            )
        else:
            self.conflict_uses = tuple()
            self.conflict_freq = 0
            return 0

    def urban_conflict(self) -> float:
        lup_dict = self.as_dict()
        urb_ag = lup_dict[3] / lup_dict[1]
        urb_con = lup_dict[3] / lup_dict[2]
        if urb_ag > 1:
            urb_ag_conf = 0
        else:
            urb_ag_conf = 1 / urb_ag
        if urb_con > 1:
            urb_con_conf = 0
        else:
            urb_con_conf = 1 / urb_con
        return urb_ag_conf + urb_con_conf
