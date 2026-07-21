# Ninety-six questions for recovering more experience

Do not answer all of these at once. Pick one real project and write the situation, the original judgment, what failed, the evidence, and how the process changed. Concrete cases are more valuable than abstract advice.

## A. Project selection and zero-to-one

1. Which project types gained most from AI, and which gained least? What explains the difference beyond the tool?
2. Which project started in the wrong direction but discovered it later because implementation was so fast?
3. Which ideas did you abandon after discussion with ChatGPT or Codex, and why?
4. In the home-valuation project, what first changed your understanding of the problem?
5. How do you decide between continued research and beginning implementation? Is there a clear transition point?
6. Did lower experimentation cost lead you to explore an approach you otherwise would not have attempted?

## B. Requirements and scope

7. In your worst rework incident, which missing sentence in the original requirement mattered most?
8. Which requirements do agents repeatedly misunderstand even when humans think they are clear?
9. How do you turn a vague experience goal into an acceptance criterion?
10. When requirements change, do you edit the source, append a patch, or rewrite the structure? Which works best?
11. Which default behaviors most often become hidden requirements?
12. When did an explicit non-goal significantly reduce over-implementation?

## C. Architecture and design

13. What was the most typical agent over-design, and why did it initially look reasonable?
14. Which recommended architecture did you reject, and what later evidence supported your judgment?
15. When did an AI proposal improve your original architecture, and what evidence persuaded you?
16. Which module boundary, once clarified, made later agent work much more stable?
17. Which type of technical debt does AI amplify most easily?
18. How does your control method differ across UI, API, database, hardware, and ML architecture?

## D. Task decomposition and context

19. At what task size does Codex begin to lose control, and what are the early signals?
20. Which fixed sections in an implementation plan reveal problems earliest?
21. How do you decide to open a fresh context instead of patching an old conversation?
22. As a repository grows, which information must remain in persistent project instructions?
23. Which unrelated files or concerns does an agent most often modify “helpfully,” and how do you stop it?
24. How do you prevent parallel agents from changing the same boundary?

## E. Implementation and code quality

25. Which redundant code, abstractions, or fallbacks does AI generate most often?
26. When is a rewrite better than continued patching, and what is the decision rule?
27. Have you had running code whose structure could no longer evolve safely?
28. Which languages, frameworks, or styles are most stable for agents, and which are not?
29. How do you detect that an agent changed requirement semantics to pass tests?
30. Without exhaustive review, which files and paths do you sample most often?

## F. Testing and acceptance

31. When did all existing tests pass while the real feature was still wrong?
32. What is the most common self-proof loop in AI-generated tests?
33. Where is UI end-to-end testing most valuable, and where is its maintenance cost too high?
34. How do you choose real, boundary, and failure data?
35. When has the test system itself become over-designed?
36. Which invariants, once expressed as property tests, increased confidence the most?

## G. Logs, diagnosis, and runtime

37. Which log field most often shortens diagnosis?
38. Has an agent produced a confident but wrong root cause from logs? How did you detect it?
39. Are your hardest isolation problems cross-module, concurrent, environmental, or data-related?
40. How do you avoid “many logs but little information”?
41. When is a runtime path explanation more useful than direct code reading?
42. Which incidents proved to be requirement, data, or environment errors rather than code errors?

## H. Performance

43. What is the most common way AI makes SQL unnecessarily complex?
44. Which performance problem was invisible in functional tests?
45. Which budgets have you used, and where did missing an early budget become expensive?
46. At which layer does AI most often repeat work: serialization, query, copying, network, or cache?
47. How do mobile, hardware, and ML bottlenecks differ in your projects?
48. When did an “optimization” make the system slower or less stable?

## I. Algorithms and research

49. Which algorithm choice would have gone wrong if left entirely to AI?
50. How do you establish a simple baseline so a complex method cannot win by appearance?
51. Where is ChatGPT Pro noticeably stronger than a repository coding agent in reasoning or algorithms?
52. When papers, blogs, code, and experiments disagree, what do you trust?
53. Which sources most often lead AI to a plausible but false synthesis?
54. What are the key learning transitions from an unfamiliar field to a usable solution?

## J. Security, data, and production

55. Has AI written a secret, token, or sensitive value into logs, configuration, or tests?
56. What does AI most often omit in authorization and authentication logic?
57. Which dependency addition or upgrade caused an unexpected problem?
58. What was the most dangerous migration or production operation, and which safeguard was missing?
59. Have you needed an emergency rollback of a model, algorithm, firmware, or device behavior?
60. Which actions are explicitly prohibited from automatic agent execution?

## K. Tools, models, and workflow

61. What was the real reason for moving from Claude to Codex: capability, integration, speed, context, or habit?
62. Which instruction types show genuine model differences, and which differences come from workflow?
63. When do you send Codex output to ChatGPT Pro, and does the reverse flow work?
64. Which problems has multi-model review actually found, and when does it only duplicate opinions?
65. Have tool upgrades invalidated an old skill or caused side effects?
66. How do you clear wrong assumptions and historical baggage from long conversations?

## L. Skills, learning, and personal role

67. What are your three most valuable skills, and which recurring errors did they eliminate?
68. Which skill over-constrained the agent and made results worse?
69. How do you decide whether a lesson becomes a skill or remains a case note?
70. After stopping hand-written coding, where does most of your daily time go?
71. Which capability—architecture, testing, product, or algorithms—improved most through AI use?
72. Which capability could degrade through over-reliance, and how do you maintain it?

## M. AI-native review and test tools

73. When did AI review find a cross-file or cross-layer issue difficult for a person to cover?
74. Among pytest, Playwright, and Maestro, which failure artifact helps AI diagnose fastest?
75. When did tests pass but the business behavior remain wrong, and where did the bad oracle come from?
76. How do you separate architecture, functional, and implementation review across agents?
77. Which high-risk code do you still inspect deeply, and why?
78. Has an agent weakened assertions or acceptance criteria to pass? How did you prevent it?

## N. Documentation and AI-readable observability

79. Which missing or stale document caused the largest rework?
80. Which field semantics, state rules, or deployment steps exist only in your head?
81. Which structured log let an agent find a difficult issue in minutes?
82. With too much telemetry, how do you narrow by time, user, request, device, or model?
83. Do your logs record decision reasons or only outcomes?
84. When documentation and code conflict, how do you establish current truth and update the other?

## O. Human value, capability, and role change

85. Which interface was functionally complete but lacked theme and soul, and how did you change it?
86. When did an AI technology recommendation look reasonable but fail the real context?
87. Which algorithmic breakthrough came from your observation of an anomaly rather than the first AI proposals?
88. Without hand-writing code, which foundational ability must you protect and how do you train it?
89. What are the common signs of someone who can build a small app but cannot control a complex system?
90. Will your future role resemble architect, product-technical leader, researcher, or AI engineering operator?

## P. Public cases, community, and software economics

91. Which three projects best prove the method rather than merely proving that AI can write code?
92. Which metrics, failures, and artifacts can be public, and which must be anonymized?
93. Which customer-specific needs were previously uneconomic but are now feasible?
94. How do personalized implementations avoid becoming unupgradeable customer forks?
95. Should the community contribute cases, skills, counterexamples, templates, or research, and what quality gate applies?
96. One year from now, what evidence would show that this GitHub project helped other people?
