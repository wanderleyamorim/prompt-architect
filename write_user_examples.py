import os

project_dir = '/a0/work_dir/prompt_architect_project'
os.chdir(project_dir)

file_content = '''### **User Prompts for README.md Examples**

#### **Example 1: Simple Request**

**User Prompt:** "Write a summary of the new Anthropic prompt leak."

#### **Example 2: Complex Request**

**User Prompt:** "I need a Python script that analyzes a CSV file of sales data. It should calculate total sales per region, identify the top 3 best-selling products, and flag any sales anomalies (e.g., sales significantly lower than the average for that product). The output should be a JSON report, and the script should handle missing values gracefully."

#### **Example 3: Creative Request**

**User Prompt:** "Write a short, inspiring poem about the future of AI, focusing on collaboration between humans and machines. It should be optimistic and avoid dystopian themes."

#### **Example 4: Technical Request with Constraints**

**User Prompt:** "Generate a SQL query to retrieve all customer names and their last order dates from a 'customers' table and an 'orders' table. The query should only include customers who have placed an order in the last 6 months and should be optimized for performance. Ensure the output is ordered by the last order date in descending order."

#### **Example 5: Multi-step Task Request**

**User Prompt:** "I need to set up a new web server on a Linux VM. First, install Nginx. Then, configure it to serve a static HTML page from `/var/www/html/my_site`. Finally, ensure it starts automatically on boot and is accessible from the internet (assuming port 80 is open). Provide the exact commands I need to run, step-by-step."
'''

with open('prompt_architect_user_examples.txt', 'w') as f:
    f.write(file_content)
