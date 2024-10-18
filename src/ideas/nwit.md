---
title: "It Will Never Work in Theory"
template: page
---

From 2011 to 2023,
[*It Will Never Work in Theory*][nwit] tried to bridge the gulf between theory and practice in software engineering
by publishing short summaries of empirical software engineering research and hosting talks by their authors.
[This post-mortem][postmortem] describes that effort and analyzes its failure,
while the current page reprints very short summaries I've posted on Mastodon since NWIT shut down.

1. Leotta et al 2023: "An empirical study to compare three web test automation approaches: NLP-based, programmable, and capture&replay" <https://onlinelibrary.wiley.com/doi/10.1002/smr.2606> The authors conclude that, "… NLP-based test automation appears to be competitive for small- to medium-sized test suites such as those considered in our empirical study. It minimizes the total cumulative cost (development and evolution) and does not require software testers with programming skills."

1. Suárez & Viscaíno 2023: "Stress, motivation, and performance in global software engineering" <https://onlinelibrary.wiley.com/doi/10.1002/smr.2600> The authors carried out a systematic mapping of 118 published studies dealing with stress, motivation, and performance in global software engineering. The summary didn't have any particular surprises, but I've bookmarked a bunch of references to chase up.

1. Kritikos & Stamelos 2023: "A resilience-based framework for assessing the evolution of open source software projects" <https://onlinelibrary.wiley.com/doi/10.1002/smr.2597> The authors adapt a city resilience framework from urban studies to assess the resilience of open source software projects. I don't know nearly enough to judge the results, but it's an interesting idea.

1. Grabinger et al 2023: "On the perception of graph layouts" <https://onlinelibrary.wiley.com/doi/10.1002/smr.2599> uses eye tracking to explore how programmers look at graphs (which in turn has implications for how we ought to lay them out)

1. Tan et al 2024: "How to Gain Commit Rights in Modern Top Open Source Communities?" <https://arxiv.org/abs/2405.01803>

1. Sun et al 2024: "AI Coders Are Among Us: Rethinking Programming Language Grammar Towards Efficient Code Generation" <https://arxiv.org/abs/2404.16333> Designs a new grammar for Python that maintains the same AST for backward compatibility but reduces token usage for LLMs. I'm still deeply ambivalent about LLMs for coding, but I think we're going to see a lot more of pre-existing tools being reshaped so that they work better.

1. Forward et al 2024: "Super Mario in the Pernicious Kingdoms: Classifying Glitches in Old Games" <https://arxiv.org/abs/2404.14870> This fun little paper uses a simple taxonomy of security errors to categorize glitches in Super Mario games. It won't change your life, but it was a fun read.

1. Molléri 2024: "Who's Actually Being Studied? A Call for Population Analysis in Software Engineering Research" <https://arxiv.org/abs/2404.15093> This short paper highlights shortcomings in the way empirical software engineering studies choose their subjects and then over-generalize their results.

1. Salerno et al 2024: "Open Source Software Development Tool Installation: Challenges and Strategies For Novice Developers" <https://arxiv.org/abs/2404.14637> In my experience, getting started is the biggest obstacle most people face with new software tools (open or otherwise); I hope work like this will help change that.

1. Meng et al 2024: "Program Environment Fuzzing" <https://arxiv.org/abs/2404.13951> This is cool: "record all observed environmental interactions at the kernel/user-mode boundary in the form of system calls. Next, we replay the program under the original recorded interactions, but this time with selective mutations applied, in order to get the effect of different program environments." The authors found 33 zero-day bugs and 14 CVEs were assigned.

1. de Souza Santos et al 2024: "Exploring Hybrid Work Realities: A Case Study with Software Professionals From Underrepresented Groups" <https://arxiv.org/abs/2404.13462> "we analyzed the experiences of neurodivergents, LGBTQIA+ individuals, and people with disabilities…Hybrid work is preferred by software professionals from underrepresented groups in the post-pandemic era. Advantages include improved focus at home, personalized work setups, and accommodation for health treatments."

1. Patrick et al 2024: "The Code the World Depends On: A First Look at Technology Makers' Open Source Software Dependencies" <https://arxiv.org/abs/2404.11763> openssl and zlib are at the top of the rankings; I was surprised that telecoms was so low when results were analyzed by industry sector (table 2).

1. McCormack et al 2024: "A Study of Undefined Behavior Across Foreign Function Boundaries in Rust Libraries" <https://arxiv.org/abs/2404.11671> "Most of these errors were caused by incompatible aliasing and initialization patterns, incorrect foreign function bindings, and invalid type conversion. The majority of aliasing violations were caused by unsound operations in Rust, but they occurred in foreign code."

