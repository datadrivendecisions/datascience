# **Prompt 1: Generating a Product Requirements Document (PRD)**

## **Goal**

The PRD should be clear, actionable, and suitable for a junior developer to understand and implement the system.

## **Process**

1. **Ask Clarifying Questions:** Before writing the PRD, you *must* ask clarifying questions to gather sufficient detail. The goal is to understand the "what" and "why" of the feature, not necessarily the "how" (which the developer will figure out). Make sure to provide options in letter/number lists so I can respond easily with my selections.  
2. **Generate PRD:** Based on the initial prompt and the user's answers to the clarifying questions, generate a PRD using the structure outlined below.

## **Clarifying Questions (Examples)**

You should adapt its questions based on the prompt, but here are some common areas to explore:

* **Problem/Goal:** "What problem does this feature solve for the user?" or "What is the main goal we want to achieve with this feature?"  
* **Target User:** "Who is the primary user of this feature?"  
* **Core Functionality:** "Can you describe the key actions a user should be able to perform with this feature?"  
* **User Stories:** "Could you provide a few user stories? (e.g., As a \[type of user\], I want to \[perform an action\] so that \[benefit\].)"  
* **Acceptance Criteria:** "How will we know when this feature is successfully implemented? What are the key success criteria?"  
* **Scope/Boundaries:** "Are there any specific things this feature *should not* do (non-goals)?"  
* **Data Requirements:** "What kind of data does this feature need to display or manipulate?"  
* **Design/UI:** "Are there any existing design mockups or UI guidelines to follow?" or "Can you describe the desired look and feel?"  
* **Edge Cases:** "Are there any potential edge cases or error conditions we should consider?"

## **PRD Structure**

The generated PRD should include the following sections:

1. **Introduction/Overview:** Briefly describe the feature and the problem it solves. State the goal.  
2. **Goals:** List the specific, measurable objectives for this feature.  
3. **User Stories:** Detail the user narratives describing feature usage and benefits.  
4. **Functional Requirements:** List the specific functionalities the feature must have. Use clear, concise language (e.g., "The system must allow users to upload a profile picture."). Number these requirements.  
5. **Non-Goals (Out of Scope):** Clearly state what this feature will *not* include to manage scope.  
6. **Design Considerations (Optional):** Link to mockups, describe UI/UX requirements, or mention relevant components/styles if applicable.  
7. **Technical Considerations (Optional):** Mention any known technical constraints, dependencies, or suggestions (e.g., "Should integrate with the existing Auth module").  
8. **Success Metrics:** How will the success of this feature be measured? (e.g., "Increase user engagement by 10%", "Reduce support tickets related to X").  
9. **Open Questions:** List any remaining questions or areas needing further clarification.

# **Prompt 2: Generating a Task List from a PRD**

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