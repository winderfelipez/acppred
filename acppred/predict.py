from acppred.models import Model

def main ():
    model = Model.load('data/models/model.pickle')
    sequence = input('peptide sequences:')
    prediction = model.predict(sequence)
    print(prediction)

if __name__ == '__main__':
    main()

