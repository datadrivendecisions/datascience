# Generate a Task List from a PRD**

## **Goal**

To guide an AI assistant in creating a detailed, step-by-step task list in Markdown format based on an existing Product Requirements Document (PRD). The task list should guide a developer through implementation.

## **Output**

* **Format:** Markdown (.md)

## **Process**

1. **Receive PRD Reference:** The user points you to a specific PRD file.  
2. **Analyze PRD:** You read and analyze the functional requirements, user stories, and other sections of the specified PRD.  
3. **Phase 1: Generate Parent Tasks:** Based on the PRD analysis, generate the main, high-level tasks required to implement the feature. Use your judgment on how many high-level tasks to use. It's likely to be about 5\.  
4. **Phase 2: Generate Sub-Tasks:** Break down each parent task into smaller, actionable sub-tasks necessary to complete the parent task. Ensure sub-tasks logically follow from the parent task and cover the implementation details implied by the PRD.  
5. **Identify Relevant Files:** Based on the tasks and PRD, identify potential files that will need to be created or modified. List these under the Relevant Files section, including corresponding test files if applicable.  
6. **Generate Final Output:** Combine the parent tasks, sub-tasks, relevant files, and notes into the final Markdown structure.

## **Output Format**

\#\# Tasks

\- \[ \] 1.0 Parent Task Title  
  \- \[ \] 1.1 \[Sub-task description 1.1\]  
  \- \[ \] 1.2 \[Sub-task description 1.2\]  
\- \[ \] 2.0 Parent Task Title  
  \- \[ \] 2.1 \[Sub-task description 2.1\]  
\- \[ \] 3.0 Parent Task Title (may not require sub-tasks if purely structural or configuration)

## **Target Audience**

Assume the primary reader of the task list is a **junior developer** who will implement the feature.