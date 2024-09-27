---
title: "June 2020 Papers"
date: 2020-06-20
---

I just downloaded 30 papers from ICSE 2020 that are
(a) more interesting and useful than 90% of what's in the undergrad SE textbooks I've read
and (b) probably won't make it onto most programmers' radar for years, if ever.
I've included titles, links and abstracts below,
and have two requests and an observation:

1.  Please make an open access copy of your paper really (really) easy to find.
    A paywall is about as welcoming as a rasied middle finger:
    if I have to resort to SciHub,
    I'm going to assume you don't really want me to read your paper.
    (I've left 7 good ones off this list for this reason.)

2.  Please make the DOI for your paper really, really easy to find,
    and put the abstract online as well.
    [doi2bib](https://www.doi2bib.org/) is one of the most useful little things on the internet;
    if anyone ever builds doi2abstract, I will do my utter best to have them canonized.

3.  I will bet my entire stock of programming books that
    the average undergraduate in biology or geology knows more
    about current research questions and methods in their field
    than the average computer science undergraduate does about questions and methods in software engineering research.
    Until we close that gap,
    I think software engineering research will continue to chase practice rather than lead it,
    and will continue to be (mostly) ignored by the people it's supposed to help.

There are lots of other good papers on [the conference site](https://conf.researchr.org/home/icse-2020);
many lie outside my areas of interest and expertise,
but are well worth reading.

## Claes and Mäntylä: [20-MAD - 20 Years of Issues and Commits of Mozilla and Apache Development](https://arxiv.org/pdf/2003.14015.pdf)

Data of long-lived and high profile projects is valuable for research on successful software engineering in the wild. Having a dataset with different linked software repositories of such projects, enables deeper diving investigations. This paper presents 20-MAD, a dataset linking the commit and issue data of Mozilla and Apache projects. It includes over 20 years of information about 765 projects, 3.4M commits, 2.3M issues, and 17.3M issue comments, and its compressed size is over 6 GB. The data contains all the typical information about source code commits (e.g., lines added and removed, message and commit time) and issues (status, severity, votes, and summary). The issue comments have been pre-processed for natural language processing and sentiment analysis. This includes emoticons and valence and arousal scores. Linking code repository and issue tracker information, allows studying individuals in two types of repositories and provide more accurate time zone information for issue trackers as well. To our knowledge, this the largest linked dataset in size and in project lifetime that is not based on GitHub. 

## Dey et al: [Detecting and Characterizing Bots that Commit Code](https://arxiv.org/pdf/2003.03172.pdf)

**Background**: Some developer activity traditionally performed manually, such as making code commits, opening, managing, or closing issues is increasingly subject to automation in many OSS projects. Specifically, such activity is often performed by tools that react to events or run at specific times. We refer to such automation tools as bots and, in many software mining scenarios related to developer productivity or code quality it is desirable to identify bots in order to separate their actions from actions of individuals.

**Aim**: Find an automated way of identifying bots and code committed by these bots, and to characterize the types of bots based on their activity patterns.

**Method and Result**: We propose BIMAN, a systematic approach to detect bots using author names, commit messages, files modified by the commit, and projects associated with the ommits. For our test data, the value for AUC-ROC was 0.9. We also characterized these bots based on the time patterns of their code commits and the types of files modified, and found that they primarily work with documentation files and web pages, and these files are most prevalent in HTML and JavaScript ecosystems. We have compiled a shareable dataset containing detailed information about 461 bots we found (all of whom have more than 1000 commits) and 13,762,430 commits they created. 

## Durieux et al: [Empirical Study of Restarted and Flaky Builds on Travis CI](https://arxiv.org/pdf/2003.11772.pdf)

Continuous Integration (CI) is a development practice where developers frequently integrate code into a common codebase. After the code is integrated, the CI server runs a test suite and other tools to produce a set of reports (e.g., output of linters and tests). If the result of a CI test run is unexpected, developers have the option to manually restart the build, re-running the same test suite on the same code; this can reveal build flakiness, if the restarted build outcome differs from the original build. In this study, we analyze restarted builds, flaky builds, and their impact on the development workflow. We observe that developers restart at least 1.72% of builds, amounting to 56,522 restarted builds in our Travis CI dataset. We observe that more mature and more complex projects are more likely to include restarted builds. The restarted builds are mostly builds that are initially failing due to a test, network problem, or a Travis CI limitations such as execution timeout. Finally, we observe that restarted builds have a major impact on development workflow. Indeed, in 54.42% of the restarted builds, the developers analyze and restart a build within an hour of the initial failure. This suggests that developers wait for CI results, interrupting their workflow to address the issue. Restarted builds also slow down the merging of pull requests by a factor of three, bringing median merging time from 16h to 48h. 

## Fang et al: [Need for Tweet: How Open Source Developers Talk About Their GitHub Work on Twitter](https://cmustrudel.github.io/papers/msr20tweets.pdf)

Social media, especially Twitter, has always been a part of the professional lives of software developers, with prior work reporting on a diversity of usage scenarios, including sharing information, staying current, and promoting one’s work. However, previous studies of Twitter use by software developers are generally restricted to surveys or small samples, and typically lack information about activities of the study subjects (and their outcomes) on other platforms. To enable such future research, in this paper we propose a computational approach to cross-linking users on Twitter and GitHub, the dominant platform for hosting open-source development, revealing 70,428 users active on both. As a preliminary analysis of this dataset, we report on a case study of 800 tweets by open-source developers about GitHub work, combining precise automatic characterization of tweet authors in terms of their relationship to the GitHub items linked in their tweets with a deep qualitative analysis of the tweet contents. We find that developers have very distinct behavioral patterns when including GitHub links in their tweets and these patterns are correlated with the relationship between the tweet author and the repository they link to. Based on this analysis, we hypothesize about what might explain such behavioral differences and what the implications of different tweeting patterns could be for the sustainability of GitHub projects.

## Girardi et al: [Recognizing Developers' Emotions while Programming](https://arxiv.org/pdf/2001.09177.pdf)

Developers experience a wide range of emotions during programming tasks, which may have an impact on job performance. In this paper, we present an empirical study aimed at (i) investigating the link between emotion and progress, (ii) understanding the triggers for developers' emotions and the strategies to deal with negative ones, (iii) identifying the minimal set of non-invasive biometric sensors for emotion recognition during programming task. Results confirm previous findings about the relation between emotions and perceived productivity. Furthermore, we show that developers' emotions can be reliably recognized using only a wristband capturing the electrodermal activity and heart-related metrics.

## Gold and Krinke: [Ethical Mining - A Case Study on MSR Mining Challenges](http://www0.cs.ucl.ac.uk/staff/j.krinke/publications/msr20ethics.pdf)

Research in Mining Software Repositories (MSR) is research involving human subjects, as the repositories usually contain data about developers’ interactions with the repositories. Therefore, any research in the area needs to consider the ethics implications of the intended activity before starting. This paper presents a discussion of the ethics implications of MSR research, using the mining challenges from the years 2010 to 2019 as a case study. It highlights problems that one may encounter in creating such datasets, and discusses ethics challenges that may be encountered when using existing datasets. An analysis of 102 accepted papers to the Mining Challenge Track suggests that none had an explicit discussion of ethics considerations. Whilst this does not necessarily mean ethics were not considered, the sparsity of discussion leads us to suggest that the MSR community should at least increase awareness by openly discussing ethicas considerations.

## Han et al: [What do Programmers Discuss about Deep Learning Frameworks](http://das.encs.concordia.ca/uploads/Han2019EMSE.pdf)

Deep learning has gained tremendous traction from the developer and researcher communities. It plays an increasingly significant role in a number of application domains. Deep learning frameworks are proposed to help developers and researchers easily leverage deep learning technologies, and they attract a great number of discussions on popular platforms, i.e., Stack Overflow and GitHub. To understand and compare the insights from these two platforms, we mine the topics of interests from these two platforms. Specifically, we apply Latent Dirichlet Allocation (LDA) topic modeling techniques to derive the discussion topics related to three popular deep learning frameworks, namely, Tensorflow, PyTorch and Theano. Within each platform, we compare the topics across the three deep learning frameworks. Moreover, we make a comparison of topics between the two platforms. Our observations include 1) a wide range of topics that are discussed about the three deep learning frameworks on both platforms, and the most popular workflow stages are Model Training and Preliminary Preparation. 2) the topic distributions at the workflow level and topic category level on Tensorflow and PyTorch are always similar while the topic distribution pattern on Theano is quite different. In addition, the topic trends at the workflow level and topic category level of the three deep learning frameworks are quite different. 3) the topics at the workflow level show different trends across the two platforms. e.g., the trend of the Preliminary Preparation stage topic on Stack Overflow comes to be relatively stable after 2016, while the trend of it on GitHub shows a stronger upward trend after 2016. Besides, the Model Training stage topic still achieves the highest impact scores across two platforms. Based on the findings, we also discuss implications for practitioners and researchers.