1. Deiner & Fraser: "NuzzleBug: Debugging Block-Based Programs in Scratch" <https://arxiv.org/abs/2309.14465> "NuzzleBug is an interrogative debugger [for Scratch] that enables to ask questions about executions and provides answers explaining the behavior in question." cool tool - I don't know if I'm ever going to get to teach kids again, but if I do, I want to give this a try.

1. Murphy-Hill et al 2024: "GenderMag Improves Discoverability in the Field, Especially for Women" <https://cmustrudel.github.io/papers/icse24gendermag.pdf> "… by combining self-reported gender data from tens of thousands of users…with software logs gathered over a five-year period, we show that GenderMag helped a team at Google (a) correctly identify discoverability as a usability barrier more likely to affect women than men, and (b) increase discoverability by 2.4x while also achieving gender parity."

1. Trinkenreich et al 2024: "Unraveling the Drivers of Sense of Belonging in Software Delivery Teams" <https://www.ime.usp.br/~gerosa/papers/ICSE_2024___Belonging.pdf> This one looks really interesting, but I'm going to wait until I'm less feverish before trying to understand its statistical methods.

1. Etemadi et al 2024: "Augmenting Diffs With Runtime Information" <https://arxiv.org/abs/2212.11077> This paper presents a tool that compares the program states of old and new versions of code in order to identify unique variable values and adds that to the source code diff to help developers understand the impact of changes.

1. El Haji et al 2024: "Using GitHub Copilot for Test Generation in Python" <https://carolin-brandt.de/publications/elhaji-ast24.pdf> "…within an existing test suite, approximately 45.28% of the tests generated by Copilot are passing tests; 54.72% of generated tests are failing, broken, or empty tests. Furthermore, if we generate tests using Copilot without an existing test suite in place, we observe that 92.45% of the tests are failing, broken, or empty tests."

1. Bogdan & Malavolta: "An Empirical Study on the Impact of CSS Prefixes on the Energy Consumption and Performance of Mobile Web Apps" <https://www.ivanomalavolta.com/files/papers/mobilesoft_2024_css_prefixes.pdf> "CSS prefixes do not lead to an observable impact on the energy consumption of the measured Web apps, while their absence leads to a statistically significant increase of CPU usage in all browsers. The presence of CSS prefixes has a statistically significant negative impact on the loading time in all browsers and devices."

1. Jin et al 2024: "Impact of Extensions on Browser Performance: An Empirical Study on Google Chrome" <https://arxiv.org/abs/2404.06827> The most interesting thing in this paper for me was the authors' use of energy consumption as a metric on an equal footing with page load time.

1. Hyrynsalmi et al 2024: "Bridging Gaps, Building Futures: Advancing Software Developer Diversity and Inclusion Through Future-Oriented Research" <https://arxiv.org/abs/2404.07142> "we present insights from SE researchers and practitioners on challenges and solutions regarding diversity and inclusion in SE. Based on these findings, we share potential utopian and dystopian visions of the future and provide future research directions and implications for academia and industry"

1. Osborne 2024: "Public-private funding models in open source software development: A case study on scikit-learn" <https://arxiv.org/abs/2404.06484> A useful exploration of an open source success story that will be of interest to anyone trying to make their own OS project financially sustainable.

1. Storey et al 2024: "Guidelines for Using Mixed and Multi Methods Research in Software Engineering" <https://arxiv.org/abs/2404.06011A> useful starting point for people like me who want to understand where empirical findings come from and how to get answers ourselves.

1. Fan et al 2024: "The Impact of Sanctions on GitHub Developers and Activities" <https://arxiv.org/abs/2404.05489> "In 2019, GitHub restricted access to certain services for users in specific locations but rolled back these restrictions for some communities (e.g., the Iranian community) in 2021. We conducted a large-scale empirical study, collecting approximately 156 thousand user profiles and their 41 million activity points from 2008 to 2022, to understand the response of developers."

1. Ma et al 2024: "How to Teach Programming in the AI Era? Using LLMs as a Teachable Agent for Debugging" <https://arxiv.org/abs/2310.05292> "We introduce a novel system to facilitate deliberate practice on debugging, where human novices play the role of Teaching Assistants and help LLM-powered teachable agents debug code…students focus on hypothesizing the cause of code errors, while adjacent skills like code completion are offloaded to LLM-agents."

1. Assad et al 2024: "Can My Microservice Tolerate an Unreliable Database? Resilience Testing with Fault Injection and Visualization" <https://arxiv.org/abs/2404.01886>.

1. Jovanovic and Sullivan: "Right or Wrong—Understanding How Novice Users Write Software Models" <https://arxiv.org/abs/2402.06624>.

