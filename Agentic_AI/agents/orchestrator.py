from agents.file_agent import FileAgent
from agents.analysis_agent import AnalysisAgent
from agents.pdf_agent import PDFAgent

class OrchestratorAgent:

    def __init__(self):

        self.file_agent = FileAgent()
        self.analysis_agent = AnalysisAgent()
        self.pdf_agent = PDFAgent()

    def run_file_pipeline(self, file_path):

        df = self.file_agent.load_file(file_path)

        analysis = self.analysis_agent.run(df)

        pdf = self.pdf_agent.run(analysis)

        return pdf