## Hilderbrand et al: [Engineering Gender-Inclusivity into Software: Tales from the Trenches](https://arxiv.org/ftp/arxiv/papers/1905/1905.10361.pdf)

Although the need for gender-inclusivity in software itself is gaining attention among both SE researchers and SE practitioners, and methods have been published to help, little has been reported on how to make such methods work in real-world settings. For example, how do busy software practitioners use such methods in low-cost ways? How do they endeavor to maximize benefits from using them? How do they avoid the controversies that can arise in talking about gender? To find out how teams were handling these and similar questions, we turned to 10 real-world software teams. We present these teams experiences "in the trenches," in the form of 12 practices and 3 potential pitfalls, so as to provide their insights to other real-world software teams trying to engineer gender-inclusivity into their software products.

## Ingram and Drachen: [How Software Practitioners Use Informal Local Meetups to Share Software Engineering Knowledge](http://eprints.whiterose.ac.uk/156323/1/HowDevelopersUseInformalLocalNetworks_Final.pdf)

Informal technology "meetups" have become an important aspect of the software development community, engaging many thousands of practitioners on a regular basis. However, although local technology meetups are well-attended by developers, little is known about their motivations for participating, the type or usefulness of information that they acquire, and how local meetups might differ from and complement other available communication channels for software engineering information. We interviewed the leaders of technology-oriented Meetup groups, and collected quantitative information via a survey distributed to participants in technology-oriented groups. Our findings suggest that participants in these groups are primarily experienced software practitioners, who use Meetup for staying abreast of new developments, building local networks and achieving transfer of rich tacit knowledge with peers to improve their practice. We also suggest that face to face meetings are useful forums for exchanging tacit knowledge and contextual information needed for software engineering practice.

