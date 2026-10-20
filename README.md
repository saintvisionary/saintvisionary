<!-- Profile README: lives in the public repo saintvisionary/saintvisionary -->

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=24&duration=3200&pause=900&color=FF9900&center=true&vCenter=true&width=640&lines=Hi%2C+I'm+Tyler+%F0%9F%91%8B;I+secured+doors.+Now+I+secure+identities.;Humans%2C+machines%2C+and+AI+agents." alt="Hi, I'm Tyler. I secured doors. Now I secure identities." />

**Access control → Identity engineering**

*I secure AI agents, and I use AI agents to secure identity.*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-connect-0A66C2?style=flat-square)](https://www.linkedin.com/in/tyler-bynum-838b8132b)
[![Featured](https://img.shields.io/badge/featured-AI_Agent_Spend_Gate-FF9900?style=flat-square)](https://github.com/saintvisionary/AI-Agent-Spend-Gate)

</div>

---

### 🛡️ About me

- I work in **physical security and access control** (C•CURE 9000): badges, readers, door schedules, and who gets in where.
- I'm moving into **IAM / identity engineering**. The job is the same. The doors are now APIs, and many of the people walking through them are agents.
- My focus is **non-human identity**: giving AI agents their own identity, a human owner, least privilege, approval for risky actions, and a full audit trail.

### 🔑 Same controls, new doors

Everything I know from the physical side has an identity equivalent:

| Physical access control | Identity engineering |
|:---|:---|
| Badge | Credential / token |
| Card reader | Policy enforcement point |
| Access panel | Policy decision point |
| Clearance and door groups | Roles and permission sets |
| Door schedules | Conditional access |
| Two-person rule | Human-in-the-loop approval |
| Deactivate the badge on the last day | Deprovisioning (joiner-mover-leaver) |
| Event log and alarm monitoring | Audit log → SIEM |

---

### 🚀 Featured project

<div align="center">

<a href="https://github.com/saintvisionary/AI-Agent-Spend-Gate">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=saintvisionary&repo=AI-Agent-Spend-Gate&theme=transparent&title_color=FF9900&icon_color=FF9900&hide_border=true" alt="AI Agent Spend Gate" />
</a>

</div>

**[AI Agent Spend Gate](https://github.com/saintvisionary/AI-Agent-Spend-Gate):** *your AI agent has a company card. Here's what keeps it honest.*

```mermaid
flowchart LR
    A["🤖 Agent<br/>Amazon Bedrock<br/><i>proposes</i>"] --> B["🧠 Decider 2B<br/>guardrail<br/><i>is it honest?</i>"]
    B --> C["🛂 Spend Gate<br/>Python rules<br/><i>is it allowed?</i>"]
    C --> D["💳 Order"]
    B -. "unsure" .-> H["🙋 Human"]
    C -. "over limit" .-> H
```

- **Three layers of control.** The LLM proposes, Strands Decider 2B checks honesty (grounded, injected, mislabeled), and a deny-by-default rules engine decides permission.
- **Built for prompt injection.** A poisoned note in a tool result tries to buy gift cards. The guardrail denies it before the tool runs, and the rules would block it anyway.
- **Calibrated confidence.** Uncertain calls go to a human, not to a guess.
- **Reusable `#guardrails` pattern** that works with any Strands agent.

---

### 🧰 Toolbox

<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white" alt="AWS" />
<img src="https://img.shields.io/badge/Amazon_Bedrock-01A88D?style=for-the-badge" alt="Amazon Bedrock" />
<img src="https://img.shields.io/badge/Strands_Agents-FF9900?style=for-the-badge" alt="Strands Agents" />
<img src="https://img.shields.io/badge/AWS_IAM-DD344C?style=for-the-badge" alt="AWS IAM" />
<img src="https://img.shields.io/badge/Microsoft_Entra_ID-0078D4?style=for-the-badge" alt="Microsoft Entra ID" />
<img src="https://img.shields.io/badge/Splunk-000000?style=for-the-badge&logo=splunk&logoColor=white" alt="Splunk" />
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
</p>

### 📜 Certifications

![Security+](https://img.shields.io/badge/CompTIA-Security%2B-C8202F?style=flat-square)
![GSEC](https://img.shields.io/badge/GIAC-GSEC-1B365D?style=flat-square)
![GCIH](https://img.shields.io/badge/GIAC-GCIH_(in_progress)-6E7781?style=flat-square)
![SC-300](https://img.shields.io/badge/Microsoft-SC--300_(in_progress)-6E7781?style=flat-square)

---

<div align="center">

<sub>Least privilege for people, machines, and agents. 🔐</sub>

</div>
