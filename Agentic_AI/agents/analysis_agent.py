from langchain_core.prompts import PromptTemplate
from .base_agent import BaseAgent

class AnalysisAgent(BaseAgent):

    def run(self, dataframe):

        preview = dataframe.head(10).to_string()

        template = '''
        Analyze the following dataset and provide insights.

        Dataset preview:
        {data}

        Provide:
        - summary
        - trends
        - anomalies
        - interesting findings
        '''

        prompt = PromptTemplate.from_template(template)

        response = self.llm.invoke(prompt.format(data=preview))

        return response.content