## Johnson et al: [Causal Testing: Understanding Defects' Root Causes](https://arxiv.org/pdf/1809.06991.pdf)

Understanding the root cause of a defect is critical to isolating and repairing buggy behavior. We present Causal Testing, a new method of root-cause analysis that relies on the theory of counterfactual causality to identify a set of executions that likely hold key causal information necessary to understand and repair buggy behavior. Using the Defects4J benchmark, we find that Causal Testing could be applied to 71% of real-world defects, and for 77% of those, it can help developers identify the root cause of the defect. A controlled experiment with 37 developers shows that Causal Testing improves participants' ability to identify the cause of the defect from 80% of the time with standard testing tools to 86% of the time with Causal Testing. The participants report that Causal Testing provides useful information they cannot get using tools such as JUnit. Holmes, our prototype, open-source Eclipse plugin implementation of Causal Testing, is available at [this http URL](http://holmes.cs.umass.edu/).

## Karampatsis et al: [Big Code != Big Vocabulary: Open-Vocabulary Models for Source Code](https://arxiv.org/pdf/2003.07914.pdf)

Statistical language modeling techniques have successfully been applied to large source code corpora, yielding a variety of new software development tools, such as tools for code suggestion, improving readability, and API migration. A major issue with these techniques is that code introduces new vocabulary at a far higher rate than natural language, as new identifier names proliferate. Both large vocabularies and out-of-vocabulary issues severely affect Neural Language Models (NLMs) of source code, degrading their performance and rendering them unable to scale.

In this paper, we address this issue by: 1) studying how various modelling choices impact the resulting vocabulary on a large-scale corpus of 13,362 projects; 2) presenting an open vocabulary source code NLM that can scale to such a corpus, 100 times larger than in previous work; and 3) showing that such models outperform the state of the art on three distinct code corpora (Java, C, Python). To our knowledge, these are the largest NLMs for code that have been reported.

All datasets, code, and trained models used in this work are publicly available. 

