
class CU_Limb:
    '''
    class for each limb, this is used to easily change data of each limb using names
    '''
    def __init__(self, data: dict):
        self._data = data
    
    def dict(self):
        return self._data
    def loaddict(self, data: dict):
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")
        self._data = data

class CU_Limbs:
    '''
    This class is for easily chaning data of each limb using names
    because in the savefile its just a list of limbs without names.
    '''
    def __init__(self, limbsdata: list):
        if not isinstance(limbsdata, list):
            raise TypeError("limbsdata must be a list")
        self._data = limbsdata
    
    def list(self):
        return self._data
    def loadlist(self, data: list):
        if not isinstance(data, list):
            raise TypeError("data must be a list")
        self._data = data

    '''
    limbs
    '''

    @property
    def HEAD(self):
        return CU_Limb(self._data[0])
    @property
    def THORAX(self):
        return CU_Limb(self._data[1])
    @property
    def ABDOMEN(self):
        return CU_Limb(self._data[2])
    @property
    def UPPER_RIGHT_ARM(self):
        return CU_Limb(self._data[3])
    @property
    def RIGHT_FOREARM(self):
        return CU_Limb(self._data[4])
    @property
    def RIGHT_HAND(self):
        return CU_Limb(self._data[5])
    @property
    def UPPER_LEFT_ARM(self):
        return CU_Limb(self._data[6])
    @property
    def LEFT_FOREARM(self):
        return CU_Limb(self._data[7])
    @property
    def LEFT_HAND(self):
        return CU_Limb(self._data[8])
    @property
    def RIGHT_THIGH(self):
        return CU_Limb(self._data[9])
    @property
    def RIGHT_CRUS(self):
        return CU_Limb(self._data[10])
    @property
    def RIGHT_FOOT(self):
        return CU_Limb(self._data[11])
    @property
    def LEFT_THIGH(self):
        return CU_Limb(self._data[12])
    @property
    def LEFT_CRUS(self):
        return CU_Limb(self._data[13])
    @property
    def LEFT_FOOT(self):
        return CU_Limb(self._data[14])