import pickle

class Object:
    def init(self):
        self.name = "sadia"
        self.age = 23

object = Object()
with open('object.pkl','w') as f:
    pickle.dump(object,f)
    print(f"the pickle file is saved ")