## Kirschner et al: [Debugging Inputs](https://publications.cispa.saarland/3060/1/camera-ready-submission.pdf)

When a program fails to process an input, it need not be the program code that is at fault. It can also be that the input data is faulty, for instance as result of data corruption. To get the data processed, one then has to debug the input data—that is,

1.  identify which parts of the input data prevent processing, and
2.  recover as much of the (valuable) input data as possible.

In this paper, we present a general-purpose algorithm called ddmax that addresses these problems automatically. Through experiments, ddmax maximizes the subset of the input that can still be processed by the program, thus recovering and repairing as much data as possible; the difference between the original failing input and the “maximized” passing input includes all input fragments that could not be processed. To the best of our knowledge, ddmax is the first approach that fixes faults in the input data without requiring program analysis. In our evaluation, ddmax repaired about 69% of input files and recovered about 78% of data within one minute per input.

## Krueger et al: [Neurological Divide: An fMRI Study of Prose and Code Writing](https://dijkstra.eecs.umich.edu/fmri/icse20-data/icse2020-fmri-preprint.pdf)

Software engineering involves writing new code or editing existing code. Recent efforts have investigated the neural processes associated with reading and comprehending code—however, we lack a thorough understanding of the human cognitive processes underlying code writing. While prose reading and writing have been studied thoroughly, that same scrutiny has not been applied to code writing. In this paper, we leverage functional brain imaging to investigate neural representations of code writing in comparison to prose writing. We present the first human study in which participants wrote and edited code and prose while undergoing a functional magnetic resonance imaging (fMRI) brain scan, making use of a full-sized fMRI-safe QWERTY keyboard.

We find that code writing and prose writing are significantly dissimilar neural tasks. While prose writing entails significant left hemisphere activity associated with language, code writing involves more activations of the right hemisphere, including regions associated with attention control, working memory, planning and spatial cognition. These findings are unlike existing work in which code and prose comprehension were studied. By contrast, we present the first evidence suggesting that code and prose \emph{writing} are quite dissimilar at the neural level.

## Louis et al: [Where Should I Comment My Code? A Dataset and Model for Predicting Locations that Need Comments](https://homes.cs.washington.edu/~mernst/pubs/predict-comments-icse2020.pdf)

Programmers should write code comments, but not on every line of code. We have created a machine learning model that suggests locations where a programmer should write a code comment. We trained it on existing commented code to learn locations that are chosen by developers. Once trained, the model can predict locations in new code. Our models achieved precision of 74% and recall of 13% in identifying comment-worthy locations. This first success opens the door to future work, both in the new where-to-comment problem and in guiding comment generation. Our code and data is available at http://groups.inf.ed.ac.uk/cup/comment-locator/. 

## Overney et al: [How to Not Get Rich: An Empirical Study of Donations in Open Source](https://cmustrudel.github.io/papers/overney20donations.pdf)

Open source is ubiquitous and critical infrastructure, yet funding and sustaining it is challenging. While there are many different funding models for open-source donations and concerted efforts through foundations, donation platforms like Paypal, Patreon, or OpenCollective are popular and low-bar forms to raise funds for open-source development, for which GitHub recently even built explicit support. With a mixed-method study, we explore the emerging and largely unexplored phenomenon of donations in open source: We quantify how commonly open-source projects ask for donations, statistically model characteristics of projects that ask for and receive donations, analyze for what the requested funds are needed and used, and assess whether the received donations achieve the intended outcomes. We find 25,885 projects asking for donations on GitHub, often to support engineering activities; however, we also find no clear evidence that donations influence the activity level of a project. In fact, we find that donations are used in a multitude of ways, raising new research questions about effective funding.

## Rahman et al: [*Gang of Eight*: A Defect Taxonomy for Infrastructure as Code Scripts](https://akondrahman.github.io/papers/icse20_acid.pdf)

Defects in infrastructure as code (IaC) scripts can have serious consequences, for example, creating large-scale system outages. A taxonomy of IaC defects can be useful for understanding the nature of defects, and identifying activities needed to fix and prevent defects in IaC scripts. The goal of this paper is to help practitioners improve the quality of infrastructure as code (IaC) scripts by developing a defect taxonomy for IaC scripts through qualitative analysis. We develop a taxonomy of IaC defects by applying qualitative analysis on 1,448 defect-related commits collected from open source software (OSS) repositories of the Openstack organization. We conduct a survey with 66 practitioners to assess if they agree with the identified defect categories included in our taxonomy. We quantify the frequency of identified defect categories by analyzing 80,425 commits collected from 291 OSS repositories spanning across 2005 to 2019.

