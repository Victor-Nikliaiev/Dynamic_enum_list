from enum import Enum

class CreateDynamicEnumList:
    def __init__(self, name, dictionary):  
        self.name = name
        self.dictionary = dictionary     
        self._enum = Enum(name, dictionary)     
    
    def add(self, key, value):       
        """Add a new key-value pair to the enum."""
        if key in self.dictionary:
            raise ValueError(f"'{key}' already exists in '{self.name}'")
        self.dictionary[key] = value
        self._enum = Enum(self.name, self.dictionary)

    def remove(self, key):
        """Remove a key-value pair from the enum."""
        self.dictionary.pop(key)
        self._enum = Enum(self.name, self.dictionary)
    
    def __getattr__(self, item):
        try:
            return self._enum[item].value
        except KeyError:
            raise AttributeError(f"'{self.name}' has no attribute '{item}'")
    
    def __iter__(self):
        """Iterate over the enum members as dictionaries."""
        for member in self._enum:
            yield {member.name: member.value}
    
    def __repr__(self):
        return f"""<DynamicEnumList: {self.name}> {self.dictionary}"""


Color = CreateDynamicEnumList("Color", {
    "RED":   "red", 
    "GREEN": "green", 
    "BLUE":  "blue",
    "GRAY":  "gray"
})

Color.add("BLACK", "black")
print(Color)

for color in Color:
    print(color)


 