1. Ben Braiek and Khomh: "Machine Learning Robustness: A Primer" <https://arxiv.org/abs/2404.00897>.

1. Lee et al 2024: "Towards Optimizing Performance-Resource Trade-Off for Serverless Functions" We propose the first differentiated scheduler for runtime cold start mitigation by optimizing serverless function provision. Experiments demonstrate success in optimizing serverless function provision: reducing the 75th-percentile cold start rates by 49.77% and the wasted memory time by 56.43%, compared to the state-of-the-art. <https://arxiv.org/abs/2403.17574>

1. Rahman et al 2024: "Characterizing Dependency Update Practice of NPM, PyPI and Cargo Packages" We find that PyPI packages update dependencies faster than NPM and Cargo. Conversely, Cargo packages update their vulnerable dependencies faster than NPM and PyPI. <https://arxiv.org/abs/2403.17382>

1. Gunatilake et al 2024: "Enablers and Barriers of Empathy in Software Developer and User Interactions: A Mixed Methods Case Study" <https://dl.acm.org/doi/10.1145/3641849>

1. Sülün et al 2024: "An Empirical Analysis of Issue Templates Usage in Large-Scale Projects on GitHub" <https://dl.acm.org/doi/10.1145/3643673>

1. Nam et al 2024: "Understanding Documentation Use Through Log Analysis: An Exploratory Case Study of Four Cloud Services" <https://arxiv.org/abs/2310.10817> " By analyzing page-view logs for over 100,000 users…we show that which documentation pages people visit often correlates with user characteristics such as past experience with the specific product, on the one hand, and with future adoption of the API on the other hand."

1. Stray et al 2024: "The Agile Coach Role: Coaching for Agile Performance Impact" <https://arxiv.org/abs/2010.15738> Reports results from semi-structured interviews with 19 agile coaches at 10 different companies. No big surprises, but it's nice to see this increasingly influential role put under the microscope.

1. Florath 2024: "LLM Interactive Optimization of Open Source Python Libraries -- Case Studies and Generalization" <https://arxiv.org/abs/2312.14949> "We find that contemporary LLM ChatGPT-4 is surprisingly adept at optimizing energy and compute efficiency. However, this is only the case in interactive use, with a human expert in the loop."

1. Sesari et al 2024: "Understanding Fairness in Software Engineering: Insights from Stack Exchange" <https://arxiv.org/abs/2402.19038> "The majority of fairness discussions revolve around the topic of income… Further…while not discussed as often, discussions on fairness in recruitment tend to receive the highest number of views and scores."

1. da Gião et al 2024: "Chronicles of CI/CD: A Deep Dive into its Usage Over Time" <https://arxiv.org/abs/2402.17588> Usage of CI/CD is tied to language (which may reflect developer age cohorts), and a surprising number of projects use multiple CI/CD technologies.

1. New paper by Druskat et al on the quality and reliability of datasets collecting mentions of software in scientific papers is depressing reading: <https://arxiv.org/abs/2402.14602> What makes it even more depressing is that _this_ is the data AI models are being trained on...

1. Calefato et al: "A Lot of Talk and a Badge: An Exploratory Analysis of Personal Achievements in GitHub" <https://arxiv.org/abs/2303.14702> 1. Most developers have at least a badge, but an increasing number of users choose to keep their profile private and opt out of displaying badges. 2. Badges are generally poorly correlated with developers' timeliness and desire to collaborate. 3. Except for the Starstruck badge (reflecting the number of followers), badges' introduction does not have an effect.

1. Ehsani et al 2024: "Incivility in Open Source Projects" presents a dataset of 404 locked GitHub issue discussion threads and 5961 individual comments from 213 OSS projects. "Bitter frustration", "Impatience", and "Mocking" are the most prevalent features in the dataset; the most common triggers, targets, and consequences of incivility include "Failed use of tool/code or error messages", "People", and "Discontinued further discussion", respectively. <https://preethac.github.io/files/MSR24_Incivility_Dataset.pdf>

1. Islam et al 2024: "Characterizing Python Library Migrations" <https://arxiv.org/abs/2207.01124> The authors manually label 3096 migration-related changes in 335 Python library migrations from 311 repositories [and] derive a taxonomy for migration-related changes. Among other things, they find that 40% of library pairs have API mappings that involve non-function program elements, while most library migration techniques assume function calls from the source will map into function calls from the target.

1. Erni et al 2024: "SBFT Tool Competition 2024 -- Python Test Case Generation Track" <https://arxiv.org/abs/2401.15189> Reports a head-to-head comparison of four Python test case generators (UTBotPython, Klara, Hypothesis Ghostwriter, and Pynguin) and describes the challenges of running such experiments.