Our defect taxonomy for IaC consists of eight categories, including a category specific to IaC called idempotency (i.e., defects that lead to incorrect system provisioning when the same IaC script is executed multiple times). We observe the surveyed 66 practitioners to agree most with idempotency. The most frequent defect category is configuration data i.e., providing erroneous configuration data in IaC scripts. Our taxonomy and the quantified frequency of the defect categories can help practitioners to improve IaC script quality by prioritizing verification and validation efforts.

## Song et al: [Using Peer Code Review as an Educational Tool](https://dl.acm.org/doi/pdf/10.1145/3341525.3387370)

Code-review, the systematic examination of source code, is widely used in industry, but seldom used in courses. We designed and implemented a rubric-driven online peer code-review system (PCR) that we have deployed for two semesters, during which 228 students performed over 1003 code reviews. PCR is designed to meet four goals: (1) Provide timely feedback to students on their submissions, (2) Teach students the art of code review, (3) Allow custom feedback on submissions even in massive online classes, and (4) Allow students to learn from each other. We report on using PCR, in particular, the accuracy of student-based reviews, the surprising number of free-form comments made by students, the variability of staff-based reviews, how student engagement impacts the accuracy, the additional workload, and anecdotal perspectives of students. We describe some critical design considerations for PCR including rubric design, the importance of PCR training on each assignment to acclimate students to the rubric, and how we match student reviewers to student submissions.

## Wang et al: [An Empirical Study on Regular Expression Bugs](https://wangpeipei90.github.io/papers/saner2019_preprint.pdf)

Understanding the nature of regular expression (regex) issues is important to tackle practical issues developers face in regular expression usage. Knowledge about the nature and frequency of various types of regular expression issues, such as those related to performance, API misuse, and code smells, for example, can guide testing, inform documentation writers, and motivate refactoring efforts. However, beyond ReDoS (Regular expression Denial of Service), little is known about to what extent regular expression issues affect software development and how these issues are addressed in practice.

This paper presents a comprehensive empirical study of 350 merged regex-related pull requests (PRs) from Apache, Mozilla, Facebook, and Google GitHub repositories. Through classifying the root causes and manifestations of those bugs, we show that incorrect regular expression behavior is the dominant root cause of regular expression bugs (46.3%). The remaining root causes are incorrect API usage (9.3%) and other code issues that require regular expression changes in the fix (29.5%). By studying the code changes of regex-related pull requests, we observe that fixing regular expression bugs is nontrivial as it takes more time and more lines of code to fix them compared to the general pull requests. The results of this study contribute to a broader understanding of the practical problems faced by developers when using regular expressions.

## Wang et al: [Better Code, Better Sharing: On the Need of Analyzing Jupyter Notebooks](https://arxiv.org/ftp/arxiv/papers/1906/1906.05234.pdf)

By bringing together code, text, and examples, Jupyter notebooks have become one of the most popular means to produce scientific results in a productive and reproducible way. As many of the notebook authors are experts in their scientific fields, but laymen with respect to software engineering, one may ask questions on the quality of notebooks and their code. In a preliminary study, we experimentally demonstrate that Jupyter notebooks are inundated with poor quality code, e.g., not respecting recommended coding practices, or containing unused variables and deprecated functions. Considering the education nature of Jupyter notebooks, these poor coding practices as well as the lacks of quality control might be propagated into the next generation of developers. Hence, we argue that there is a strong need to programmatically analyze Jupyter notebooks, calling on our community to pay more attention to the reliability of Jupyter notebooks.

## Wurzel Gonçalves et al: [Do Explicit Review Strategies Improve Code Review Performance?](https://sback.it/publications/msr2020rr.pdf)

**Context**: Code review is a fundamental, yet expensive part of software engineering. Therefore, research on understanding code review and its efficiency and performance is paramount.

**Objective**: We aim to test the effect of a guidance approach on review effectiveness and efficiency. This effect is expected to work by lowering the cognitive load of the task; thus, we analyze the mediation relationship as well.

