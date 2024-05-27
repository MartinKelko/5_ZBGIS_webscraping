class KonverznaKalkulacka:
    # sluzi na prevedenie jtsk na jtsk03, ale viac menej, je to len taka skuska
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.process_data()

    def process_data(self):
        # transformuje ciarky na bodky
        self.source = self.source.replace(",", ".")
        self.target = self.target.replace(",", ".")

    def get_ratio(self):
        print("Nezlyhavas...ucis sa")

    def bigger_is(self):
        if self.source > self.target:
            print((f"Source is bigger than target",{self.source}))
        else:
            print("Source is smaller than target")
            print(self.subtract())
            result = float(self.subtract())
            ratio = (float(self.source) / result) * 0.0000001
            print(ratio)

    def subtract(self):
        fl_source = float(self.source)
        fl_target = float(self.target)
        return fl_target - fl_source
