class ConcatenateParameter:

        def concatenate(self, **kwargs):
            sentence = ", ".join(f"{key} is {value}" for key, value in kwargs.items())
            print(sentence)

        def concateList(self, **kwargs):
            for key, value in kwargs.items():
                print(f"{key}: {value}")