**Method**: To investigate this effect, we employ an experimental design where professional developers have to perform three code reviews. We use three conditions: no guidance, a checklist, and a checklist-based review strategy. Furthermore, we measure the reviewers’ cognitive load.

**Limitations**: The main limitations of this study concern the specific cohort of participants, the mono-operation bias for the guidance conditions, and the generalizability to other changes and defects.

## Zampetti et al: [An Empirical Characterization of Bad Practices in Continuous Integration](https://docs.google.com/viewer?a=v&pid=sites&srcid=Z2VyYXJkb2NhbmZvcmEubmV0fHd3d3xneDozNGQ1MjFhYTk3MDcxMDY)

Continuous Integration (CI) has been claimed to introduce several benefits in software development, including high software quality and reliability. However, recent work pointed out challenges, barriers and bad practices characterizing its adoption. This paper empirically investigates what are the bad practices experienced by developers applying CI. The investigation has been conducted by leveraging semi-structured interviews of 13 experts and mining more than 2,300 Stack Overflow posts. As a result, we compiled a catalog of 79 CI bad smells belonging to 7 categories related to different dimensions of a CI pipeline management and process. We have also investigated the perceived importance of the identified bad smells through a survey involving 26 professional developers, and discussed how the results of our study relate to existing knowledge about CI bad practices. Whilst some results, such as the poor usage of branches, confirm existing literature, the study also highlights uncovered bad practices, e.g., related to static analysis tools or the abuse of shell scripts, and contradict knowledge from existing literature, e.g., about avoiding nightly builds. We discuss the implications of our catalog of CI bad smells for (i) practitioners, e.g., favor specific, portable tools over hacking, and do not ignore nor hide build failures, (ii) educators, e.g., teach CI culture, not just technology, and teach CI by providing examples of what not to do, and (iii) researchers, e.g., developing support for failure analysis, as well as automated CI bad smell detectors.

## Zhang et al: [An Empirical Study on Program Failures of Deep Learning Jobs](http://hongyujohn.github.io/icse20-main-199.pdf)

Deep learning has made significant achievements in many application areas. To train and test models more efficiently, enterprise developers submit and run their deep learning programs on a shared, multi-tenant platform. However, some of the programs fail after a long execution time due to code/script defects, which reduces the development productivity and wastes expensive resources such as GPU, storage, and network I/O.

This paper presents the first comprehensive empirical study on program failures of deep learning jobs. 4960 real failures are collected from a deep learning platform in Microsoft. We manually examine their failure messages and classify them into 20 categories. In addition, we identify the common root causes and bug-fix solutions on a sample of 400 failures. To better understand the current testing and debugging practices for deep learning, we also conduct developer interviews. Our major findings include: (1) 48.0% of the failures occur in the interaction with the platform rather than in the execution of code logic, mostly due to the discrepancies between local and platform execution environments; (2) Deep learning specific failures (13.5%) are mainly caused by inappropriate model parameters/structures and framework API misunderstanding; (3) Current debugging practices are not efficient for fault localization in many cases, and developers need more deep learning specific tools. Based on our findings, we further suggest possible research topics and tooling support that could facilitate future deep learning development.

## Zieris and Prechelt: [Explaining Pair Programming Session Dynamics from Knowledge Gaps](http://www.inf.fu-berlin.de/inst/ag-se/pubs/ZiePre20-ppsessiondyn.pdf)

**Background**: Despite a lot of research on the effectiveness of Pair Programming (PP), the question when it is useful or less useful remains unsettled.

**Method**: We analyze recordings of many industrial PP sessions with Grounded Theory Methodology and build on prior work that identified various phenomena related to within-session knowledge build-up and transfer. We validate our findings with practitioners.

**Result**: We identify two fundamentally different types of required knowledge and explain how different constellations of knowledge gaps in these two respects lead to different session dynamics. Gaps in project-specific systems knowledge are more hampering than gaps in general programming knowledge and are dealt with first and foremost in a PP session.

**Conclusion**: Partner constellations with complementary knowledge make PP a particularly effective practice. In PP sessions, differences in system understanding are more important than differences in general software development knowledge.

## And a reminder

Every single one of the sources cited in the Christchurch killer's manifesto had a store on Shopify.
The company has refused to deplatform any of them.