1. Schorlemmer et al 2024: "Signing in Four Public Software Package Registries: Quantity, Quality, and Influencing Factors" <https://arxiv.org/abs/2401.14635> This paper looks at the nature of signed artifacts, current quantity and quality of signatures, and longitudinal trends in signing practices for Maven, PyPi, DockerHub, and HuggingFace.

1. Franke et al 2024: "A First Look at the General Data Protection Regulation (GDPR) in Open-Source Software" reports a survey of 47 open source developers' experience with GDPR compliance. <https://arxiv.org/abs/2401.14629>

1. Zhang et al 2024: "Machine Learning Systems are Bloated and Vulnerable" <https://arxiv.org/abs/2212.09437> "We analyze and quantify bloat in machine learning containers… Through experimentation with 15 machine learning containers from TensorFlow, PyTorch, and Nvidia, we show that bloat accounts for up to 80% of machine learning container sizes, increasing container provisioning times by up to 370% and exacerbating vulnerabilities by up to 99%."

1. Zhang et al 2024: "How Are Paid and Volunteer Open Source Developers Different? A Study of the Rust Project" <https://arxiv.org/abs/2401.13940> "We find that core paid developers tend to contribute more frequently; commits contributed by one-time paid developers have bigger sizes; peripheral paid developers implement more features; and being paid plays a positive role in becoming a long-term contributor. We also find that volunteers do have some prejudices against paid developers."

1. Birillo et al 2024: "IDEs as Interactive Learning Platforms" <https://arxiv.org/abs/2401.14284> Describes a plugin for JetBrains IDEs that offers the usual suspects (course outline, multiple choice questions, run-and-check) inside the IDE. Doesn't appear to drive the IDE to (for example) show learners how to use a breakpointing debugger or the refactoring tools, and doesn't appear to have any support for lesson discovery.

1. Champion & Mako Hill: "Sources of Underproduction in Open Source Software" <https://arxiv.org/abs/2401.11281> Open source software is often underproduced: its relative quality is lower than its relative importance. This paper examines underproduction in Debian. It finds that software age and programming language age are partly responsible, but the association is weaker in older languages. Also, more contributors is associated with higher underproduction risk, but maintainer turnover is not.

1. de Souza Santos and Gama 2024: "Hidden Populations in Software Engineering: Challenges, Lessons Learned, and Opportunities" <https://arxiv.org/abs/2401.09608> This paper discusses the authors' experiences and lessons learned while conducting multiple studies involving hidden, marginalized, and underrepresented populations in software engineering.

1. Malviya-Thakur and Mockus 2024: "The Role of Data Filtering in Open Source Software Ranking and Selection" <https://arxiv.org/abs/2401.10136> Most projects study a subset of public open source projects, but how does subsetting affect findings? This paper randomly samples 100K repositories and uses multiple regression to model the number of stars based on tseveral fcators. It finds filtering significantly alters results, and recommends using either complete data or stratified sampling to avoid bias.

1. Tiwari et al 2024: "With Great Humor Comes Great Developer Engagement" <https://arxiv.org/abs/2312.01680> "We collect…data about humorous elements present in three significant, real-world software projects… [and] receive unique insights from 125 developers. Our analysis…highlights the prevalence of humor in software… When practiced responsibly, humor increases developer engagement… [S]oftware tests and documentation are the best locations in code to practice humor."

1. Amit et al 2024: "Which Code Smells are Worth Chasing?" <https://arxiv.org/abs/2103.01861> "We evaluated the smells in 31,687 Java files from 677 GitHub repositories…We measured the influence of smells on four metrics for quality, productivity, and bug detection efficiency. Out of 151 code smells computed by the CheckStyle smell detector, less than 20% were found to be potentially causal, and only a handful are rather robust."

1. Madugalla et al 2024: "Engineering Adaptive Information Graphics for Disabled Communities: A Case Study with Public Space Indoor Maps" <https://arxiv.org/abs/2401.05659> "Our research [develops] a framework that generates adaptive and accessible information graphics for multiple disabilities. Uniquely, the approach also serves people with multiple simultaneous disabilities…people with low vision, colour blindness, dyslexia and mobility impairment."

1. Wang & Lopez Moreno 2024: "Version Control of Speaker Recognition Systems" <https://arxiv.org/abs/2007.12069> This paper discusses the practical engineering challenges of version control of models and user profiles based on strategies for speaker recognition systems at Google. These strategies are categorized into device-side deployment, server-side deployment, and hybrid deployment and compared using SpeakerVerSim, a Python simulation framework. 

