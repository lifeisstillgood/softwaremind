==============================
COmpanies are version numbered
==============================


Yeah.  

https://news.ycombinator.com/item?id=38625907

It's not so much "not JIRA", it's that managing code bases outside of the code base is hard and awkward. And due respect to fossil-scm, I don't know if any way to do it otherwise.
The goal here is to look at something that tells an organisation why chnages to a codebase occurred. Each individual commit can have a nice explanation (in a given human language) of why that specific change occurred. But how does one link other commits, dozens or hundreds or orders of magnitude more.
Can they be accounted for to investors, auditors, regulators?
But equally demanding that commits link to something that links to why, it demands that the rest of the business also link to that something (ie JIRA) so they can explain why they expended time and effort
JIRA or whatever ticketing system, will slowly become the central repository of justification for expense - a great position sure, but also dangerous.
Following on, having some repository of why - of cost drivers - forces not just the software developers but the whole business to justify its activity against the repository. This seems hugely similar to lawyers billing by the 15 minute increment, and indeed a git repo will provide good billing like data too !
But the issue still exists - if I say my activity links to ticket number 1234, then we have a hierarchy (?) of what 1234 links to. The smacks of stories and epics and the whole agile package, but is also a common accounting process
my issue is that this is a neat, backwards looking explanation for what was done. It's not a good way to manage forwards.
And often I find the problem is people wanting to use JIRAs tickets to manage what will be done, not account for what has been done
reply
	
xorcist 5 hours ago | parent | next [–]

Why the need to reinvent the commit message? Look at how Linux does it. If it's good enough for a globally distributed organization creating the operating system the cloud and most phones run on, it can't be completely wrong. They rely solely on mail and commit messages.
Ticketing systems are useful for a lot of other things such as keeping track of work on an individual level, or managing project resource allocations on a company wide level, but I'm not sure it's the best tool to do audits and have accountability. It will at best be a secondary source of that data.
reply
	
*

1 point by lifeisstillgood 1 minute ago | root | parent | next | edit | delete [–]

And the Linux mailing lists are a great example of what I mean - deciding what to do and why is a huge upfront discussion - one they do in the open. but it's a crap backwards looking method for a summary.
Most businesses hide the upfront discussion (or at least keep it to a smaller set of people who have often conflicting incentives for decisions as well (we tend to refer to this as politics but that's a bit like fish moaning about water.)
Anyway the point is that Linux shows how to make good decisions in the open (usually) - a process that I think most would 10x good decision making in most businesses but also lead to huge other sets of problems (worth it in my view but ...).
But Linux does not have a simple way of post-hoc justifying the decisions unless one reads the threads (which is where the recent post of open source journalist at lwn was a great idea)
But things like Jira, external ticket stores are good at providing a hierarchy to post hoc justify the decision - even if they are a terrible way to plan forwards.
So the ideal I guess is some kind of open architecture discussion upfront and some kind of extract and rebuild the rationale from commits (ie in house journalism?)
