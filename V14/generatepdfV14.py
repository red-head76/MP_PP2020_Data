import generatepdf_base as gpdf
import numpy as np
from get_students import get_students

students = get_students()
experiment = "V14"

for student in students:
    workingDir = experiment + "/" + student + "/"
    gpdf.addText("Versuchsdaten für " + student.replace('_', ' '))
    gpdf.addText("Versuch Nummer " + experiment[1:])
    gpdf.addSpacer()

    m_cu, m_ges, T_1, T_2, d = np.load(workingDir + "DataV14Part1.npy")

    gpdf.addText("Masse des leeren Kalorimeters: {:.1f} g".format(m_cu))
    gpdf.addSpacer()

    gpdf.addText("Masse des gefüllten Kalorimeters: {:.1f} g".format(m_ges))
    gpdf.addSpacer()

    gpdf.addText("Temperatur vor der Erwärmung: {:.1f} °C".format(T_1))
    gpdf.addSpacer()

    gpdf.addText("Temperatur nach der Erwärmung: {:.1f} °C".format(T_2))
    gpdf.addSpacer()

    gpdf.addText("Durchmesser des Kalorimeters: {:.1f} mm".format(d))
    gpdf.addSpacer()

    gpdf.addPagebreak()

gpdf.createPDF(experiment)