1. Peng et al: "Less is More? An Empirical Study on Configuration Issues in Python PyPI Ecosystem" <https://arxiv.org/abs/2310.12598> "To evaluate the effectiveness o current automatic dependency inference approaches, we build a benchmark[…]identify 15 kinds of configuration issues and find that 183,864 library releases suffer from potential configuration issues. Remarkably, 68% of these issues can only be detected via the source-level check."

1. Cheong et al: "Ethical Considerations Towards Protestware" <https://arxiv.org/abs/2306.10019> "Using different frameworks commonly used in AI ethics, we illustrate how an open-source maintainer's decision to protest is influenced by different stakeholders (viz., their membership in the OSS community, their personal views, financial motivations, social status, and moral viewpoints), making protestware a multifaceted and intricate matter."

1. Boteju et al 2024: "Demystifying Privacy Enhancing Technologies Through the Lens of Software Developers" <https://arxiv.org/abs/2401.00879> This paper reviews 39 studies of developers' privacy-enhancing practices, from pseudonymisation and onion routing to zero-knowledge proofs. I've only ever implemented one of the techniques they look at in a 40-year career.

1. Winter et al 2023: "Error Propagation Analysis for Multithreaded Programs: An Empirical Approach" looks at how well automatically-inferred invariants in programs can be used in lieu of fault-free runs of multithreaded programs for error propagation analysis. <https://arxiv.org/abs/2312.16791>

1. Hajari et al 2023: "Factoring Expertise, Workload, and Turnover into Code Review Recommendation" looks at ways of recommending reviewers to mitigate loss of knowledge resulting from developer turnover. <https://arxiv.org/abs/2312.17236>

1. Chen et al 2023: Why Not Mitigate Vulnerabilities in Helm Charts? "We conduct a mixed-methods study on 11,035 Helm Charts affected by 10,982 fixable vulnerabilities…the complexity of a Chart correlates with the number of vulnerabilities, and the official Charts do not contain fewer vulnerabilities compared to unofficial Charts…The use of automated [mitigation] strategies is low as automation has…a high number of false positives…" <https://arxiv.org/abs/2312.15350>

1. Florath & Kiraly 2023: LLM Interactive Optimization of Open Source Python Libraries–Case Studies and Generalization. "We find that contemporary LLMs… are surprisingly adept at optimizing energy and compute efficiency. However, this is only the case…with a human expert in the loop…Nonetheless, we were surprised by how few iterations were required to achieve substantial performance improvements that were not obvious to the expert in the loop." <https://arxiv.org/abs/2312.14949>

1. Guenes et al: "Impostor Phenomenon in Software Engineers" <https://arxiv.org/abs/2312.03966>

1. Gao et al 2023: '"Add more config detail": A Taxonomy of Installation Instruction Changes'. <https://arxiv.org/abs/2312.03250> Having every student team in an undergrad software engineering class try to install and run every other team's software using only the instructions in the latter's README would be an interesting exercise :-)

1. Dinh et al 2023: "Large Language Models of Code Fail at Completing Code with Potential Bugs" <https://arxiv.org/abs/2306.03438>

1. Li et al: "Exploring Multi-Programming-Language Commits and Their Impacts on Software Quality: An Empirical Study on Apache Projects" finds, among other things, that issues in multi-programming-language commits take significantly longer to be resolved and introduce more bugs than commits in a single programming language. <https://arxiv.org/abs/2311.08424> As much as I like Python, I gotta say, TypeScript front and back is looking pretty compelling…

1. Sajadi et al: "Interpersonal Trust in OSS: Exploring Dimensions of Trust in GitHub Pull Requests" The authors investigate various dimensions of trust to identify the ways trusting behavior can be observed in OSS, then sample a set of 100 GitHub pull requests from Apache Software Foundation projects, to analyze and demonstrate how each dimension of trust can be exhibited. I think handbooks for software engineering teams have to include ideas like these to be useful. <https://arxiv.org/abs/2311.04767v1>

1. Saavedra et al: "GitBug-Actions: Building Reproducible Bug-Fix Benchmarks with GitHub Actions" is a neat idea—the authors mine GitHub Actions to detect bug fixes, then use that data to build a benchmark suite for automatic program repair and fault localization tools. <https://arxiv.org/abs/2310.15642>

1. Butler et al: "Objectives and Key Results in Software Teams: Challenges, Opportunities and Impact on Development" finds (among other things) that "…tracking, measuring and setting goals is hard work, regardless of tools used. Middle management seems to be a critical component of the translation of lofty goals to actionable work items." <https://arxiv.org/abs/2311.00236>

