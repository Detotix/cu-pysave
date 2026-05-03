
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
        self.saves={}
    
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
        if "HEAD" not in self.saves: self.saves["HEAD"]=CU_Limb(self._data[0])
        return self.saves["HEAD"]
    @property
    def THORAX(self):
        if "THORAX" not in self.saves: self.saves["THORAX"]=CU_Limb(self._data[1])
        return self.saves["THORAX"]
    @property
    def ABDOMEN(self):
        if "ABDOMEN" not in self.saves: self.saves["ABDOMEN"]=CU_Limb(self._data[2])
        return self.saves["ABDOMEN"]
    @property
    def UPPER_RIGHT_ARM(self):
        if "UPPER_RIGHT_ARM" not in self.saves: self.saves["UPPER_RIGHT_ARM"]=CU_Limb(self._data[3])
        return self.saves["UPPER_RIGHT_ARM"]
    @property
    def RIGHT_FOREARM(self):
        if "RIGHT_FOREARM" not in self.saves: self.saves["RIGHT_FOREARM"]=CU_Limb(self._data[4])
        return self.saves["RIGHT_FOREARM"]
    @property
    def RIGHT_HAND(self):
        if "RIGHT_HAND" not in self.saves: self.saves["RIGHT_HAND"]=CU_Limb(self._data[5])
        return self.saves["RIGHT_HAND"]
    @property
    def UPPER_LEFT_ARM(self):
        if "UPPER_LEFT_ARM" not in self.saves: self.saves["UPPER_LEFT_ARM"]=CU_Limb(self._data[6])
        return self.saves["UPPER_LEFT_ARM"]
    @property
    def LEFT_FOREARM(self):
        if "LEFT_FOREARM" not in self.saves: self.saves["LEFT_FOREARM"]=CU_Limb(self._data[7])
        return self.saves["LEFT_FOREARM"]
    @property
    def LEFT_HAND(self):
        if "LEFT_HAND" not in self.saves: self.saves["LEFT_HAND"]=CU_Limb(self._data[8])
        return self.saves["LEFT_HAND"]
    @property
    def RIGHT_THIGH(self):
        if "RIGHT_THIGH" not in self.saves: self.saves["RIGHT_THIGH"]=CU_Limb(self._data[9])
        return self.saves["RIGHT_THIGH"]
    @property
    def RIGHT_CRUS(self):
        if "RIGHT_CRUS" not in self.saves: self.saves["RIGHT_CRUS"]=CU_Limb(self._data[10])
        return self.saves["RIGHT_CRUS"]
    @property
    def RIGHT_FOOT(self):
        if "RIGHT_FOOT" not in self.saves: self.saves["RIGHT_FOOT"]=CU_Limb(self._data[11])
        return self.saves["RIGHT_FOOT"]
    @property
    def LEFT_THIGH(self):
        if "LEFT_THIGH" not in self.saves: self.saves["LEFT_THIGH"]=CU_Limb(self._data[12])
        return self.saves["LEFT_THIGH"]
    @property
    def LEFT_CRUS(self):
        if "LEFT_CRUS" not in self.saves: self.saves["LEFT_CRUS"]=CU_Limb(self._data[13])
        return self.saves["LEFT_CRUS"]
    @property
    def LEFT_FOOT(self):
        if "LEFT_FOOT" not in self.saves: self.saves["LEFT_FOOT"]=CU_Limb(self._data[14])
        return self.saves["LEFT_FOOT"]