import openai

async def ask_llm(query, workflow_context):
    context = f"Workflow: {workflow_context}\nUser asked: {query}"
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You're an expert in n8n workflows."},
                  {"role": "user", "content": context}]
    )
    return res.choices[0].message["content"]