1. Feldman et al: "On the Relationship between Code Verifiability and Understandability" <https://arxiv.org/abs/2310.20160> "Proponents of software verification have argued that simpler code is easier to verify…We empirically validate this by comparing the number of warnings produced by four verification tools on 211 snippets of Java code with 20 metrics of code comprehensibility from human subjects… Our experiments…show a small correlation (r = 0.23) between understandability and verifiability."

1. Narayanan et al 2023: "Diversity in Software Engineering Conferences and Journals" Some software engineering conferences and journals are slowly becoming more inclusive ethnically, but all of the ones studied have become worse on gender. <https://arxiv.org/abs/2310.16132>

1. Yan et al: "GitHub OSS Governance File Dataset" <https://arxiv.org/abs/2304.00460> presents a dataset of 710 GitHub-hosted OSS projects with explicit governance description files. Lots of useful here...

1. Peng et al: "Less is More? An Empirical Study on Configuration Issues in Python PyPI Ecosystem" <https://arxiv.org/abs/2310.12598> describes a source-level checker for Python configuration issues that seems to be a significant advance over previous approaches. Packaging remains Python's biggest sore spot; it might be too late to fix it, but work like this might make it hurt less.

1. Wyrich: "Source Code Comprehension: A Contemporary Definition and Conceptual Model for Empirical Investigation" what we mean by "understanding a program" has changed significantly over 50 years; this paper traces how and why (and is relevant to LLMs in lots of ways) <https://arxiv.org/abs/2310.11301>

1. Di Cosmo and Zacchiroli: "The Software Heritage Open Science Ecosystem" <https://arxiv.org/abs/2310.10295> describes an incredibly useful resource for empirical studies of software that is itself a pretty major piece of engineering.

1. Huang et al: "Detecting and Fixing Violations of Modification Terms in Open Source Licenses during Forking" <https://arxiv.org/abs/2310.07991>

1. Nitin et al: "Yuga: Automatically Detecting Lifetime Annotation Bugs in the Rust Language" From the abstract: "Yuga successfully detects bugs with good precision on these datasets, and we make the code and datasets publicly available for review." <https://arxiv.org/abs/2310.08507>

1. Ma et al.: "HypoCompass: Large-Language-Model-based Tutor for Hypothesis Construction in Debugging for Novices" From the abstract: "Hypothesis construction in debugging is rarely taught due to a lack of explicit instruction. In this work, we explore whether LLMs can be used to train novices on hypothesis construction…" I think this is a really interesting use case for LLMs: ask me if I've checked for X or why I think Y might be wrong. <https://arxiv.org/abs/2310.05292>

1. Ye et al: "PreciseBugCollector: Extensible, Executable and Precise Bug-fix Collection" <https://arxiv.org/abs/2309.06229> From the abstract: "Bug datasets are vital for enabling deep learning techniques to address software maintenance tasks related to bugs. However, existing bug datasets…are either small-scale but precise…or large-scale but imprecise… In this paper, we introduce PreciseBugCollector, a precise, multi-language bug collection approach that overcomes these two limitations."

1. Fu et al: "Security Weaknesses of Copilot Generated Code in GitHub" finds (1) 35.8% of Copilot generated code snippets contain CWEs, (2) the security weaknesses are diverse and related to 42 different CWEs, in which CWE-78: OS Command Injection, CWE-330: Use of Insufficiently Random Values, and CWE-703: Improper Check or Handling of Exceptional Conditions occurred the most frequently, and (3) 11 of those belong to the currently recognized 2022 CWE Top-25. <https://arxiv.org/abs/2310.02059>

1. "40 Years of Designing Code Comprehension Experiments: A Systematic Mapping Study" by Wyrich et al is a great look back at how people have tried to measure the readability and comprehensibility of code 1979–2019. If you are building any kind of programming support tools or experimenting with LLMs for programmers, this is a great introduction to how people have tried to build goalposts in the past to evaluate success (or otherwise). <https://arxiv.org/abs/2206.11102>

1. Huang et al: "Bias Assessment and Mitigation in LLM-based Code Generation" looks at the degree to which different prompts to nine different LLM-based code generators produce answers biased on age, race, sex, gender, etc. <https://arxiv.org/abs/2309.14345>

1. Deiner and Fraser: "NuzzleBug: Debugging Block-Based Programs in Scratch" presents an extension of the Scratch block-based environment that provides better debugging support. <https://arxiv.org/abs/2309.14465>

1. Melegati and Guera: "DAnTE: a taxonomy for the automation degree of software engineering tasks" describes several levels of automation in software engineering, then uses that classification scheme to try to figure out where LLMs might be of use. <https://arxiv.org/abs/2309.14903>

