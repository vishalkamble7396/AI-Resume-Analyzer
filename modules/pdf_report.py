from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(score, skills, career):

    pdf = SimpleDocTemplate("Resume_Report.pdf")

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Resume Analyzer Report</b>", styles["Title"]))

    story.append(Paragraph(f"Resume Score : {score}/100", styles["Normal"]))

    story.append(Paragraph(f"Career Recommendation : {career}", styles["Normal"]))

    story.append(Paragraph("<b>Skills Found</b>", styles["Heading2"]))

    for skill in skills:
        story.append(Paragraph(skill, styles["Normal"]))

    pdf.build(story)

    return "Resume_Report.pdf"