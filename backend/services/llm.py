import openai

# its the core logic that talks to OpenAI GPT-4 to get a response based on the user's voice input and your workflow.json.
async def ask_llm(query, workflow_context):
    context = f"Workflow: {workflow_context}\nUser asked: {query}"
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You're an expert in n8n workflows."},
                  {"role": "user", "content": context}]
    )
    return res.choices[0].message["content"]
