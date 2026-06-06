---
title: "Algorithmic Criminal Justice"
date: 2026-05-06
category: sdgc ethics
---

In May 2016, two reporters at ProPublica named Julia Angwin and Jeff Larson
published an investigation of a risk assessment tool called COMPAS,
which was being used in Broward County, Florida to help judges make bail and sentencing decisions.
COMPAS was built by a company called Northpointe
and had been adopted by courts across the United States;
it produced a score from one to ten predicting a defendant's likelihood of reoffending.
The ProPublica analysis found that Black defendants were nearly twice as likely as white defendants
to be falsely flagged as high risk,
i.e., 
to be scored as likely to reoffend when they did not,
while white defendants were more likely to be falsely flagged as low risk
and then go on to commit new offenses.

COMPAS does not use race as an input.
Its inputs include things like criminal history, age, employment status, and residential stability.
These variables are legally permissible and individually plausible as predictors of behavior.
They are also deeply correlated with race,
as a consequence of decades of differential policing,
prosecution,
and sentencing.
A Black defendant with the same criminal history as a white defendant
is likely to have received that history because of more intensive police scrutiny,
in a neighborhood with higher patrol density,
in a jurisdiction with more aggressive charging practices.
The algorithm does not *need* to see race;
the other, legal inputs serve as proxies.

The dispute between ProPublica and Northpointe could not be resolved by better data.
Computer scientists Alexandra Chouldechova proved in 2017 that
no algorithm can simultaneously provide both equal false positive rates across groups
*and* equal calibration across groups
when the underlying base rates differ between groups.
Broward County's Black and white populations had different historical recidivism rates,
as a result of differential enforcement.
No single risk assessment instrument could treat both groups equitably by both measures at once.
This is not a bug that better engineering will fix;
it is a mathematical consequence of deploying statistical tools
using data produced by historical discrimination.

<div class="callout" markdown="1">

Actuarial tools in criminal justice are not a recent invention.
The criminologist Ernest Burgess developed the first statistical parole prediction instrument
in Illinois in the 1920s,
using factors including offense type, employment history, and national origin.
His tool was adopted by several state parole boards and used for decades.
The national origin variable,
which explicitly penalized immigrants,
was quietly dropped after the Second World War,
but the broader approach survived.
By the time the COMPAS investigation was published in 2016,
at least forty-six US states were using risk assessment instruments somewhere in their criminal justice systems.
The tools were marketed as scientific improvements over subjective judicial discretion,
but most simply encoded prior biases in a form that was harder to question.

</div>

In January 2020,
Detroit police arrested Robert Williams,
a Black man,
on suspicion of theft.
He was taken to a police station,
shown a photograph taken from surveillance footage,
and asked if it was him.
He held the photograph next to his face and said:
"I hope you don't think all Black men look alike."

The photograph was not Williams,
but had been identified as a match by a facial recognition system operated by the Michigan State Police.
This was the first documented case of a wrongful arrest
directly resulting from facial recognition identification,
but more were to come.
In every such case over the next two years,
the wrongfully arrested person was Black.
Audits done by the National Institute of Standards and Technology had shown that
these facial recognition systems
had error rates for darker-skinned faces
that were ten to one hundred times higher than for lighter-skinned faces.
They were deployed anyway.

The legal framework for challenging these tools is nearly nonexistent.
COMPAS and similar instruments are proprietary.
When defendants have sought to examine the algorithms,
courts have generally ruled that the commercial trade secret protects the code from disclosure.
In other words,
a person's liberty can be determined by a calculation they are legally prevented from inspecting or contesting.
The right to confront the evidence against you,
which has been foundational to criminal procedure since the seventeenth century,
does not currently extend to the algorithms that generate that "evidence".

Virginia Eubanks's research on automated decision-making in social services
tells a similar story in a different context.
In Indiana,
an automated eligibility determination system introduced in 2006 to manage welfare, Medicaid, and food stamps
terminated benefits for hundreds of thousands of low-income residents,
often for minor procedural failures that the previous human caseworkers would have sorted out with a phone call.
In Allegheny County, Pennsylvania, a predictive risk model used by child protective services
assessed children's likelihood of being removed from their families
using data that included whether their parents had used the county's crisis services,
creating direct incentives for poor families not to seek help.
In both cases,
the introduction of algorithmic decision-making
was described as an improvement over biased human judgment.
What it actually did was entrench the biases already present in the data
while removing human discretion.

India's Aadhaar program is the same story at continental scale.
Introduced as a biometric identity database,
Aadhaar was linked to food ration distribution in several states starting around 2016.
The system required residents to authenticate their identity with a fingerprint scan at the ration shop.
Agricultural workers whose fingerprints had worn smooth from years of labor,
elderly residents whose biometrics had drifted with age,
and anyone whose enrollment data contained errors were denied food.
Journalists and researchers documented deaths linked to starvation
after benefits were terminated because a scanner could not read someone's hand.
The Indian government's response was largely to attribute failures to local implementation
rather than to the design itself.

The outcome was different in the Netherlands.
The Dutch government's SyRI system cross-referenced
seventeen government datasets to assign welfare fraud risk scores,
and was deployed predominantly in lower-income, immigrant-heavy neighborhoods.
In 2020,
a Dutch court struck it down as a violation of the European Convention on Human Rights,
ruling that the government had not explained how it worked,
demonstrated that it was accurate,
or justified why it targeted certain communities.
The fact that it required a human rights case rather than any technology-specific law
is as telling as the victory itself.

*[see the whole series](@root/sdgc/) · [email me](mailto:gvwilson@third-bit.com?subject=SDGC)*

<span id="Chouldechova2017">Chouldechova2017</span>
:   Alexandra Chouldechova:
    "Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments".
    *Big Data*,
    5(2),
    2017,
    doi:10.1089/big.2016.0047.

<span id="Eubanks2018">Eubanks2018</span>
:   Virginia Eubanks:
    *Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor*.
    St. Martin's Press,
    2018,
    978-1250074317.

<span id="Khera2019">Khera2019</span>
:   Reetika Khera (ed.):
    *Dissent on Aadhaar: Big Data Meets Big Brother*.
    Orient BlackSwan,
    2019,
    978-9352875429.

<span id="Oneil2016">ONeil2016</span>
:   Cathy O'Neil:
    *Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy*.
    Crown,
    2016,
    978-0553418811.

<span id="Pasquale2015">Pasquale2015</span>
:   Frank Pasquale:
    *The Black Box Society: The Secret Algorithms That Control Money and Information*.
    Harvard University Press,
    2015,
    978-0674368279.
