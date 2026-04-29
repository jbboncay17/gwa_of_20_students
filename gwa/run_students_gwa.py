from students_gwa import StudentGWA

gwa_checker = StudentGWA("gwa.txt")
name, grade = gwa_checker.get_highest()

print(f"Top Student: {name} with GWA: {grade}")