1. Casseau et al: "MOON: Assisting Students in Completing Educational Notebook Scenarios" presents a mini-language for teachers using Jupyter notebooks that enables them to formalize the expected usage of those notebooks. <https://arxiv.org/abs/2309.16201>

1. Uyaguari et al: "Relevant information in TDD experiment reporting" Studies of test-driven development exemplify both the promise of empirical software engineering research (does this widely-advocated technique actually make a difference?) and the field's shortcomings (many published studies are shaky, and few practitioners know they exist). Careful, cautious, incremental papers like this won't make Hacker News, but are essential precisely because of that. <https://arxiv.org/abs/2406.06405>

1.  Baltes & Ralph 2024: "Teaching Literature Reviewing for Software Engineering Research" <https://arxiv.org/abs/2406.08369> and Treude 2024: "Qualitative Data Analysis in Software Engineering: Techniques and Teaching Insights" <https://arxiv.org/abs/2406.08228> - I wish I'd had these 15 years ago when I had graduate students.

1.  Straubinger et al 2024: "Acknowledging Good Java Code with Code Perfumes" <https://arxiv.org/abs/2406.16348> Instead of a tool that complains about code smells, the authors use one that praises things students have done well. "Our evaluation shows…programs with more code perfume instances tend to have better functionality and readability [and] students who incorporate more code perfumes tend to achieve higher grades. Thus, code perfumes serve as a valuable tool to acknowledge learners' successes…"

1.  Syukron et al: "A Comprehensive Study of Disaster Support Mobile Apps" <https://arxiv.org/abs/2407.08145> "We identified 13 key features in these apps and categorised them in to the 4 stages of disaster life cycle. We provide a set of practical recommendations for future disaster app developers."

1.  Castor 2024: "Estimating the Energy Footprint of Software Systems: a Primer" <https://arxiv.org/abs/2407.11611> "We talk about how the energy footprint of a software system can be estimated to support Green Software Development. Our focus is on general concepts and approaches and not on specific tools, although we do refer to some of them to make explanations more concrete. This document aims to be a starting point for researchers who want to start conducting work in this area."

1.  Gordillo & López-Fernández 2024: "Are Educational Escape Rooms More Effective Than Traditional Lectures for Teaching Software Engineering? A Randomized Controlled Trial" <https://arxiv.org/abs/2407.12355> "…students who learned software modeling through the educational escape room had very positive perceptions toward this activity, significantly increased their knowledge, and outperformed those students who learned through a traditional lecture in terms of knowledge acquisition."

1.  Brown & Cusati 2024: "Exploring the Evidence-Based Beliefs and Behaviors of LLM-Based Programming Assistants" <https://arxiv.org/abs/2407.13900> "We investigate 17 evidence-based claims by empirical SE research across five LLM-based programming assistants. Our findings show that [they] have ambiguous beliefs regarding research claims, lack credible evidence to support responses, and are incapable of adopting practices demonstrated by empirical SE research to support development tasks."

1.  Shaw & Petre: "Design Spaces and How Software Designers Use Them: a sampler" <https://arxiv.org/abs/2407.18502> Two of my favorite software engineering researchers present, "…a sampling of what designers, especially software designers, mean when they say "design space" and provide examples of the roles their design spaces serve in their design activity."

1.  Frattini et al 2024: "Crossover Designs in Software Engineering Experiments: Review of the State of Analysis" <https://arxiv.org/abs/2408.07594> "…despite the explicit guidelines, only 29.5% of all threats to validity were addressed properly."

1.  Zhong et al 2024: "An Empirical Study on Package-Level Deprecation in Python Ecosystem" <https://arxiv.org/abs/2408.10327> "75.4% of inactive package developers have no intention of releasing deprecation declarations for various reasons, while 89.5% of users express a desire to be notified about the deprecation"

1.  Sáinz-Pardo Díaz & López García 2024: "An Open Source Python Library for Anonymizing Sensitive Data" <https://arxiv.org/abs/2408.10766> (package at <https://pypi.org/project/anjana/>) I'm not qualified to assess their statistics, but I'm grateful to see work like this.

1.  Bhatia et al 2024: "Data Quality Antipatterns for Software Analytics" <https://arxiv.org/abs/2408.12560> "We identified 8 types and 14 sub-types of ML-specific data quality antipatterns  [and] conducted experiments to determine the prevalence of these antipatterns, assess how cleaning order affects model performance, evaluate the impact of antipattern removal on performance, and examine the consistency of interpretation from models built with different antipatterns."

