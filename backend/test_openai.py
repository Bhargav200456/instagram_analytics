from services.insight_service import client


response = client.responses.create(
    model="gpt-5.6-luna",
    input="Explain Instagram clustering in one sentence."
)

print(response.output_text)