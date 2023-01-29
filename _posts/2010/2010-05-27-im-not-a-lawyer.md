---
title: "I'm Not a Lawyer..."
date: 2010-05-27 07:44:58
year: 2010
---
Google recently announced a <a href="http://code.google.com/apis/predict/">Prediction API</a>:
<blockquote>The Prediction API enables access to Google's machine learning algorithms  to analyze your historic data and predict likely future outcomes.  Upload your data..., then use the Prediction API to make  real-time decisions in your applications.</blockquote>
Interesting, and possibly very useful, but is Google going to keep a copy of my data for its own use? Or will it record some characteristics of that data (e.g., to improve its algorithms)?  The former seems unlikely, but then, so did the success of Javascript as a general-purpose programming language. The latter sounds very possible, which makes me worry about accidental information leakage, particularly through post-facto correlation.

Their <a href="http://www.google.com/privacypolicy.html">privacy policy</a> doesn't explicitly mention uploaded data (though it's very clear about what Google will and won't do with personal data). As of right now, their <a href="http://www.google.com/intl/en/privacy.html">product-specific elaboration</a> doesn't seem to have anything either. The <a href="http://code.google.com/apis/predict/docs/terms.html">Terms of Service</a> for their APIs looks promising, but Section 4 ("Your Data") just says:
<ol>
  <li>You're responsible for your data.</li>
  <li>" Google claims no ownership or control over any of your Data.  You  retain copyright and any other rights you already hold in the Data, and  you are responsible for protecting those rights, as appropriate." OK, but that <em>doesn't</em> say that they won't keep a copy, or keep a copy of any metadata or aggregated statistics that they calculate from it.</li>
  <li>"By submitting, posting, displaying, or transmitting Data on or  through the Service, you give Google permission to process your Data for  the sole purpose of enabling Google to provide you with the Service in  accordance with its privacy policy." OK, they're not allowed to process my data to do other things than the service I signed up for, but again, what about any derived metadata?</li>
</ol>
I'm being deliberately paranoid here, but past experience with licensing and other legal matters has taught me to assume that contracts mean exactly, and only, what's written. I'd be interested in hearing from anyone who actually <em>is</em> a lawyer about whether my "aggregate, record, and use" scenario could be defended.