1.  Aranda et al 2024: "Effect of Requirements Analyst Experience on Elicitation Effectiveness" <https://arxiv.org/abs/2408.12538> "In unfamiliar domains, interview, requirements, development, and professional experience does not influence analyst effectiveness. In familiar domains, effectiveness varies depending on the type of experience. Interview experience has a strong positive effect, whereas professional experience has a moderate negative effect."

1.  Guégain et al 2024: "Exploring Performance Trade-offs in JHipster" <https://arxiv.org/abs/2409.16480> Analyzes the ways in which different configuration settings in a Java full-stack web platform affect its performance.

1.  Beau and Crabbé 2024: "CodeInsight: A Curated Dataset of Practical Coding Solutions from Stack Overflow" <https://arxiv.org/abs/2409.16819> Describes a curated set of 3400 examples of Python code that can be used to fine-tune and evaluate generative models (available online at <https://github.com/NathanaelBeau/CodeInsight>).

1.  Fan et al 2024: "Developer Reactions to Protestware in Open Source Software: The cases of color.js and es5.ext" <https://arxiv.org/abs/2409.15674> An in-depth analysis of how open source communities reacted to two specific instances of software-as-protest.

1.  Nierstrasz and Girba 2024: "Moldable Development Patterns" <https://arxiv.org/abs/2409.18811> explores a better world programmers could have.

1.  Amjad et al 2024: "Accessibility Issues in Ad-Driven Web Applications" <https://arxiv.org/abs/2409.18590> 67% of websites experience increased accessibility violations due to ads; what's worse, user-identifiable data is collected on 94% of websites through interactions that people using disability aids require.

1.  Gorostidi et al 2024: "On the Creation of Representative Samples of Software Repositories" <https://arxiv.org/abs/2410.00639> We present a methodology for creating representative samples of software repositories, where such representativeness is properly aligned with both the characteristics of the population of repositories and the requirements of the empirical study.

1.  Casanueva et al 2024: "The Impact of the COVID-19 Pandemic on Women's Contribution to Public Code" <https://arxiv.org/abs/2410.01454> Findings show that the COVID-19 pandemic has disproportionately impacted women's ability to contribute to the development of public code, relatively to men. Further, our observations of specific contributor subgroups indicate that COVID-19 particularly affected women hobbyists…

1.  Sesari et al 2024: "It is Giving Major Satisfaction" <https://arxiv.org/abs/2410.02482> …distributive, procedural, interpersonal, and informational [fairness] significantly affect…overall job satisfaction and satisfaction with job security…interpersonal fairness has the biggest impact, being more than twice as influential on overall job satisfaction. The relationship …is notably stronger for female, ethnically underrepresented, less experienced practitioners, and those with work limitations.

1.  Olson et al 2024: "Crossing Margins: Intersectional Users' Ethical Concerns about Software" <https://arxiv.org/abs/2410.08090> Worth reading for the methodology as well as the findings - makes me think yet again about how hard it would be to put together an undergrad course on empirical methods in software engineering, and how valuable such a course would be.

1.  Schesh et al 2024: "Evaluation of Version Control Merge Tools" <https://arxiv.org/abs/2410.09934> I've wanted usable diff-and-merge tools for non-textual files for decades; hopefully this systematic evaluation of alternatives for text files will be a step in that direction.

1.  Birillo et al 2024: "One Step at a Time: Combining LLMs and Static Analysis to Generate Next-Step Hints for Programming Tasks" <https://arxiv.org/abs/2410.09268> Computing ed researchers have been studying the value of labeled subgoals for years; this paper looks at how well AI tools can generate them on the fly to help novices take their next step.

1.  Dorner et al 2024: "The Upper Bound of Information Diffusion in Code Review" <https://arxiv.org/abs/2306.08980> "…code review participants…can spread information to between 72% and 85% of all…participants within four weeks; for large…systems, we found…about 11000 reachable participants…information can spread between two participants in code review in less than five hops and less than five days."

1.  Xavier 2024: "An evidence-based and critical analysis of the Fediverse decentralization promises" <https://arxiv.org/abs/2408.15383> "Our findings suggest that Fediverse will face significant challenges in fulfilling its decentralization promises, potentially hindering its ability to positively impact the social Web on a large scale."

1.  Spinellis et al 2024: "Broken Windows: Exploring the Applicability of a Controversial Theory on Code Quality" <https://arxiv.org/abs/2410.13480> "Our results show that history matters, that developers behave differently depending on some aspects of the code quality they encounter, and that programming style inconsistency is not necessarily related to structural qualities."

[nwit]: https://neverworkintheory.org/
[postmortem]: https://www.computer.org/csdl/magazine/so/5555/01/10424425/1Ulj1Qa8tJ6
