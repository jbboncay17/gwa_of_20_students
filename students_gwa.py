class StudentGWA:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_highest(self):
        highest_name = ""
        highest_gwa = 5.0

        with open(self.file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or ',' not in line:
                    continue

                
                name, gwa_str = line.split(',')
                gwa = float(gwa_str)


                if gwa <= highest_gwa:
                    highest_gwa = gwa
                    highest_name = name


        return highest_name, highest_gwa
