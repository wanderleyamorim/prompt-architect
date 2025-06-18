import os

project_dir = '/a0/work_dir/prompt_architect_project'
os.chdir(project_dir)

readme_content = '''# Prompt Architect

## Project Name
Prompt Architect

## Objective
To engineer initial ideas into sophisticated, robust, and highly effective prompts for Large Language Models (LLMs). It aims to create comprehensive policy documents for an AI, maximizing clarity, preventing errors, and ensuring superior final output.

## Features
- **Structured Prompt Generation:** Utilizes XML-style tags for clear, hierarchical prompt structures.
- **Proactive Error Prevention:** Systematically analyzes potential failure modes and adds negative constraints.
- **Detailed and Exhaustive Prompts:** Prioritizes clarity and completeness over brevity, repeating critical instructions where necessary.
- **Dynamic Logic Integration:** Incorporates conditional logic for adaptive and intelligent AI responses.
- **Learning from Failure:** Provides both positive and negative examples for crucial formats or styles.
- **Mandated Self-Reflection:** Embeds a chain-of-thought process for complex tasks, triggered by keywords like `analyze`, `strategize`, `plan`, `synthesize`, `compare`, `recommend`.
- **Language Handling:** Accepts initial requests in Brazilian Portuguese (pt_BR) or English, but processes and outputs engineered prompts exclusively in English (en_US).

## Target Audience
Developers, prompt engineers, AI researchers, product managers, startup founders, and anyone looking to create more effective and reliable prompts for LLMs.

## Usage Instructions
1.  **Understand the Principles:** Familiarize yourself with the core principles and heuristics outlined in `prompt_architect.txt`.
2.  **Provide Your Request:** Present your initial idea or task to the Prompt Architect (e.g., by copying the content of `prompt_architect.txt` into your LLM's system prompt).
3.  **Receive Engineered Prompt:** The Prompt Architect will process your request and deliver a production-grade, engineered prompt in English, ready for use with your LLM.

## Dependencies/Requirements
- A Large Language Model (LLM) capable of understanding and executing complex, structured prompts.
- No specific programming language or framework is required to *use* the generated prompts, but understanding prompt engineering concepts is beneficial.

## Known Limitations
- The effectiveness of the engineered prompt ultimately depends on the capabilities and specific training of the LLM being used.
- While designed to prevent common errors, it cannot guarantee perfect output from all LLMs in all scenarios.
- The Prompt Architect's internal processing and final output are exclusively in English, even if the initial request is in Portuguese.

## Contact and Contribution
For questions, suggestions, or contributions, please refer to the GitHub repository issues section or contact the repository owner.

'''

with open('README.md', 'w') as f:
    f.write(readme_content)
