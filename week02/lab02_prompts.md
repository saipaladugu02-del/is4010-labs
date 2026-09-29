# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

I installed GitHub Copilot CLI using the official install script and signed in with my GitHub account through the browser. Version: GitHub Copilot CLI 1.0.89.

### Antigravity CLI

I installed Antigravity CLI using the official install script and signed in with my Google account using Google OAuth. Version: 1.2.13.

## Shared task

### Shared prompt

```text
Write a Python function count_vowels(text: str) -> int that counts the vowels a, e, i, o, and u in text, ignoring uppercase and lowercase. Do not count the letter y. Include a short docstring. Show me the code and explain it briefly, but do not create or edit any files.
```

### Copilot CLI observations

Copilot responded with a very brief one-line solution, using sum() together with a generator that converts each character to lowercase and then checks if it is one of the letters in the string "aeiou". The explanation was one sentence stating that uppercase vowels are counted and that y is not included. I wasn't sure how adding together True and False values results in a number, since that wasn't clear to me as a beginner. I would check that an empty string returns 0 and that a mixed-case word such as "OpenAI" is counted correctly. It followed my instruction and did not make any changes to the files.

### Antigravity CLI observations

Antigravity converted the entire text to lowercase once, put the vowels into a set, and added one for each character that was a vowel. Its docstring says the count is case-insensitive, and it included a more detailed explanation with three bullet points. It noted that a set allows for O(1) lookup, which I didn't completely understand, so I'd like to look that up. During setup, it warned that AI agents can run code and should be monitored, which is one of the reasons I told both tools not to create or edit any files. I would check it using a word that contains no vowels, for example "rhythms".

### Comparison

Both responses were correct. They both ignored whether letters were uppercase or lowercase, did not count the letter y, and should return 0 when the string is empty. The main difference was their style. Copilot's version was shorter, only one line, but it depended on the fact that True counts as 1, which is harder for a beginner to see. Antigravity's version was a bit longer, but each step was easier to understand: it converted the text to lowercase, defined the vowels, and then added 1 for each match. Antigravity also gave a more detailed explanation, while Copilot gave only one sentence. Both solutions assumed the text contains only ordinary English letters, so accented vowels such as "é" would not be counted. I chose Antigravity's version because I could go through it step by step and explain what each line does, and its docstring clearly states the case-insensitive rule in the code.

## Test-guided implementation

I used the command `uv run --directory week02 python -m pytest tests/ -v` to run the grader. The first time, it failed with the error "No such file or directory" because the VS Code terminal had opened in the parent is4010 folder instead of the repository folder. After I ran `cd is4010-labs`, the tests worked and all 9 function tests passed on the first attempt. The only failures were the journal checks, because I hadn't created the lab02_prompts.md file yet. The vowel tests verified the key rules: "OpenAI" gave 4, which shows that uppercase vowels are included; "rhythms" returned 0, meaning y is not counted; and an empty string returned 0. The greeting and even-number tests also passed, covering an empty name, zero, and negative numbers. I did not have to change the code, but going through these test cases helped me understand why the final behavior matches each function contract.

## Preferred tool combination

The most helpful tool for me this week was a browser chat, because I wanted detailed explanations for each command, error, and screen. I also used a browser chat to help me organize and word this journal. Setting up the tools was the hardest part for me: I had to sign in to each one separately, and I got confused when Antigravity asked me to paste an authorization code back into the terminal. Copilot CLI and Antigravity CLI were useful because they run inside the repository and can see the project files, but I had to be careful about what changes they were allowed to make. I haven't used GitHub Copilot inside VS Code much yet, but it seems useful for short suggestions while typing. Right now I prefer using a browser chat to understand concepts and a CLI tool like Antigravity for code with clear explanations, then checking everything with the tests. This could change on a larger project with many files, where a CLI agent that can read the whole repository would save more time, or if I hit the usage limits of a free plan.